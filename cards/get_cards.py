from cards.models import *
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
                match card_type:
                    case "CQUAD4":
                        dict_line = get_cquad(a)
                    case "CTRIA3":
                        dict_line = get_ctria(a, dict_line)
                    case "CBEAM":
                        dict_line = get_cbeam(a, dict_line)
                    case "CBAR":
                        dict_line = get_cbar(a, dict_line)
                    case "PSHELL":
                        dict_line = get_shell(a, dict_line)
                    case "PBEAM":
                        dict_line = get_pbeam(a, dict_line)
                    case "PBAR":
                        dict_line = get_pbar(a, dict_line)
                    case "PCOMP":
                        dict_line = get_pcomp(a, dict_line)
                    case "MAT1":
                        dict_line = get_mat1(a, dict_line)
                    case "MAT8":
                        dict_line = get_mat8(a, dict_line)
                if card_type in dict:
                    dict[card_type] += [dict_line]
                else:
                    dict[card_type] = [dict_line]
    my_file.close()

    return dict


def get_cquad(a):
    # try:
    #     d['property'] = a[2].strip()
    #     d['grids'] = a[3].strip() + " " + a[4].strip() + " " + a[5].strip() + " " + a[6].strip()
    #     d['orientation'] = a[7].strip()
    # except:
    #     pass
    cquad=Element(a[0].strip(),a[1].strip(),a[2].strip(),a[3].strip() + " " + a[4].strip() + " " + a[5].strip() + " " + a[6].strip(),a[7].strip())
    return cquad


def get_ctria(a, d):
    try:
        d['property'] = a[2].strip()
        d['grids'] = a[3].strip() + " " + a[4].strip() + " " + a[5].strip()
        d['orientation'] = a[6].strip()
    except:
        pass
    return d


def get_cbeam(a, d):
    try:
        d['property'] = a[2].strip()
        d['grids'] = a[3].strip() + " " + a[4].strip()
        d['orientation'] = a[5].strip() + " " + a[6].strip() + " " + a[7].strip()
    except:
        pass
    return d


def get_cbar(a, d):
    try:
        d['property'] = a[2].strip()
        d['grids'] = a[3].strip() + " " + a[4].strip()
        d['orientation'] = a[5].strip() + " " + a[6].strip() + " " + a[7].strip()
    except:
        pass
    return d


def get_shell(a, d):
    try:
        d['material'] = a[2].strip()
        d['data'] = a[3].strip() + " " + a[4].strip() + " " + a[5].strip() + " " + a[6].strip() + " " + a[7].strip()
    except:
        pass
    return d


def get_pbeam(a, d):
    try:
        d['material'] = a[2].strip()
        d['data'] = a[3].strip() + " " + a[4].strip() + " " + a[5].strip() + " " + a[6].strip() + " " + a[7].strip()
    except:
        pass
    return d


def get_pbar(a, d):
    try:
        d['material'] = a[2].strip()
        d['data'] = a[3].strip() + " " + a[4].strip() + " " + a[5].strip() + " " + a[6].strip()
    except:
        pass
    return d


def get_pcomp(a, d):
    try:
        d['material'] = a[2].strip()
        d['data'] = a[3].strip() + " " + a[4].strip() + " " + a[5].strip() + " " + a[6].strip() + " " + a[
            7].strip() + " " + a[8].strip() + " " + a[9].strip()
    except:
        pass
    return d


def get_mat1(a, d):
    try:
        d['data'] += a[2].strip()
        d['data'] += a[3].strip()
        d['data'] += a[4].strip()
        d['data'] += a[5].strip()
        d['data'] += a[6].strip()
        d['data'] += a[7].strip()
        d['data'] += a[8].strip()
    except:
        d['data'] = a[2].strip()
        d['data'] = a[3].strip()
        d['data'] = a[4].strip()
        pass
    return d


def get_mat8(a, d):
    try:
        d['data'] = a[2].strip() + " " + a[3].strip() + " " + a[4].strip() + " " + a[5].strip() + " " + a[
            6].strip() + " " + a[7].strip() + " " + a[8].strip()
    except:
        pass
    return d
