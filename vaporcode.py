def vaporcode(s):
    word_list = s.split()
    letter_list = []
    for word in word_list:
        letter_list += list(word.upper())
    print(letter_list)
    pass
