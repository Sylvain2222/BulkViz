from cards import models
from cards.get_cards import *

existing_cards = ['CQUAD4', 'CTRIA3', 'CBEAM', 'CBAR', 'PSHELL', 'PBEAM', 'PBAR', 'PCOMP', 'MAT1', 'MAT8']
file_url = 'cards/storage/curved_plate.bdf'  # for server
# file_url = 'storage/curved_plate.bdf'  # for IDE run

dict_bulk = (get_cards(existing_cards, file_url))

first_cards = {}
for card in existing_cards:
    first_cards[card] = dict_bulk[card][0]
    # print(first_cards[card])
    # print("Nombre de ",card,":",len(dict_bulk[card]))
