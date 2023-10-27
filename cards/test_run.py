from cards import models
from cards.get_cards import *

existing_cards = ['CQUAD4', 'CTRIA3', 'CBEAM', 'CBAR', 'PSHELL', 'PBEAM', 'PBAR', 'PCOMP', 'MAT1', 'MAT8']
# file_url = 'cards/storage/curved_plate.bdf'
file_url = 'storage/curved_plate.bdf'

d = (get_cards(existing_cards, file_url))

first_quad = models.Element(d["CQUAD4"][0]['name'], d["CQUAD4"][0]['id'], d["CQUAD4"][0]['property'])
print(first_quad.name, first_quad.id, first_quad.property)
print(len(d["CQUAD4"]))
