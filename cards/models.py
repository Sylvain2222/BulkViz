from django.db import models


# Create your models here.
class Card:

    def __init__(self, name, id):
        self.name = name
        self.id = id


class Element(Card):
    def __init__(self, name, id, property, grids, orientation):
        super().__init__(name, id)
        self.property = property
        self.grids = grids
        self.orientation = orientation


class Property(Card):
    def __init__(self, name, id, material,data):
        super().__init__(name, id)
        self.material = material
        self.data = data


class Material(Card):
    def __init__(self, name, id, data):
        super().__init__(name, id)
        self.data = data


