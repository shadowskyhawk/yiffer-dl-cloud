<div align=center>
  <h1>yiffer-dl</h1>
  <p>Simple CLI tool to download comics from yiffer.xyz.<br>Downloads by comic name, and saves original images + .zip file for use with comic readers</p>
</div>
  
### DEPS
- Python 3.x
- [Requests 2.x](https://pypi.org/project/requests/)

### INSTALL
#### Auto (if on Linux or MacOS):
Install Requests:
```
python3 -m pip install requests
```
Then run the installer file using:
```
git clone https://github.com/kiosion/yiffer-dl && \
cd yiffer-dl && \
chmod +x ./install.sh && \
sudo ./install.sh
```

#### Manual:
Install Requests:
```
python3 -m pip install requests
```
Clone the repo:
```
git clone https://github.com/kiosion/yiffer-dl
```
Either:
- Run directly with python (`python3 ./ydl.py`)
- Add to your system PATH
- Add to your shell as an alias

### USAGE
The syntax for commands is:

```
python3 ydl.py "Comic Name"
```

Image files are saved to ~/ydl/comic_name/Imgs
An archive of the images is saved to ~/ydl/comic_name/comic_name.zip

### CREDITS

Based on https://github.com/TNTINC/yiffer-dl, rewritten to work again.
