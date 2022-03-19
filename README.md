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
chmod +x ./install && \
sudo ./install
```

#### Manual:
Else, clone this repo (`git clone https://github.com/kiosion/yiffer-dl`), and either:
- Run directly with python
- Add to your system PATH
- Add to your shell as an alias

### USAGE
The syntax for commands is:

```
python3 ydl.py https://yiffer.xyz/comic%20name%20here 
```

Images are saved to ~/ydl/comic_name_here/

### CREDITS

Based on https://github.com/TNTINC/yiffer-dl, rewritten to work again.
