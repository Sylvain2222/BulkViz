from cards.models import *


def get_cards(existing_cards, file_url):
    a = []
    n: int = 8  # card format
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
                if card_type in dict:
                    dict[card_type] += [dict_line]
                else:
                    dict[card_type] = [dict_line]
    my_file.close()

    return dict


def get_cquad(a):
    cquad = Element(a[0].strip(), a[1].strip(), a[2].strip(),
                    a[3].strip() + " " + a[4].strip() + " " + a[5].strip() + " " + a[6].strip(), a[7].strip())
    return cquad


def get_ctria(a):
    ctria = Element(a[0].strip(), a[1].strip(), a[2].strip(),
                    a[3].strip() + " " + a[4].strip() + " " + a[5].strip(), a[6].strip())
    return ctria


def get_cbeam(a):
    cbeam = Element(a[0].strip(), a[1].strip(), a[2].strip(),
                    a[3].strip() + " " + a[4].strip(), a[5].strip() + " " + a[6].strip() + " " + a[7].strip())
    return cbeam


def get_cbar(a):
    cbar = Element(a[0].strip(), a[1].strip(), a[2].strip(),
                   a[3].strip() + " " + a[4].strip(), a[5].strip() + " " + a[6].strip() + " " + a[7].strip())
    return cbar


def get_pshell(a):
    pshell = Property(a[0].strip(), a[1].strip(), a[2].strip(),
                      a[3].strip() + " " + a[4].strip() + " " + a[5].strip() + " " + a[6].strip() + " " + a[7].strip())
    return pshell


def get_pbeam(a):
    pbeam = Property(a[0].strip(), a[1].strip(), a[2].strip(),
                     a[3].strip() + " " + a[4].strip() + " " + a[5].strip() + " " + a[6].strip() + " " + a[7].strip())
    return pbeam


def get_pbar(a):
    pbar = Property(a[0].strip(), a[1].strip(), a[2].strip(),
                    a[3].strip() + " " + a[4].strip() + " " + a[5].strip() + " " + a[6].strip())
    return pbar


def get_pcomp(a):
    pcomp = Property(
        a[0].strip(), a[1].strip(), a[2].strip(),
        a[3].strip() + " " + a[4].strip() + " " + a[5].strip() + " " + a[6].strip() + " " + a[7].strip() + " " + a[
            8].strip() + " " + a[9].strip())
    return pcomp


def get_mat1(a):
    try:
        mat1 = Material(
            a[0].strip(), a[1].strip(), a[2].strip() + " " + a[3].strip() + " " + a[4].strip() + " " + a[
                5].strip() + " " + a[6].strip() + " " + a[7].strip() + " " + a[8].strip())
    except:
        mat1 = Material(
            a[0].strip(), a[1].strip(), a[2].strip() + " " + a[3].strip() + " " + a[4].strip())
        pass
    return mat1


def get_mat8(a):
    mat8 = Material(
        a[0].strip(), a[1].strip(), a[2].strip() + " " + a[3].strip() + " " + a[4].strip() + " " + a[
            5].strip() + " " + a[6].strip() + " " + a[7].strip() + " " + a[8].strip())
    return mat8
