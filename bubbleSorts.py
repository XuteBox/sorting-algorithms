def bubbleSortV1(lst):
    pocet = 0

    for i in range(0, len(lst)):
        for j in range(0, len(lst) - 1):
            pocet += 1
            
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return pocet

def bubbleSortV2(lst):
    pocet = 0
    velikost = len(lst)

    for i in range(velikost):
        for j in range(velikost -1 - i):
            pocet += 1
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return pocet

def bubbleSortV3(lst):
    pocet = 0
    velikost = len(lst)

    for i in range(velikost):
        sorted = True
        for j in range(velikost -1 - i):
            pocet += 1

            if lst[j] > lst[j + 1]:
                sorted = False
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

        pocet += 1
        if sorted == True:
            break
    return pocet

def bubbleSortV4(lst):
    pocet = 0
    spodni = 0
    horni = len(lst) - 1

    for i in range(0, len(lst)):
        sorted = True
        for j in range(spodni, horni):
            pocet += 1
            if lst[j] > lst[j + 1]:
                sorted = False
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

        horni -= 1

        if sorted == True:
            break

        sorted = True

        for j in range(horni, spodni, -1):
            pocet += 1
            if lst[j - 1] > lst[j]:
                sorted = False
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
        spodni += 1

        if sorted == True:
            break

    return pocet