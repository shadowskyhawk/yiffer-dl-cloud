#!/usr/bin/env python3

import os
import requests
import json
from sys import argv
import shutil
from posixpath import join as urljoin
from zipfile import ZipFile
import owncloud
import config

# Constants
U_HOME = os.path.expanduser("~")
DL_LOC = os.path.join(U_HOME, config.downloadFolder)

# Input
if len(argv) < 2:
    print("Usage: {} <yiffer.xyz comic name>".format(argv[0]))
    exit(1)

name = argv[1]

def download_comic(name, DL_LOC):
    img_id = 1
    err = None

    # Get comic name and create dir in dl/
    cname = name.replace(" ", config.space)
    cname_url = name.replace(" ", "%20")

    # Create download folder based on comic name
    try:
        os.mkdir(os.path.join(DL_LOC, cname))
    except:
        print(f"Comic directory already exists: '{cname}'")
    try:
        os.mkdir(os.path.join(DL_LOC, cname, "Images"))
    except:
        print(f"Comic directory already exists: '{cname}/Images'")
    
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
            cloud_upload(DL_LOC, cname, config)
            break

def download_image(DL_LOC, cname, img_id):
    # Parse URL
    img_url = urljoin(
        "comics/", 
        cname.replace(" ", "%20"), 
        f"00{img_id}.jpg"[-7:])
    dl_url = urljoin("https://static.yiffer.xyz/", img_url)

    # Check image exists
    if os.path.isfile(os.path.join(DL_LOC, cname, "Images") + "/" + f"00{img_id}.jpg"[-7:]):
        print(f"Image already exists: '{img_id}.jpg'")
        return None

    # Download image
    res = requests.get(dl_url, stream = True)
    if res.status_code == 200:
        with open(os.path.join(DL_LOC, cname, "Images") + "/" + f"00{img_id}.jpg"[-7:], 'wb') as f:
            res.raw.decode_content = True
            shutil.copyfileobj(res.raw, f)
        print("Downloaded image " + f"00{img_id}"[-3:])
    else:
        print(f"Error {res.status_code}: Image {img_id} could not be retrieved")
        return res.status_code

def zip_files(DL_LOC, cname):
    print("=> Zipping files...")
    if os.path.isfile(config.archiveFolder + f"/{cname}.zip"):
        print(f"Comic file already exists: '{cname}.zip'")
        print("=> Done!")
        return None
    shutil.make_archive(config.archiveFolder + f"/{cname}", "zip", os.path.join(DL_LOC, cname, "Images"))
    print("=> Done!")

def cloud_upload(DL_LOC, cname, config):
    # Login to Nextcloud/Owncloud
    print("=> Logging in to cloud server")
    oc = owncloud.Client(config.server)
    oc.login(config.username, config.password)
    print("=> Done!")
    print("=> Uploading {format}...")
    # upload file
    oc.put_file(config.uploadFolder + f"/{cname}.{config.uploadFormat}", os.path.join(DL_LOC, cname) + f"/{cname}.zip")
    print("=> Done!")

if __name__ == "__main__":
    try: os.mkdir(DL_LOC)
    except: pass
    download_comic(name, DL_LOC)
