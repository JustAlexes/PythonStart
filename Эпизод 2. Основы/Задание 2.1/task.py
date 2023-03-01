def task_1(N):

    result = 1
    for i in range(1, N + 1):
        result *= i
    return result

def task_2(N):

    a = 1
    b = 1
    for i in range(1, N + 1):
        b = a + b
    return b

def task_3(N):

    result = []
    for i in range(1, N + 1):
        if N % i == 0:
            result.append(i)
    return result
