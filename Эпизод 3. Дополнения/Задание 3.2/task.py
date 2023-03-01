import math

def task_1(a, var):
    mid = len(a) // 2
    low = 0
    high = len(a) - 1
    while a[mid] != var and low <= high:
        if var > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    return str(mid)

def task_2(num):
    prime = True
    for i in range(2, int(math.sqrt(num))):
        if num % i != 0:
            prime = False
    return prime