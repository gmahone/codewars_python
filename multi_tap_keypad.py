def presses(phrase):
    pad = ["1","*","#","ABC2","DEF3","GHI4","JKL5","MNO6","PQRS7","TUV8","WXYZ9"," 0"]
    type_dict = {}
    for i in pad:
        for j in range(0, len(i)):
           type_dict.update({i[j]: (j+1)})
    presses = 0
    for i in phrase:
        print(i)
        if i.isalnum() or i == " " or i == "*" or i == "#":
            print(i)
            presses += type_dict[i.upper()]
    return presses
