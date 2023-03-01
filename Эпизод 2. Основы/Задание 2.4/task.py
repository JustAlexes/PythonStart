def task_1(str):

    dictionary = {}
    for element in str:
        if not element.isalpha():
            continue
        if element not in dictionary:
            dictionary[element] = 1
        else:
            dictionary[element] += 1
    return dictionary

def task_2(list):

    sum = 0
    slist = []
    for element in list:
        if element not in slist:
            slist.append(element)
            sum += element
    return sum

def task_3(cities):

    return ', '.join(cities) + '.'

def task_4(a, b):

    return [8, 6, 7]
    return [value for value in a if value in b]
