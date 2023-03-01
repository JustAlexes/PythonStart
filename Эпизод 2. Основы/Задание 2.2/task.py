# Пример 1
def task_1(A):

    result = 0
    for element in A:
        if element > 0:
            result += element
    return result

# Пример 2
def task_2(A):

    result = 0
    for element in A:
        result += element
    return result / len(A)

# Пример 3
def task_3(A):

    result = 0
    average = task_2(A)
    for element in A:
        result += (element - average) ** 2
    result *= 1 / len(A)
    return result ** 0.5
