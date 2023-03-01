def task_1(list):
    return max(list, key = list.count)

def task_2(x, y):
    n = 8
    strike = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                strike = False
    if strike:
        return 'NO'
    else:
        return 'YES'

def task_3(x, y, xc, yc, r):
    return ((x - xc) ** 2 + (y - yc) ** 2) <= (r * r)

def task_4(list):
    counter = 0
    for i in range(1, len(list) - 1):
        if list[i - 1] < list[i] > list[i + 1]:
            counter += 1
    return counter

def task_5(key):
    data = open("file.txt", "r").read()
    rows = data.split('\n')
    nRows = []
    for row in rows:
        if '' == row:
            continue
        row = row.lower()
        nRow = ''
        for char in row:
            if char.isalpha():
                nChar = chr((ord(char) + key - 96) % 26 + 96)
            else:
                nChar = chr((ord(char) + key) + 64)
            nRow += nChar
        nRows.append(nRow)
    return nRows