# verze V1 vybírají na místo pivota poslední člen listu a vytváří pomocné listy (horší časová složitost)
def quickSortV1_1(lst, pocet=0):
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

    lstLeft, pocetLeft = quickSortV1_1(left, pocet)
    lstRight, pocetRight = quickSortV1_1(right, pocet)

    return lstLeft + [pivot] + lstRight, pocet + pocetLeft + pocetRight

def quickSortV1_2(lst, pocet=0):
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

    lstLeft, pocetLeft = quickSortV1_2(left)
    lstRight, pocetRight = quickSortV1_2(right)

    return lstLeft + [pivot] + lstRight, pocet + pocetLeft + pocetRight

# tyhle funkce slouží ke vrácení pouze comparisons, protože potřebují rekurzivně přijímat listy
def quickV1_1(lst):
    return quickSortV1_1(lst)[1]

def quickV1_2(lst):
    return quickSortV1_2(lst)[1]

# verze V2 nevytváří pomocné listy
# verze V2_1 používá jako pivota poslední člen listu
# verze V2_2 používá jako pivota prostřední člen listu
def quickSortV2_1(lst, low=0, high=None, pocet=0):
    pocet += pocet

    pocet += 1
    if high is None:
        high = len(lst) - 1
    
    pocet += 1
    if low < high:
        pivotIndex, pct = partitionV1(lst, low, high)
        pocet += pct
        pocet += quickSortV2_1(lst, low, pivotIndex - 1)
        pocet += quickSortV2_1(lst, pivotIndex + 1, high)

    return pocet

def partitionV1(lst, low, high, pocet=0):
    i = low - 1
    j = low

    pivotIndex = high
    pivot = lst[pivotIndex]

    while True:
        pocet += 1
        if j == pivotIndex:
            i += 1
            lst[pivotIndex], lst[i] = lst[i], lst[pivotIndex]
            break

        pocet += 1
        if lst[j] < pivot:
            i += 1
            lst[j], lst[i] = lst[i], lst[j]
            j += 1
        else:
            j += 1

    return i, pocet

def quickSortV2_2(lst, low=0, high=None, pocet=0):
    pocet += pocet

    pocet += 1
    if high is None:
        high = len(lst) - 1

    pocet += 1
    if low < high:
        mid, pct = partitionV2(lst, low, high)
        pocet += pct
        pocet += quickSortV2_2(lst, low, mid - 1)
        pocet += quickSortV2_2(lst, mid, high)

    return pocet

def partitionV2(lst, low, high, pocet=0):
    pivot = lst[(low + high) // 2]

    i = low
    j = high

    pocet += 1
    while j >= i:
        pocet += 1

        pocet += 1
        while lst[i] < pivot:
            pocet += 1
            i += 1

        pocet += 1
        while lst[j] > pivot:
            pocet += 1
            j -= 1

        pocet += 1
        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1

    return i, pocet
