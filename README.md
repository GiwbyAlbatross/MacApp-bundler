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

## but the app doesn't run
By default MacOS doesn't trust arbitrary executables or .app files. You need to right-click (or cntrl-click) the .app and select open.
This should be the same as double-clicking a normal app, but it forces MacOS to trust the executable for the rest of eternity (on your computer.

It could also be that you didn't create the app on a UNIX filesystem. MacOS uses UNIX permissions to identify executables, so on a filesystem that lacks such UNIX permissions, MacOS can't open the app.

###### if there is an error message with an app from this tool, please add an issue to the repo. I want to know about it
Try running the app in the terminal with `open <YourAppName.app>` and `/path/to/app/YourAppName.app/Contents/MacOS/yourappnamelowercase` and see if either of them. 
