def shellSortV1(lst):
    pocet = 0

    gap = (len(lst) + 1)

    while gap > 1:
        gap = gap // 2
        
        for j in range(gap):
            count = len(lst) // gap
            temp = []

            for i in range(count):
                temp.append(lst[j + gap * i])

            temp, comp = insertSort(temp)

            pocet += comp

            for i in range(count):
                lst[j + gap * i] = temp[i]

    lst, comp = insertSort(lst)
    return pocet + comp

def insertSort(lst):
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
    return lst, pocet