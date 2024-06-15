from .component import Component
from .transform import Transform

from .. import __globals__
from ..entity.color import Color
from .. import application
from .. import Asset

import pygame


class Rect(Component):
    def __init__(self, parent):
        super().__init__(parent)

        self.require_component(Transform)
        self.color : Color = Color(0, 0, 0)
    
    def update(self):
        transform = self.parent.get_component(Transform)
        position = transform.position.as_tuple()
        size = transform.scale.as_tuple()
        pygame.draw.rect(application.Application.get_window().__window__, self.color.as_tuple(),
                         pygame.Rect(position[0], position[1], size[0], size[1]))
        
class Circle(Component):
    def __init__(self, parent):
        super().__init__(parent)

        self.require_component(Transform)
        self.color : Color = Color(0, 0, 0)

    def update(self):
        transform = self.parent.get_component(Transform)
        position = transform.position.as_tuple()
        size = transform.scale.as_tuple()

        pygame.draw.circle(application.Application.get_window().__window__, self.color.as_tuple(),
                           position, size[0])
        
class Ellipse(Component):
    def __init__(self, parent):
        super().__init__(parent)

        self.require_component(Transform)
        self.color : Color = Color(0, 0, 0)

    def update(self):
        transform = self.parent.get_component(Transform)
        position = transform.position.as_tuple()
        scale = transform.scale.as_tuple()

        pygame.draw.ellipse(application.Application.get_window().__window__, self.color.as_tuple(),
                             pygame.Rect(position[0], position[1], scale[0], scale[1]))
        
class Image(Component):
    def __init__(self, parent, asset : Asset | str | None = None):
        super().__init__(parent)

        self.require_component(Transform)
        self.asset = asset
        self.image = None

    def awake(self):
        if self.asset == None:
            raise AttributeError("No image path supplied")
        if type(self.asset) == str:
            self.image = pygame.image.load(self.path)
        if type(self.asset) == Asset:
            self.image = self.asset.get()
    
    def update(self):
        transform = self.parent.get_component(Transform)
        position = transform.position.as_tuple()

        rect = self.image.get_rect()
        rect.topleft = position

        application.Application.get_window().__window__.blit(self.image, rect)