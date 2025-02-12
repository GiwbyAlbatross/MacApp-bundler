"functions for creating bundle file structures"

import os
import os.path as path
import pathlib
import stat
from typing import Union

pathish = Union[str, os.PathLike]

def makebundle(bundlename: str,
               dir: pathish = '.',
               executableName: str=None,
               subdirs: set=set()) -> str:
    "create the bundle file structure and return its file location"
    if not bundlename.endswith('.app'):
        bundlename += '.app'
    
    if excecutableName is None:
        executableName = bundlename[:-4]

    bundlelocation = path.join(dir, bundlename)
    contentslocation = path.join(dir, bundlename, 'Contents/')
    subdirs.add('MacOS')
    subdirs.add('Resources')

    os.mkdir(bundlelocation)
    os.mkdir(contentslocation)
    
    for subdir in subdirs:
        os.mkdir(path.join(contentslocation, subdir))
    
    with open(path.join(contentslocation, 'Info.plist'), 'x') as f:
        pass
    with open(path.join(contentslocation, 'MacOS', executableName), 'x') as f:
        pass
    os.chmod(path.join(contentslocation, 'MacOS', executableName),
             stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    
    return bundlelocation

