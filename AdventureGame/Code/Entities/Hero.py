from Entities.AbstractEntity import AbstractEntity

# Hero
class Hero(AbstractEntity):
    def __init__(self, name, health):
        super().__init__(name, health)

