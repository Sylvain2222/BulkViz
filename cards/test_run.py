import models
from get_cards import *

existing_cards = ['CQUAD4', 'CTRIA3', 'CBEAM', 'CBAR', 'PSHELL', 'PBEAM', 'PBAR', 'PCOMP', 'MAT1', 'MAT8']
file_url = 'storage/curved_plate.bdf'

# print(get_cards(existing_cards, file_url))

d = (get_cards(existing_cards, file_url))
print("---------------TEST CLASS-----------")
cquad4 = models.Element
cquad4.name = d["CQUAD4"][0]['name']
cquad4.id = d["CQUAD4"][0]['id']
cquad4.property = d["CQUAD4"][0]['property']
print(cquad4.name, ": id=", cquad4.id, ", Property=", cquad4.property)

ctria3 = models.Element
ctria3.name = d["CTRIA3"][0]['name']
ctria3.id = d["CTRIA3"][0]['id']
ctria3.property = d["CTRIA3"][0]['property']
print(ctria3.name, ": id=", ctria3.id, ", Property=", ctria3.property)
