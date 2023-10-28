from django.db import models


# Create your models here.
class Card:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    # def toDict(self):
    #     return {'name': self.name, 'id': self.id}


class Element(Card):
    def __init__(self, name, id, property, grids, orientation):
        super().__init__(name, id)
        self.property = property
        self.grids = grids
        self.orientation = orientation


class Property(Card):
    def __init__(self, name, id, material):
        super().__init__(name, id)
        self.material = material

    data = ''


class Material(Card):
    def __init__(self, name, id, data):
        super().__init__(name, id)
        self.data = data


# class Test(Card):
#     def __init__(self, name, id, lacarte):
#         super().__init__(name, id)
#         # self.lacarte = lacarte
#
#     name = lacarte['name']
#     id = lacarte['id']
#     property = lacarte['property']
#     grids = lacarte['grids']
#     orientation = lacarte['orientation']

