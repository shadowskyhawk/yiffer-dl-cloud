#!/usr/bin/env python3

import os
import requests
import json
from sys import argv
import shutil
from posixpath import join as urljoin
from zipfile import ZipFile

# Constants
U_HOME = os.path.expanduser("~")
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
        print(f"Comic directory already exists: '{cname}/Imgs'")
    
    # Get comic info from API (length, url)
    cname_api_url = ("https://yiffer.xyz/api/comics/"+cname_url)
    api_dict = json.loads(requests.get(cname_api_url).text)
    comic_length = api_dict["numberOfPages"]
    comic_artist = api_dict["artist"]
    url = "https://yiffer.xyz/"+cname_url

    print(f"=> Downloading '{name}'...")

    # Iterate for length of comic
    while err is None:
        err = download_image(DL_LOC, cname, img_id)
        img_id = img_id + 1
        if img_id > comic_length:
            print("=> Done downloading...")
            zip_files(DL_LOC, cname)
            break

def download_image(DL_LOC, cname, img_id):
    # Parse URL
    img_url = urljoin(
        "comics/", 
        cname.replace("_", "%20"), 
        f"00{img_id}.jpg"[-7:])
    dl_url = urljoin("https://static.yiffer.xyz/", img_url)

    # Check image exists
    if os.path.isfile(os.path.join(DL_LOC, cname, "Imgs") + "/" + f"00{img_id}.jpg"[-7:]):
        print(f"Image already exists: '{img_id}.jpg'")
        return None

    # Download image
    res = requests.get(dl_url, stream = True)
    if res.status_code == 200:
        with open(os.path.join(DL_LOC, cname, "Imgs") + "/" + f"00{img_id}.jpg"[-7:], 'wb') as f:
            res.raw.decode_content = True
            shutil.copyfileobj(res.raw, f)
        print("Downloaded image " + f"00{img_id}"[-3:])
    else:
        print(f"Error {res.status_code}: Image {img_id} could not be retrieved")
        return res.status_code

def zip_files(DL_LOC, cname):
    print("=> Zipping files...")
    if os.path.isfile(os.path.join(DL_LOC, cname) + f"/{cname}.zip"):
        print(f"Zip already exists: '{cname}.zip'")
        print("=> Done!")
        return None
    shutil.make_archive(os.path.join(DL_LOC, cname) + f"/{cname}", "zip", os.path.join(DL_LOC, cname, "Imgs"))
    print("=> Done!")

if __name__ == "__main__":
    try: os.mkdir(DL_LOC)
    except: pass
    download_comic(name, DL_LOC)
