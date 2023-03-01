import math


# Пример 1
def task_1(a, b):

    if a > b:
        return (a * b) ** 0.5 - 3
    elif a == b:
        return math.log10(2)

    return (math.log(a ** 3 + 1)) / b

# Пример 2
def task_2(a, b):

    if a < b:
        return math.tan(a / b) + 1
    elif a == b:
        return math.tan(-1)

    return ((a * b - 5) ** 0.5) / a

# Пример 3
def task_3(a, b):

    if a > b:
        return math.log10(a * b) + 21
    elif a == b:
        return math.tan(-5)

    return math.log(3 * a / b) + 1

# Пример 4
def task_4(a, b):

    if a > b:
        return (a * b - 1) ** 0.5
    elif a == b:
        return math.log10(255)

    return (math.tan(a - 5)) / b

# Пример 5
def task_5(a, b):

    if a > b:
        return math.log(a / b) + 31
    elif a == b:
        return math.tan(-25)
    return (math.cos(a * 5 - 1)) / a

# Пример 6
def task_6(a, b):

    if a < b:
        return (b / a + 1) ** 0.5
    elif a == b:
        return 5
    return math.log10(a ** 3 - 5) / b
