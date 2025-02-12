from typing import Union
import os, pathlib

pathish = Union[str, os.PathLike]

def getentrypoint(cwd: Union[str, bytes, os.PathLike],
                  assetfolder: pathish=None,
                  executable: pathish=...,
                  flags: Union[tuple[str], list[str]]=tuple()) -> str:
    """Write entrypoint code to put in App.app/Contents/MacOS/
    cwd: cwd relative to assetfolder
    assetfolder: name of assetfolder (not used?)
    executable: path of executable, relative to assetfolder
    flags: list of flags to pass to python interpreter"""

    basic = """#!/usr/bin/env python3
from sys import argv, flags, executable
from pathlib import Path
from os import getcwd, chdir, system
import os.path as path

path = Path(__file__).absolute()
os.chdir(str(path.parents[2]))
os.chdir(path.join('Resources', {assetfolder}))
assetfolder = Path(os.getcwd())
os.chdir('{cwd}')

executable = assetfolder / '{executable}'

system(executable + ' '.join({flags}) + str(executable))
"""
    return basic.format(cwd=str(cwd),
                        assetfolder=str(assetfolder),
                        executable=str(executable),
                        flags=repr(flags))
