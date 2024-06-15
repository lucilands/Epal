from enum import Enum
from typing import Self
import pygame
import pathlib



class AssetType(Enum):
    Image = 0
    Audio = 1

class Asset:
    def __init__(self, name : str, path : str = pathlib.Path(__file__).parent.resolve().__str__()+"/null_asset.png", asset_type : AssetType = AssetType.Image):
        self.name = name
        if path != None:
            self.path = path
            self.asset_type = asset_type
        else:
            path = pathlib.Path(__file__).parent.resolve().__str__()+"/null_asset.png"
            self.asset_type = AssetType.Image

        self.__asset__ = None
        self.loaded = False

    def load(self):
        if self.asset_type == AssetType.Image:
            self.__asset__ = pygame.image.load(self.path).convert()
        if self.asset_type == AssetType.Audio:
            self.__asset__ = pygame.mixer.Sound(self.path)
        
        self.loaded = True

    null : Self

    def get(self):
        if not self.loaded:
            raise RuntimeError(f"Asset {self.name} is not loaded")
        return self.__asset__
    
    def resize(self, new_size : tuple[int, int]):
        self.__asset__ = pygame.transform.scale(self.get(), new_size)