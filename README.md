<div align=center>
  <h1>yiffer-dl-cloud</h1>
  <p>CLI tool to download comics from yiffer.xyz.<br>Downloads by comic name, saves original images and a zip file for use with comic readers.<br> After downloading it will also upload to a Nextcloud or Owncloud server.</p>
</div>
  
### DEPS
- Python 3.x
- [Requests 2.x](https://pypi.org/project/requests/)
- [pyocclient] (https://github.com/owncloud/pyocclient)

### INSTALL
#### Auto (if on Linux or MacOS):
Install Requests and pyocclient:
```
python3 -m pip install requests
python3 -m pip install pyocclient
```
Then run the installer file using:
```
git clone https://github.com/kiosion/yiffer-dl && \
cd yiffer-dl && \
chmod +x ./install.sh && \
sudo ./install.sh
```

#### Manual:
Install Requests and pyocclient:
```
python3 -m pip install requests
python3 -m pip install pyocclient
```
Clone the repo:
```
git clone https://github.com/shadowskyhawk/yiffer-dl-cloud
```
Either:
- Run directly with python (`python3 ./ydl.py`)
- Add to your system PATH
- Add to your shell as an alias


### Configure
The file config.py is used for setting your cloud server credentials.
user - Your cloud username
pass - Your cloud password
server - The base URL leading to your cloud server (e.g. "https://cloud.example.com/")
folder - The folder on your cloud server you would like to upload to (e.g. "Yiff/Comics")
format - Defines the extension of the uploaded file. Default is .zip, but you can change this to "cbz" if you want.


### USAGE
The syntax for commands is:

```
python3 ydl.py "Comic Name"
```

Image files are saved to ~/ydl/comic_name/Imgs
An archive of the images is saved to ~/ydl/comic_name/comic_name.zip
The archive is then uploaded to Nextcloud based on your server url and selected cloud folder.

### PLANNED FEATURES
- Choosing local download folder
- Toggling archiving, if you just want the images without zipping
- Toggling cloud support, in case you just want to download locally
- Uploading the images instead of the archive

### CREDITS

Based on https://github.com/kiosion/yiffer-dl, which was itself based off of https://github.com/TNTINC/yiffer-dl, modified to add cloud upload support.
