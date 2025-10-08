def insertSortV1(lst):
    pocet = 0
    for i in range(1, len(lst)):
        for j in range(i, 0, -1):
            pocet += 1
            
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
            else:
                break
    return pocet

def insertSortV2(lst):
    pocet = 0
    for i in range(1, len(lst)):
        key = lst[i]
        for j in range(i, 0, -1):
            pocet += 1
            
            if key < lst[j - 1]:
                lst[j] = lst[j - 1]
            else:
                lst[j] = key
                break
        else:
            lst[0] = key
    return pocet