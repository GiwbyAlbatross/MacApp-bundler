# this file is intentionally left blank, for now
import MacAppBundler.bundlestructure as _structure
import MacAppBundler.entrypoint as _entrypoint
import MacAppBundler.plist as _plist

Pathish = _structure.Pathish

def mkapp(name: str,
          script: Pathish,
          assetfolder: Pathish,
          cwd: Pathish='../',
          dir: Pathish='.',
          *,
          plistData: dict = {}):
    """mkapp: generates the app bundle structure, 100% ready to go
    name: name of the app
    script: path to executable the app triggers
    assetfolder: path to asset folder to package in the bundle
    cwd: relative path (from asset folder in the app) that the script should be from run from
    dir: relative path (from the cwd this function was run in)
    *
    plistData: extra plist data (a dict)"""
    raise NotImplementedError("This is not implemented. The docstring is there, but there's no code.")
    return NotImplemented