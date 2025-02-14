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
                    minimumMacOSversion: str='10.4.8',
                    *,
                    bundleSignature: str='????',
                    binary: bool=False,
                    _defaultdata: dict = defaultdata) -> bytes:
    d = _defaultdata.copy()
    d['CFBundleName'] = appname
    d['CFBundleDisplayName'] = appname
    d['CFBundleIdentifier'] = bundleIdentifier
    d['CFBundleVersion'] = bundleVersion
    d['CFBundleExecutable'] = appname.lower()
    d['CFBundleGetVersionString'] = ' '.join([appname, bundleVersion])
    d['LSMinimumSystemVersion'] = minimumMacOSversion
    d['CFBundleSignature'] = bundleSignature
    return plistlib.dumps(d, fmt=(plistlib.FMT_BINARY if do_binary else plistlib.FMT_XML))

class BundleDocumentType:
    extensions: list[str]
    name: str
    iconFile: str
    role: str
    def __init__(self,
                 extensions: list[str],
                 name: str,
                 iconFile: str,
                 role: str='Editor') -> None:
        self.extensions = extensions
        self.iconFile = iconFile
        self.role = role
        self.name = name
    @property
    def dict(self) -> dict:
        return {
            'CFBundleTypeExtensions':self.extensions,
            'CFBundleTypeName':self.name,
            'CFBundleTypeIconFile':self.iconFile,
            'CFBundleTypeRole':self.role
        }

class BundleDocumentTypes:
    doctype_objs: list[BundleDocumentType]
    @property
    def dict(self) -> dict[str, list[dict]]:
        return {'CFBundleDocumentTypes':self.doctypes}
    @property
    def doctypes(self) -> list[dict]:
        return [doctype.dict for doctype in self.doctype_objs]
