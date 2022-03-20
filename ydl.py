#!/usr/bin/env python3

import os
import requests
import json
from sys import argv
import shutil
from shutil import make_archive
import urllib.request
from posixpath import join as urljoin
from os.path import expanduser
from zipfile import ZipFile

# Constants
U_HOME = expanduser("~")
DL_LOC = os.path.join(U_HOME, "ydl/")

# Input
if len(argv) < 2:
    print("Usage: {} <yiffer.xyz comic name>".format(argv[0]))
    exit(1)

name = argv[1]

def download_comic(name, DL_LOC):
    img_id = 1
    err = None

    # Get comic name and create dir in dl/
    cname = name.replace(" ", "_")
    cname_url = name.replace(" ", "%20")

    # Create download folder based on comic name
    try:
        os.mkdir(os.path.join(DL_LOC, cname))
    except:
        print(f"Comic directory already exists: '{cname}'")
    try:
        os.mkdir(os.path.join(DL_LOC, cname, "Imgs"))
    except:
        print(f"Comic directory already exists: '{cname}'")
    
    # Get comic info from API (length, url)
    cname_api_url = ("https://yiffer.xyz/api/comics/"+cname_url)
    api_dict = json.loads(requests.get(cname_api_url).text)
    comic_length = api_dict["numberOfPages"]
    comic_artist = api_dict["artist"]
    url = "https://yiffer.xyz/"+cname_url

    print(f"=> Downloading '{name}'...")

    # Iterate for length of comic
    while err is None:
        err = download_image(url, DL_LOC, cname, img_id)
        img_id = img_id + 1
        if img_id > comic_length:
            print("=> Done!")
            zip_files(DL_LOC, cname)
            break

def download_image(url, DL_LOC, cname, img_id):
    # Parse URL
    # format: ../comics/<comic name>/xxx.jpg
    img_url = urljoin(
        "comics/", 
        url.split("/")[-1], 
        "{0:03d}.jpg".format(img_id))
    url_parsed = urllib.parse.urlparse(url)
    base_url = "{uri.scheme}://static.{uri.netloc}/".format(uri=url_parsed)
    dl_url = urljoin(base_url, img_url)

    # Check image exists
    if os.path.isfile(os.path.join(DL_LOC, cname, "Imgs") + f"/{img_id}.jpg"):
        print(f"Image already exists: {img_id}.jpg")
        return None

    # Download image
    res = requests.get(dl_url, stream = True)

    # Save if res is OK
    if res.status_code == 200:
        # Save image
        with open(os.path.join(DL_LOC, cname, "Imgs") + "/" + f"00{img_id}.jpg"[-7:], 'wb') as f:
            res.raw.decode_content = True
            shutil.copyfileobj(res.raw, f)
        print("Downloaded image " + f"00{img_id}"[-3:])
    else:
        print('Error: Image ' + '{}'.format(img_id) + ' could not be retrieved')
        return res.status_code

def zip_files(DL_LOC, cname):
    print("=> Zipping files...")
    make_archive(os.path.join(DL_LOC, cname) + f"/{cname}", "zip", os.path.join(DL_LOC, cname, "Imgs"))
    print("=> Done!")

if __name__ == "__main__":
    # Make sure the dl directory exists
    try: os.mkdir(DL_LOC)
    except: pass

    # Run script
    download_comic(name, DL_LOC)
