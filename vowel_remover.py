def shortcut(s):
    for i in list("aeiou"):
        s = "".join(s.split(i))
    return s


# solution using .translate()
