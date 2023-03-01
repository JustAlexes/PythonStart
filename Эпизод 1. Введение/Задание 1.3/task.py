# Пример 1
def task_1(n):

    result = 0
    for i in range(1, 11):
        result += 1 / i
    return result

# Пример 2
def task_2(x, n):

    result = x
    for i in range(1, 9):
        result += x / (2 * i + 1)
    return result

# Пример 3
def task_3(n):

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Пример 4
def task_4(x, n):

    result = 1
    for i in range(2, 10):
        result *= (x + i) / i
    return result

# Пример 5
def task_5(x, n):

    result = 0
    for i in range(1, n + 1):
        result += x / 2
    return result

# Пример 6
def task_6(n):

    result = 1
    for i in range(1, 11):
        result *= 2 * i
    return result
