from .asset import Asset, AssetType


class AssetManager:
    def __init__(self):
        self.__assets__ : list[Asset] = []

    def add_asset(self, name : str, path : str, atype : AssetType):
        self.__assets__.append(Asset(name, path, atype))
    
    def get_asset(self, name : str):
        ret = next((x for x in self.__assets__ if x.name == name), None)
        if not ret.loaded:
            raise RuntimeError(f"Asset '{name}' is not loaded")
        return ret

    def load_assets(self):
        for asset in self.__assets__:
            asset.load()