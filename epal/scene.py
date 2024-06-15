from . import __globals__



class Scene:
    def __init__(self):
        self.__entities__ = []
        self.__uuid__ : int

        __globals__.__application__.add_scene(self)
    
    def __awake__(self):
        self.__entities__.sort(key = lambda x: x.layer)
        for entity in self.__entities__:
            entity.__awake__()

    def __update__(self):
        self.__entities__.sort(key = lambda x: x.layer)
        for entity in self.__entities__:
            if entity.enabled: entity.__update__()
    
    def add_entity(self, entity):
        self.__entities__.append(entity)
    
    def get_uuid(self):
        return self.__uuid__
    
    def get_all_entities(self):
        return self.__entities__