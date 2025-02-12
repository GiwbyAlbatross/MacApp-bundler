"functions for creating bundle file structures"

import os
import os.path as path
import pathlib
from typing import Union

pathish = Union[str, os.PathLike]

def makebundle(bundlename: pathish, dir: pathish = '.') -> None:
    pass