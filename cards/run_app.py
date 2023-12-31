from cards.get_cards import *  # for run in python console

# from get_cards import * # for test

# Input of wanted cards
existing_cards = ['CQUAD4', 'CTRIA3', 'CBEAM', 'CBAR', 'PSHELL', 'PBEAM', 'PBAR', 'PCOMP', 'MAT1', 'MAT8']
# Input URL file location
file_url = 'cards/storage/curved_plate.bdf'  # for server
# file_url = 'storage/curved_plate.bdf'  # for IDE run

# Create dictionary containing the bulk
dict_bulk = (get_cards(existing_cards, file_url))

# Create dictionary containing first cards of each type as objects
# first_cards = {}
# for card in existing_cards:
#     try:
#         first_cards[card] = dict_bulk[card][0]
#         print(first_cards[card].__dict__)
#         print("Nombre de ", card, ":", len(dict_bulk[card]))
#     except:
#         print("Pas de", card, "dans le bulk")
