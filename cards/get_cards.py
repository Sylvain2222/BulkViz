# fonction sans dictionnaires
# def get_cards(new_card):
#     stop_count = False
#     a = []
#     n: int = 8  # card format
# #     my_file = open('storage/curved_plate.bdf', 'r')
#     my_line = my_file.readline()
#     while my_line:
#         my_line = my_file.readline()
#         # count cards
#         if my_line.startswith(new_card.name):
#             new_card.count += 1
#         # get first card
#         # use endwith("+") for multi lines
#         if my_line.startswith(new_card.name) and stop_count == False:
#             a = ([(my_line[j:j + n]) for j in range(0, len(my_line), n)])
#             new_card.name = a[0].strip()
#             new_card.id = a[1].strip()
#             new_card.property = a[2].strip()
#             stop_count = True
#     my_file.close()

# fonction avec dictionnaires - cquad4 en argument de la fonction - renvoie qu'une seule ligne
# def get_cards(new_card):
#     a = []
#     n: int = 8  # card format
#     i = 0
#     dict = {}
#
#     my_file = open('storage/curved_plate.bdf', 'r')
#     my_line = my_file.readline()
#     while my_line:
#         dict_line = {}
#         my_line = my_file.readline()
#         # get first card
#         # use endwith("+") for multi lines
#         if my_line.startswith(new_card.name):
#             a = ([(my_line[j:j + n]) for j in range(0, len(my_line), n)])
#             dict[i] = i
#             dict_line["name"] = a[0].strip()
#             dict_line["id"] = a[1].strip()
#             dict_line["property"] = a[2].strip()
#             dict[i] = dict_line
#             i += 1
#
#             new_card.count += 1
#             new_card.name = a[0].strip()
#             new_card.id = a[1].strip()
#             new_card.property = a[2].strip()
#
#     my_file.close()
#     return dict


def get_cards(existing_cards, file_url):
    a = []
    n: int = 8  # card format
    i = 0
    dict = {}

    my_file = open(file_url, 'r')  # TBD: URL as argument
    my_line = my_file.readline()

    while my_line:
        my_line = my_file.readline()
        for card_type in existing_cards:
            dict_line = {}
            if my_line.startswith(card_type):
                i += 1
                a = ([(my_line[x:x + n]) for x in range(0, len(my_line), n)])
                dict_line["name"] = a[0].strip()
                dict_line["id"] = a[1].strip()
                dict_line["property"] = a[2].strip()
                # dict[card, i] = dict_line
                if card_type in dict:
                    dict[card_type] += [dict_line]
                else:
                    dict[card_type] = [dict_line]
    my_file.close()

    return dict
