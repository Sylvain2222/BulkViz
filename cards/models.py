from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    #data = models.CharField()
    slug = models.SlugField()

class Element(models.Model):
    name = models.CharField(max_length=20)
    id = models.IntegerField
    property = models.CharField(max_length=20)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

class Property(models.Model):
    name = models.CharField(max_length=20)
    id = models.IntegerField
    material = models.CharField(max_length=20)
    #data = models.CharField()
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

class Material(models.Model):
    name = models.CharField(max_length=20)
    id = models.IntegerField
    young = models.FloatField(max_length=20)
    poisson = models.FloatField(max_length=20)
    #data = models.CharField()
    card = models.ForeignKey(Card, on_delete=models.CASCADE)




