import plistlib
import os
from typing import Union

Pathish = Union[str, os.PathLike]

defaultdata = {
    'CFBundlePackageType':'AAPL',
    'CFBundleSignature':'????'
}

def load(filename: Pathish) -> dict:
    "load data from filename"
    with open(filename) as f:
        r = plistlib.loads(f.read())
    return r
def writeto(filename: Pathish, data: Union[dict, bytes, str]) -> int:
    "write data to filename and return the number of bytes written"
    if isinstance(data, dict):
        d = plistlib.dumps(data)
    elif isinstance(data, str):
        d = data.encode()
    else:
        d = data
    with open(filename, 'wb') as f:
        f.write(d)
    return len(d)

def getdefaultplist(appname: str,
                    bundleIdentifier: str,
                    bundleVersion: str='0.0.0',
                    minimumMacOSversion: str='10.4.8') -> bytes:
    d = defaultdata.copy()
    d['CFBundleName'] = appname
    d['CFBundleDisplayName'] = appname
    d['CFBundleIdentifier'] = bundleIdentifier
    d['CFBundleVersion'] = bundleVersion
    d['CFBundleExecutable'] = appname.lower()
    d['CFBundleGetVersionString'] = ' '.join([appname, bundleVersion])
    d['LSMinimumSystemVersion'] = minimumMacOSversion
    return plistlib.dumps(d)
 