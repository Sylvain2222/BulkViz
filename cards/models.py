from django.db import models


# Create your models here.
class Card:
    count = 0
    id = 0

    def __init__(self, name):
        self.name = name

    # def toDict(self):
    #     return {'name': self.name, 'id': self.id, 'count': self.count}


class Element(Card):
    property = 0

    # def func_element(self, name):
    #     # count = 0
    #     # Element.count = 0
    #     stop_count = False
    #     n = 8
    #
    #     #  get element card data
    #     my_file = open('storage/curved_plate.bdf', 'r')
    #     my_line = my_file.readline()
    #     while my_line:
    #         my_line = my_file.readline()
    #         # count cards
    #         if my_line.startswith(name):
    #             self.count += 1
    #         # get first card in array
    #         # use endwith("+") for multi lines
    #         if my_line.startswith(name) and stop_count == 0:
    #             a = ([(my_line[j:j + n]) for j in range(0, len(my_line), n)])
    #             print(a)
    #             name = a[0].strip()
    #             id = a[1].strip()
    #             property = a[2].strip()
    #             stop_count = True
    #     my_file.close()


class Property(Card):
    material = 0


class Material(Card):
    young_modulus = 0




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
