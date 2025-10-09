import copy
import matplotlib.pyplot as plt
import numpy as np
import time

from bubbleSorts import bubbleSortV1, bubbleSortV2, bubbleSortV3, bubbleSortV4
from insertionSorts import insertSortV1, insertSortV2
from quickSorts import quickV1, quickV2
from selectionSorts import selectV1
from shellSorts import shellSortV1

def measureSorts():
    rozsah = range(od, do + 1, krok)

    listLens = [n for n in rozsah]

    comps = [[] for _ in funcList]
    times = [[] for _ in funcList]

    for n in rozsah:
        lst = list(range(1, n))
        np.random.shuffle(lst)

        for i, func in enumerate(funcList):
            deepCopy = copy.deepcopy(lst)

            start = time.time()
            comp = func(deepCopy)
            end = time.time()

            print(func.__name__, n)

            comps[i].append(comp)
            times[i].append(end - start)

    axs = plt.subplots(1, 2, figsize=(14, 5))[1]

    for i in range(len(comps)):
        axs[0].plot(listLens, comps[i], label=funcList[i].__name__)
    axs[0].legend()
    axs[0].set_xlabel('List Size')
    axs[0].set_ylabel('Comparisons')
    axs[0].set_title('Time Complexity')

    for i in range(len(times)):
        axs[1].plot(listLens, times[i], label=funcList[i].__name__)
    axs[1].legend()
    axs[1].set_xlabel('List Size')
    axs[1].set_ylabel('Time')
    axs[1].set_title('Sorting Time')

    plt.tight_layout()
    plt.show()

#můžete upravit velikost a počet čísel v listu, které algoritmy budou třídit
od = 1000 #nastavte počáteční velikost listu 
do = 10000 #nastavte konečnou velikost listu
krok = 1000 #nastavte po kolika se má zvětšovat list

#vyřaďte jakýkoliv sort z měření tím, že ho dáte do komentáře
#při stažení souboru je bubble verze 1 vyřazena pro ukázku
funcList = [
    #bubbleSortV1,
    bubbleSortV2,
    bubbleSortV3,
    bubbleSortV4,
    insertSortV1,
    insertSortV2,
    selectV1,
    shellSortV1,
    quickV1,
    quickV2
]

measureSorts()