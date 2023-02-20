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

# Fix home directory links
homeDir = os.path.expanduser("~")
localDir = config.downloadFolder.replace("~", homeDir)
archiveDir = config.archiveFolder.replace("~", homeDir)

# Input
if len(argv) < 2:
    print("Usage: {} <yiffer.xyz comic name>".format(argv[0]))
    exit(1)

name = argv[1]

def download_comic(name, localDir):
    img_id = 1
    err = None

    # Get comic name and create dir in dl/
    cname = name.replace(" ", config.space)
    cname_url = name.replace(" ", "%20")

    # Create download folder based on comic name
    try:
        os.mkdir(os.path.join(localDir, cname))
    except:
        print(f"Comic directory already exists: '{cname}'")
    try:
        os.mkdir(os.path.join(localDir, cname))
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
        err = download_image(localDir, cname, img_id)
        img_id = img_id + 1
        if img_id > comic_length:
            print("=> Done downloading...")
            zip_files(localDir, cname)
            cloud_upload(localDir, cname, config)
            break

def download_image(localDir, cname, img_id):
    # Parse URL
    img_url = urljoin(
        "comics/", 
        cname.replace(" ", "%20"), 
        f"00{img_id}.jpg"[-7:])
    dl_url = urljoin("https://static.yiffer.xyz/", img_url)

    # Check image exists
    if os.path.isfile(os.path.join(localDir, cname) + "/" + f"00{img_id}.jpg"[-7:]):
        print(f"Image already exists: '{img_id}.jpg'")
        return None

    # Download image
    res = requests.get(dl_url, stream = True)
    if res.status_code == 200:
        with open(os.path.join(localDir, cname) + "/" + f"00{img_id}.jpg"[-7:], 'wb') as f:
            res.raw.decode_content = True
            shutil.copyfileobj(res.raw, f)
        print("Downloaded image " + f"00{img_id}"[-3:])
    else:
        print(f"Error {res.status_code}: Image {img_id} could not be retrieved")
        return res.status_code

def zip_files(localDir, cname):
    print("=> Zipping files...")
    if os.path.isfile(archiveDir + f"/{cname}.zip"):
        print(f"Comic file already exists: '{cname}.zip'")
        print("=> Done!")
        return None
    shutil.make_archive(archiveDir + f"/{cname}", "zip", os.path.join(localDir, cname))
    print("=> Done!")

def cloud_upload(localDir, cname, config):
    # Login to Nextcloud/Owncloud
    print("=> Logging in to cloud server")
    oc = owncloud.Client(config.server)
    oc.login(config.username, config.password)
    print("=> Done!")
    print("=> Uploading " + config.uploadFormat + "...")
    # upload file
    oc.put_file(config.uploadFolder + f"/{cname}.{config.uploadFormat}", archiveDir + f"/{cname}.zip")
    print("=> Done!")

if __name__ == "__main__":
    try: os.mkdir(localDir)
    except: pass
    download_comic(name, localDir)
