<div align=center>
  <h1>yiffer-dl-cloud</h1>
  <p>CLI tool to download comics from yiffer.xyz.<br>Downloads by comic name, saves original images and a zip file for use with comic readers.<br> After downloading it will also upload to a Nextcloud or Owncloud server.</p>
</div>
  
### DEPS
- Python 3.x
- [Requests 2.x](https://pypi.org/project/requests/)
- [pyocclient](https://github.com/owncloud/pyocclient)

### INSTALL
#### Auto (if on Linux or MacOS):
Install Requests and pyocclient:
```
python3 -m pip install requests pyocclient
```
Then run the installer file using:
```
git clone https://github.com/shadowskyhawk/yiffer-dl-cloud && \
cd yiffer-dl-cloud && \
chmod +x ./install.sh && \
sudo ./install.sh
```

#### Manual:
Install Requests and pyocclient:
```
python3 -m pip install requests pyocclient
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
- downloadFolder - Local folder to download comics to. Default is ~/yiff-dl
- archiveFolder - Local folder all zip/cbz files are loaded into. Handy if you don't want them in subfolders.
- user - Your cloud username
- pass - Your cloud password
- server - The base URL leading to your cloud server (e.g. "https://cloud.example.com/")
- uploadFolder - The folder on your cloud server you would like to upload to (e.g. "Yiff/Comics")
- uploadFormat - Defines the extension of the uploaded file. Default is .zip, but you can change this to "cbz" if you want.
- space - Defines the seperator character for filenames. Default is an underscore (_) but can be replaced with a space or dash.


### USAGE
The syntax for commands is:

```
python3 ydl.py "Comic Name"
```

Image files are saved to ~/yiff-dl/comic_name/Imgs
An archive of the images is by default saved to ~/yiff-dl/comic_name/comic_name.zip, or where defined in config.py
The archive is then uploaded to the cloud based on your server url, cloud folder, and selected format.

### PLANNED FEATURES
- Choosing local download folder
- Toggling archiving, if you just want the images without zipping
- Toggling cloud support, in case you just want to download locally
- Uploading the images instead of the archive

### CREDITS

Based on https://github.com/kiosion/yiffer-dl, which is itself based off of https://github.com/TNTINC/yiffer-dl, modified to add cloud upload support.
