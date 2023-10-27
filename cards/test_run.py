import models
from get_cards import *

# cquad4 = models.Element("CQUAD4")
# get_cards(cquad4)
# print(cquad4.name, ": ", cquad4.count, "elements")
# print("first id:", cquad4.id)
# print("first property:",cquad4.property)
# #
# ctria3 = models.Element("CTRIA3")
# get_cards(ctria3)
# print(ctria3.name, ": ", ctria3.count, "elements")
# print("first id:", ctria3.id)
# print("first property:",ctria3.property)
#
# cbar = models.Element("CBAR")
# get_cards(cbar)
# print(cbar.name, ": ", cbar.count, "elements")
# print("ctria3:", cbar.id)
# print("first property:",cbar.property)
#
# cbeam = models.Element("CBEAM")
# get_cards(cbeam)
# print(cbeam.name, ": ", cbeam.count, "elements")
# print("first id:", cbeam.id)
# print("first property:",cbeam.property)
#
# existing_elements = ["CQUAD4", "CTRIA3", "CBEAM", "CBAR"]
# existing_properties = ["PSHELL", "PBEAM", "PBAR", "PCOMP"]
# existing_materials = ["MAT1", "MAT8"]
existing_cards = ['CQUAD4', 'CTRIA3', 'CBEAM', 'CBAR', 'PSHELL', 'PBEAM', 'PBAR', 'PCOMP', 'MAT1', 'MAT8']
file_url = 'storage/curved_plate.bdf'
#
# print("*****************")
# for i in existing_cards:
#     j = models.Element(i)
#     # print(get_cards(j))
#     d = get_cards(j)
#     print(d)

# get_cards(j)
# print(j.name, ": ", j.count, "elements")
# print("first id:", j.id)
# print("first property:", j.property)
# print("******************")

# print(d[0])


# print("*****************")
# get_cards(existing_cards)

# test dictionnaires
# x = {}
# j = 10
# for i in range(0, 10):
#     x["TEST",i] = i
#     xx = {}
#     xx["name"] = j
#     x[i] = xx
#     j += 1
# print(x)


cquad4 = get_cards(existing_cards, file_url)
print(cquad4)
print(cquad4['CQUAD4', 273]['name'])
print(cquad4['CQUAD4', 273]['id'])
print(cquad4['CQUAD4', 273]['property'])
