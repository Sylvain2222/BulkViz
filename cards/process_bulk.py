import models

# Declarations
first_quad4: str = ""  # to remove
count_quad4: int = 0
count_card: int = 0
count_line: int = 0
start_line: int = 0
tab = []
n: int = 8  # card format
a = []
# List of cards to check
# ----to improve
existing_cards = ["CQUAD4", "CTRIA3", "CBAR", "CBEAM",
                  "PSHELL", "PBEAM", "PBAR", "PCOMP",
                  "MAT1", "MAT8",
                  "DUMMY"]

# count cards
# Open bulk file as read
# my_file = open('storage/curved_plate.bdf', 'r')
# my_line = my_file.readline()
# while my_line:
#     my_line = my_file.readline()
#     for i in existing_cards:
#         if my_line.startswith(i):
#             print(my_line)
#             print("****** i = ",i)
#             count_quad4 += 1
#             print("******count_quad4 = ",count_quad4)
#
#     # if my_line.startswith("CQUAD4"):
#     #     count_quad4 += 1
#
# my_file.close()


# get cards
my_file = open('storage/curved_plate.bdf', 'r')
my_line = my_file.readline()
while my_line:
    my_line = my_file.readline()
    # get first card in array
    # use endwith("+") for multi lines
    for i in existing_cards:
        if my_line.startswith(i):
            tab.append(my_line)
            existing_cards.remove(i)
my_file.close()

# print("CQUAD4:", count_quad4, "elements")
# print(first_quad4)
# for i in range(0,10):
#     print(tab[i])

# print([(tab[1][i:i + n]) for i in range(0, len(tab[1]), n)])
# print(a)

x = models.Card()

for j in range(0, 10):
    a = ([(tab[j][i:i + n]) for i in range(0, len(tab[j]), n)])

    x.name = a[0].strip()
    x.id = a[1].strip()
    # print(a)
# print("Card name:",x.name)
# print("Card id:",x.id)


# x = models.Card()
# for j in range(0, 10):
#     a = ([(tab[j][i:i + n]) for i in range(0, len(tab[j]), n)])
#     x.name = a[0].strip()
#     x.id = a[1].strip()
#     # print(a)
# print("Card name:", x.name)
# print("Card id:", x.id)