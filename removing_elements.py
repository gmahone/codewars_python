def filter_odd(input):
    if( input % 2 ):
        return False
    else:
        return True

def remove_every_other(my_list):
    filtered_list = filter(filter_odd, my_list)
    result = []
    for x in filtered_list:
        result.append(x)
    return result
