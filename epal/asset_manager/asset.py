from enum import Enum
import pygame



class AssetType(Enum):
    Image = 0
    Audio = 1

class Asset:
    def __init__(self, name : str, path : str, asset_type : AssetType):
        self.name = name
        self.path = path
        self.asset_type = asset_type
        self.__asset__ = None
        self.loaded = False

    def load(self):
        if self.asset_type == AssetType.Image:
            self.__asset__ = pygame.image.load(self.path)
        if self.asset_type == AssetType.Audio:
            self.__asset__ = pygame.mixer.Sound(self.path)
        
        self.loaded = True

    def get(self):
        return self.__asset__