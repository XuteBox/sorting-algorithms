def mergeSortV1(lst, pocet=0):
    pocet += 1
    if len(lst) <= 1:
        return lst, pocet
    
    mid = len(lst) // 2

    left, pocetLeft = mergeSortV1(lst[:mid])
    right, pocetRight = mergeSortV1(lst[mid:])

    pocet += pocetLeft + pocetRight

    lst = []

    length = len(left) + len(right)

    indexLeft = 0
    indexRight = 0

    while length > len(lst):
        l = left[indexLeft] if indexLeft < len(left) else float("inf")
        r = right[indexRight] if indexRight < len(right) else float("inf")
        pocet += 4
        if l <= r:
            lst.append(l)
            indexLeft += 1
        else:
            lst.append(r)
            indexRight += 1

    return lst, pocet

def mergeSortV2(lst, pocet=0):
    pocet += 1
    if len(lst) < 2:
        return lst, pocet
    mid = len(lst) // 2
    lst, pct = merge(mergeSortV2(lst[:mid]), mergeSortV2(lst[mid:]))
    return lst, pocet + pct

def merge(l1, l2):
    pocet = l1[1] + l2[1]
    l1 = l1[0]
    l2 = l2[0]

    length = len(l1) + len(l2)

    i = 0
    j = 0
    lst = []
    while length > len(lst):
        pocet += 4
        l = l1[i] if i < len(l1) else float("inf")
        r = l2[j] if j < len(l2) else float("inf")
        if l <= r:
            lst.append(l)
            i += 1
        else:
            lst.append(r)
            j += 1
    return lst, pocet

def mergeV1(lst):
    return mergeSortV1(lst)[1]

def mergeV2(lst):
    return mergeSortV2(lst)[1]