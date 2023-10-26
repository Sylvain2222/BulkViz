# Declarations

def get_cards(new_card):
    stop_count = False
    a = []
    n: int = 8  # card format

    my_file = open('storage/curved_plate.bdf', 'r')
    my_line = my_file.readline()
    while my_line:
        my_line = my_file.readline()
        # count cards
        if my_line.startswith(new_card.name):
            new_card.count += 1
        # get first card
        # use endwith("+") for multi lines
        if my_line.startswith(new_card.name) and stop_count == False:
            a = ([(my_line[j:j + n]) for j in range(0, len(my_line), n)])
            new_card.name = a[0].strip()
            new_card.id = a[1].strip()
            new_card.property = a[2].strip()
            stop_count = True
    my_file.close()


#func