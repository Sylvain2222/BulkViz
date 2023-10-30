from cards.models import *  # for run in python console


# from models import * # for test


# Function to collect all wanted cards from the bulk in a dictionary
def get_cards(existing_cards, file_url):
    a = []  # array for line split
    n: int = 8  # nastran card format
    dict = {}  # dictionary for the bulk

    my_file = open(file_url, 'r')  # bulk file to read
    my_line = my_file.readline()

    # Loop to read all lines of the bulk
    while my_line:
        my_line = my_file.readline()
        for card_type in existing_cards:
            dict_line = {}  # Dictionary containing the cards as objects
            if my_line.startswith(card_type):
                # split the line for each cell of the card
                # To improve for multi lines cards with endwith('+')
                a = ([(my_line[x:x + n]) for x in range(0, len(my_line), n)])
                # attribute all values in objects
                dict_line["name"] = a[0].strip()
                dict_line["id"] = a[1].strip()
                match card_type:
                    case "CQUAD4":
                        dict_line = get_cquad(a)
                    case "CTRIA3":
                        dict_line = get_ctria(a)
                    case "CBEAM":
                        dict_line = get_cbeam(a)
                    case "CBAR":
                        dict_line = get_cbar(a)
                    case "PSHELL":
                        dict_line = get_pshell(a)
                    case "PBEAM":
                        dict_line = get_pbeam(a)
                    case "PBAR":
                        dict_line = get_pbar(a)
                    case "PCOMP":
                        dict_line = get_pcomp(a)
                    case "MAT1":
                        dict_line = get_mat1(a)
                    case "MAT8":
                        dict_line = get_mat8(a)
                # adding card objects in the dictionary
                if card_type in dict:
                    dict[card_type] += [dict_line]
                else:
                    dict[card_type] = [dict_line]
    my_file.close()

    return dict


# Functions for different types of cards - return card object

def get_cquad(a):
    cquad = Element(a[0].strip(), a[1].strip(), a[2].strip(),
                    a[3].strip() + " " + a[4].strip() + " " +
                    a[5].strip() + " " + a[6].strip(), a[7].strip())
    return cquad


def get_ctria(a):
    ctria = Element(a[0].strip(), a[1].strip(), a[2].strip(),
                    a[3].strip() + " " + a[4].strip() + " " +
                    a[5].strip(), a[6].strip())
    return ctria


def get_cbeam(a):
    cbeam = Element(a[0].strip(), a[1].strip(), a[2].strip(),
                    a[3].strip() + " " + a[4].strip(), a[5].strip() + " " +
                    a[6].strip() + " " + a[7].strip())
    return cbeam


def get_cbar(a):
    cbar = Element(a[0].strip(), a[1].strip(), a[2].strip(),
                   a[3].strip() + " " + a[4].strip(),
                   a[5].strip() + " " + a[6].strip() + " " + a[7].strip())
    return cbar


def get_pshell(a):
    data = ""
    pshell = Property(a[0].strip(), a[1].strip(), a[2].strip(), data)
    for x in range(3, len(a)):
        data += a[x].strip() + " "
        x += 1
    pshell.data = data
    return pshell


def get_pbeam(a):
    data = ""
    pbeam = Property(a[0].strip(), a[1].strip(), a[2].strip(), data)
    for x in range(3, len(a)):
        data += a[x].strip() + " "
        x += 1
    pbeam.data = data
    return pbeam


def get_pbar(a):
    data = ""
    pbar = Property(a[0].strip(), a[1].strip(), a[2].strip(), data)
    for x in range(3, len(a)):
        data += a[x].strip() + " "
        x += 1
    pbar.data = data
    return pbar


def get_pcomp(a):
    data = ""
    pcomp = Property(a[0].strip(), a[1].strip(), a[2].strip(), data)
    for x in range(3, len(a)):
        data += a[x].strip() + " "
        x += 1
    pcomp.data = data
    return pcomp


def get_mat1(a):
    data = ""
    mat1 = Material(a[0].strip(), a[1].strip(), data)
    for x in range(2, len(a)):
        data += a[x].strip() + " "
    mat1.data = data
    return mat1


def get_mat8(a):
    data = ""
    mat8 = Material(a[0].strip(), a[1].strip(), data)
    for x in range(2, len(a)):
        data += a[x].strip() + " "
    mat8.data = data
    return mat8
