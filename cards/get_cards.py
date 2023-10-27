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
                        dict_line = get_cquad(a, dict_line)
                        # dict_line["property"] = a[2].strip()
                        # dict_line["grids"] = a[3].strip() + " " + a[4].strip() + " " + a[5].strip() + " " + a[6].strip()
                        # dict_line["mcid"] = a[7].strip()
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


def get_cquad(a, d):
    try:
        d["property"] = a[2].strip()
        d["grids"] = a[3].strip() + " " + a[4].strip() + " " + a[5].strip() + " " + a[6].strip()
        d["orientation"] = a[7].strip()
    except:
        pass
    return d


def get_ctria(a, d):
    try:
        d["property"] = a[2].strip()
        d["grids"] = a[3].strip() + " " + a[4].strip() + " " + a[5].strip()
        d["orientation"] = a[6].strip()
    except:
        pass
    return d


def get_cbeam(a, d):
    try:
        d["property"] = a[2].strip()
        d["grids"] = a[3].strip() + " " + a[4].strip()
        d["orientation"] = a[5].strip() + " " + a[6].strip() + " " + a[7].strip()
    except:
        pass
    return d


def get_cbar(a, d):
    try:
        d["property"] = a[2].strip()
        d["grids"] = a[3].strip() + " " + a[4].strip()
        d["orientation"] = a[5].strip() + " " + a[6].strip() + " " + a[7].strip()
    except:
        pass
    return d


def get_shell(a, d):
    try:
        d["material"] = a[2].strip()
        d["th"] = a[3].strip()
        d["MID2"] = a[4].strip()
        d["BI"] = a[5].strip()
        d["MID3"] = a[6].strip()
        d["SI"] = a[7].strip()
    except:
        pass
    return d


def get_pbeam(a, d):
    try:
        d["material"] = a[2].strip()
        d["area"] = a[3].strip()
        d["I1"] = a[4].strip()
        d["I2"] = a[5].strip()
        d["I2"] = a[6].strip()
        d["J"] = a[7].strip()
    except:
        pass
    return d


def get_pbar(a, d):
    try:
        d["material"] = a[2].strip()
        d["area"] = a[3].strip()
        d["I1"] = a[4].strip()
        d["I2"] = a[5].strip()
        d["J"] = a[6].strip()
    except:
        pass
    return d


def get_pcomp(a, d):
    try:
        d["material"] = a[2].strip()
        d["Z0"] = a[3].strip()
        d["NSM"] = a[4].strip()
        d["SB"] = a[5].strip()
        d["FT"] = a[6].strip()
        d["TREF"] = a[7].strip()
        d["GE"] = a[8].strip()
        d["LAM"] = a[9].strip()
    except:
        pass
    return d


def get_mat1(a, d):
    try:
        d["E"] = a[2].strip()
        d["G"] = a[3].strip()
        d["NU"] = a[4].strip()
        d["RHO"] = a[5].strip()
        d["A"] = a[6].strip()
        d["TREF"] = a[7].strip()
        d["GE"] = a[8].strip()
    except:
        pass
    return d


def get_mat8(a, d):
    try:
        d["E1"] = a[2].strip()
        d["E2"] = a[3].strip()
        d["NU12"] = a[4].strip()
        d["G12"] = a[5].strip()
        d["G1Z"] = a[6].strip()
        d["G2Z"] = a[7].strip()
        d["RHO"] = a[8].strip()
    except:
        pass
    return d
