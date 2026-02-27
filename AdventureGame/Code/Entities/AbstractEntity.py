from abc import ABC, abstractmethod

#AbstractEntity
class AbstractEntity(ABC):
    @abstractmethod
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def get_name(self):
        return self.name
    
    def get_health(self):
        return self.health

    def set_name(self, name):
        self.name = name
        
    def set_health(self, health):
        self.health = health
        