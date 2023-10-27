from django.db import models


# Create your models here.
class Card:
    # name: ""
    # id = 0
    count = 0

    def __init__(self, name,id):
        self.name = name
        self.id = id

    # def toDict(self):
    #     return {'name': self.name, 'id': self.id}


class Element(Card):
    # property = ""
    def __init__(self, name, id,property):
        # self.name = name
        # self.id = id
        super().__init__(name, id)
        self.property = property

    # def toDict(self):
    #     return {'name': self.name, 'id': self.id, 'property': self.property}


class Property(Card):
    # material = 0
    def __init__(self, name, id, material):
        super().__init__(name, id)
        self.material = material


class Material(Card):
    # young_modulus = 0
    def __init__(self, name, id, young_modulus):
        super().__init__(name, id)
        self.young_modulus = young_modulus


# class Card(models.Model):
#     def __init__(self,name,id,slug):
#         self.name = models.CharField(max_length=16)
#         self.id = models.CharField(max_length=16)
#         self.slug = models.SlugField()

# class Element(Card):
#     property = models.CharField(max_length=16)
#     card = models.ForeignKey(Card, on_delete=models.CASCADE)
#     # Element.__init__(self,name,id,slug)
#
# class Property(Card):
#     material = models.CharField(max_length=16)
#     card = models.ForeignKey(Card, on_delete=models.CASCADE)
#
# class Material(Card):
#     young = models.FloatField(max_length=16)
#     poisson = models.FloatField(max_length=16)
#     card = models.ForeignKey(Card, on_delete=models.CASCADE)
