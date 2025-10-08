def selectV1(lst):
    pocet = 0

    for i in range(len(lst) - 1):
        index = i
        nejmensi = lst[i]
        for j in range(i + 1, len(lst)):
            pocet += 1
            if nejmensi >= lst[j]:
                nejmensi = lst[j]
                index = j

        lst[i], lst[index] = lst[index], lst[i]
    return pocet