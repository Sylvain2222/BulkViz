from cards import models
from cards.get_cards import *

existing_cards = ['CQUAD4', 'CTRIA3', 'CBEAM', 'CBAR', 'PSHELL', 'PBEAM', 'PBAR', 'PCOMP', 'MAT1', 'MAT8']
file_url = 'cards/storage/curved_plate.bdf'  # for server
# file_url = 'storage/curved_plate.bdf'  # for IDE run
#
d = (get_cards(existing_cards, file_url))
# d = (get_cards(existing_cards, file_url))
# d = (get_cards(existing_cards, file_url))
# d = (get_cards(existing_cards, file_url))
# d = (get_cards(existing_cards, file_url))
# d = (get_cards(existing_cards, file_url))
# d = (get_cards(existing_cards, file_url))
# d = (get_cards(existing_cards, file_url))

# first_quad = models.Element(d["CQUAD4"][0]['name'], d["CQUAD4"][0]['id'], d["CQUAD4"][0]['property'],
#                             d["CQUAD4"][0]['grids'], d["CQUAD4"][0]['orientation'])
# print(first_quad.name, first_quad.id, first_quad.property, first_quad.grids, first_quad.orientation)
# print(len(d["CQUAD4"]))
# print("***********")
#
# first_pshell = models.Property(d["PSHELL"][0]['name'], d["PSHELL"][0]['id'], d["PSHELL"][0]['material'])
# print(first_pshell.name, first_pshell.id, first_pshell.material)
# print(len(d["PSHELL"]))
# print("***********")
#
# first_mat1 = models.Material(d["MAT1"][0]['name'], d["MAT1"][0]['id'], d["MAT1"][0]['data'])
# print(first_mat1.name, first_mat1.id, first_mat1.data)
# print(len(d["MAT1"]))
# print("***********")
#
# first_mat8 = models.Material(d["MAT8"][0]['name'], d["MAT8"][0]['id'], d["MAT8"][0]['data'])
# print(first_mat8.name, first_mat8.id, first_mat8.data)
# print(len(d["MAT8"]))
# print("***********")
#
# print(d["CQUAD4"][0].items())
first_cards = {}
# first_cards["CQUAD4"]= d["CQUAD4"][0]
# first_cards["CTRIA3"]= d["CTRIA3"][0]
# print(first_cards["CQUAD4"].__dict__)
# print(first_cards["CTRIA3"])

for card in existing_cards:
    first_cards[card] = d[card][0]
    print(first_cards[card])
    print("Nombre de ",card,":",len(d[card]))


letest = "le test"