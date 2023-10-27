from cards import models
from cards.get_cards import *

existing_cards = ['CQUAD4', 'CTRIA3', 'CBEAM', 'CBAR', 'PSHELL', 'PBEAM', 'PBAR', 'PCOMP', 'MAT1', 'MAT8']
# file_url = 'cards/storage/curved_plate.bdf'
file_url = 'storage/curved_plate.bdf'

d = (get_cards(existing_cards, file_url))

first_quad = models.Element(d["CQUAD4"][0]['name'], d["CQUAD4"][0]['id'], d["CQUAD4"][0]['property'],d["CQUAD4"][0]['grids'],d["CQUAD4"][0]['orientation'])
print(first_quad.name, first_quad.id, first_quad.property,first_quad.grids,first_quad.orientation)
print(len(d["CQUAD4"]))
print("***********")

first_pshell = models.Property(d["PSHELL"][0]['name'], d["PSHELL"][0]['id'], d["PSHELL"][0]['material'])
print(first_pshell.name, first_pshell.id, first_pshell.material)
print(len(d["PSHELL"]))
print("***********")
print(d)

first_mat1 = models.Material(d["MAT1"][0]['name'], d["MAT1"][0]['id'], d["MAT1"][0]['E'])
print(first_mat1.name, first_mat1.id, first_mat1.E)
print(len(d["MAT1"]))
print("***********")
print(d)