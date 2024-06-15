from typing import Type, Self, TypeVar
import warnings

from .. import __globals__
from ..components import component
from ..scene import Scene



class Entity:
    def __init__(self, scene : Scene | None = None, components : list[component.Component] = [], layer : int = 0, **kwargs):
        if scene == None: __globals__.__application__.active_scene.add_entity(self)
        else: scene.add_entity(self)

        self.enabled : bool = True
        self.layer : int = layer

        self.__components__ : list[component.Component] = []

        for key, value in kwargs.items():
            setattr(self, key, value)

        for comp in components:
            self.add_component(comp)

    def __awake__(self):
        for component in self.__components__:
            component.awake()

    def __update__(self):
        for component in self.__components__:
            component.update()

    def add_component(self, component : Type[component.Component], **kwargs) -> None:
        if not self.has_component(component):
            self.__components__.append(component(self, **kwargs))
        else:
            warnings.warn(f"Instance of '{type(self).__name__}' already has component '{component.__name__}'", RuntimeWarning, stacklevel=2)
    
    ComponentType = TypeVar("ComponentType")
    def get_component(self, t : Type[ComponentType]) -> ComponentType:
        for comp in self.__components__:
            if type(comp) == t:
                return comp
        
        raise AttributeError(f"Instance of '{type(self).__name__}' does not have component '{t.__name__}'")
    
    def has_component(self, component : Type[component.Component]) -> bool:
        for comp in self.__components__:
            if type(comp) == component:
                return True
        return False
    
    def remove_component(self, component : Type[component.Component]):
        if self.has_component(component):
            self.__components__.pop(self.__components__.index(self.get_component(component)))
    
    def instantiate(a : Self) -> Self:
        e = Entity()
        e.__components__ = a.__components__
        e.enabled = a.enabled
        return e
