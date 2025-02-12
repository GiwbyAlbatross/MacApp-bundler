from typing import Union
import os, pathlib

def getentrypoint(cwd: typing.Union[str, bytes, os.PathLike],
                  flags: Union[tuple[str], list[str]]=tuple()) -> str:
    "Write entrypoint code to put in App.app/Contents/MacOS/"
    if isinstance(cwd, bytes):
        path = cwd.decode()
    else:
        path = str(cwd)
    basic = """#!/usr/bin/env python3
from sys import argv, flags, executable
from pathlib import Path
from os import getcwd, chdir, system

path = Path(__file__).absolute()
os.chdir(path.parents[1])"""
    #
