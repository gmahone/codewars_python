def stock_list(listOfArt, listOfCat):
    art_dict = {}
    for i in listOfArt:
        split_temp = i.split(" ")
        if split_temp[0][0] in art_dict:
            art_dict[split_temp[0][0]] += int(split_temp[1])
        else:
            art_dict[split_temp[0][0]] = int(split_temp[1])
