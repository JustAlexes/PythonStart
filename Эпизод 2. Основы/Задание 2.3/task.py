# todo: replace this with an actual task
def task_1(str):

    words = str.split()
    lastWord = words[- 1]
    return len(lastWord)

def task_2(str):

    words = str.split()
    count = len(words)
    newWordsOrder = []
    for i in range(0, count, 2):
        if i + 1 < count:
            newWordsOrder.append(words[i + 1])
        newWordsOrder.append(words[i])
    return ' '.join(newWordsOrder)

def task_3(str):

    words = str.split()
    count = 0
    prevWord = ''
    for word in words:
        if prevWord == '':
            prevWord = word
            continue
        if word[0] == prevWord[len(prevWord) - 1]:
            count += 1
        prevWord = word
    return count
