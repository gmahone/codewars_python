## not working version here

str = "COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH"
we = [1, 4, 4, 5, 2, 1]

rank_dict = {}
name_list = str.split(",")
for i in range(0,len(name_list)):
    curr_name = name_list[i]
    word_value = len(curr_name)
    for curr_letter in curr_name:
        word_value += ord(curr_letter.upper())-64
    rank_dict[curr_name] = word_value * we[i]
sorted(rank_dict.items(), key=lambda x:x[1])

# occurrences = lambda s, lst: (i for i,e in enumerate(lst) if e == s)
# list(occurrences(1, [1,2,3,1])) # = [0, 3]

# print(dict(sorted(rank_dict.items(), key=lambda item: item[0])))
# print(dict(sorted(rank_dict.items(), key=lambda x:x[1])))
print(sorted(rank_dict.items(), key=lambda x:x[1])[3][1])
# print(list(rank_dict.keys())[list(rank_dict.values()).index(172)])
print(list(rank_dict.values()).index(172))

## working version below

rank_list = []
name_list = str.split(",")
for i in range(0,len(name_list)):
    curr_name = name_list[i]
    word_value = len(curr_name)
    for curr_letter in curr_name:
        word_value += ord(curr_letter.upper())-64
    rank_list.append((curr_name,word_value * we[i]))
rank_list.sort(key=lambda tup: tup[1], reverse=True)
print(rank_list)
filtered_rank = list(filter(lambda tup: tup[1] == rank_list[n-1][1], rank_list))
filtered_rank.sort(key=lambda tup: tup[0])
winner = filtered_rank[0][0]
print(winner)

# two ways
#sorted_by_second = sorted(rank_list, key=lambda tup: tup[1])
# rank_list.sort(key=lambda tup: tup[1])  # sorts in place
# filtered_rank = list(filter(lambda tup: tup[1] == 172, rank_list))
# print(filtered_rank)
# filtered_rank.sort(key=lambda tup: tup[0])
# print(filtered_rank[0][0])
