# MacApp-bundler
A program to put python scripts into a macOS application bundle. Should work.
## Installation
#### MacOS:
With homebrew:
`brew install python3 && python3 -m ensurepip && python3 -m pip install -r requirements.txt`
#### UNIX/GNU Linux
With python already installed: `python3 -m pip install -r requirements.txt`

Debian-like (ubuntu, etc.): `sudo apt install python3 python3-pip && pip3 install -r requirements.txt`

Others: `install python somehow... ; python3 -m pip install -r requirements.txt`
#### Windows
I don't really know... Maybe try Debian instructions under WSL? Just do whatever windows users do to process `requirements.txt` files. I don't use windows. *Note that it probably won't work on windows due to lack of unix permission system*.

## Usage
```
python3 -m MacAppBundler [OPTIONS] COMMAND [ARGS]
```
