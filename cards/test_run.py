import models
from get_cards import *

cquad4 = models.Element("CQUAD4")
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
existing_elements = ["CQUAD4", "CTRIA3", "CBEAM", "CBAR"]
existing_properties = ["PSHELL", "PBEAM", "PBAR", "PCOMP"]
existing_materials = ["MAT1", "MAT8"]

print("*****************")
for i in existing_elements:
    j = models.Element(i)
    get_cards(j)
    print(j.name, ": ", j.count, "elements")
    print("first id:", j.id)
    print("first property:", j.property)
    print("******************")
