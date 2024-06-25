from .asset import Asset, AssetType
from . import asset_dumper
from typing import Self
import warnings


class AssetManager:
    def __init__(self):
        self.__assets__ : list[Asset] = []

    def add_asset(self, asset : Asset):
        self.__assets__.append(asset)

    def add(self, name : str, path : str, atype : AssetType):
        self.__assets__.append(Asset(name, path, atype))
    
    def get_asset(self, name : str):
        ret = next((x for x in self.__assets__ if x.name == name), None)
        if ret == None: 
            warnings.warn(f"Could not find asset {name}", UserWarning, 2)
            ret = Asset.null
        if not ret.loaded:
            raise RuntimeError(f"Asset '{name}' is not loaded")
        
        return ret

    def load_assets(self):
        for asset in self.__assets__:
            asset.load()

    def dump_asset_pack(self, filename : str) -> None:
        with open(filename, "wb") as f:
            asset_dumper.dump(self, f)
    
    @classmethod
    def load_asset_pack(cls, filename : str):
        with open(filename, "rb") as f:
            return asset_dumper.load(f, AssetManager)