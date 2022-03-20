# yiffer-dl
Downloads comics as images from yiffer.xyz

### DEPS
- Python 3.x
- [Requests 2.x](https://pypi.org/project/requests/)

### INSTALL
#### Auto:
If on Linux or MacOS, run the installer using:
```
git clone https://github.com/kiosion/yiffer-dl && \
cd yiffer-dl && \
chmod +x ./install.sh && \
sudo ./install.sh
```

#### Manual:
Else, clone this repo (`git clone https://github.com/kiosion/yiffer-dl`), and either:
- Run directly with python
- Add to your system PATH
- Add to your shell as an alias

### USAGE
The syntax for commands is:

```
python3 ydl.py "Comic Name"
```

Images are saved to ~/ydl/comic_name/Imgs/
An archive of the images is saved to ~/ydl/comic_name/comic_name.zip

### CREDITS

Based on https://github.com/TNTINC/yiffer-dl, rewritten to work again.
