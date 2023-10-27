def get_cards(existing_cards, file_url):
    a = []
    n: int = 8  # card format
    i = 0
    dict = {}

    my_file = open(file_url, 'r')
    my_line = my_file.readline()

    while my_line:
        my_line = my_file.readline()
        for card_type in existing_cards:
            dict_line = {}
            if my_line.startswith(card_type):
                a = ([(my_line[x:x + n]) for x in range(0, len(my_line), n)])
                dict_line["name"] = a[0].strip()
                dict_line["id"] = a[1].strip()
                dict_line["property"] = a[2].strip()
                switch:
                if card_type in dict:
                    dict[card_type] += [dict_line]
                else:
                    dict[card_type] = [dict_line]
    my_file.close()

    return dict
