def quickSortV1(lst, pocet=0):
    pocet = 0

    pocet += 1
    if len(lst) <= 1:
        return lst, 1

    x = 0
    y = -1

    pivotIndex = len(lst) - 1
    pivot = lst[pivotIndex]

    while True:
        pocet += 1
        if x == pivotIndex:
            y += 1
            lst[pivotIndex], lst[y] = lst[y], lst[pivotIndex]
            break

        pocet += 1
        if lst[x] < pivot:
            y += 1
            lst[x], lst[y] = lst[y], lst[x]
            x += 1
        else:
            x += 1
        
    left = lst[:y]
    right = lst[y + 1:]

    lstLeft, pocetLeft = quickSortV1(left, pocet)
    lstRight, pocetRight = quickSortV1(right, pocet)

    return lstLeft + [pivot] + lstRight, pocet + pocetLeft + pocetRight

def quickSortV2(lst, pocet=0):
    pocet = 0

    pocet += 1
    if len(lst) <= 1:
        return lst, 1

    left = []
    right = []

    pivot = lst[len(lst) - 1]

    for i in range(len(lst) - 1):
        pocet += 1
        if lst[i] < pivot:
            left.append(lst[i])
        else:
            right.append(lst[i])

    lstLeft, pocetLeft = quickSortV2(left)
    lstRight, pocetRight = quickSortV2(right)

    return lstLeft + [pivot] + lstRight, pocet + pocetLeft + pocetRight

def quickV1(lst):
    return quickSortV1(lst)[1]

def quickV2(lst):
    return quickSortV2(lst)[1]