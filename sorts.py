import copy
import matplotlib.pyplot as plt
import numpy as np
import time

from bubbleSorts import bubbleSortV1, bubbleSortV2, bubbleSortV3, bubbleSortV4
from insertionSorts import insertSortV1, insertSortV2
from selectionSorts import selectV1
from shellSorts import shellSortV1
from quickSorts import quickV1_1, quickV1_2, quickSortV2_1, quickSortV2_2
from mergeSorts import mergeV1, mergeV2

#můžete upravit velikost a počet čísel v listu, které algoritmy budou třídit
od = 1000 #nastavte počáteční velikost listu 
do = 10000 #nastavte konečnou velikost listu
krok = 1000 #nastavte po kolika se má zvětšovat list

#vyřaďte jakýkoliv sort z měření tím, že ho dáte do komentáře
#při stažení souboru je bubble verze 1 vyřazena pro ukázku
funcList = [
    bubbleSortV1, #blbý bubble sort
    bubbleSortV2, #V1 se zarážkou zprava
    bubbleSortV3, #V2 s kontrolou zda je list seřazený
    bubbleSortV4, #V3 se zarážkou i zleva a zpětným bubble sortem
    insertSortV1,
    insertSortV2, #insert sort s využitím klíče (o trošičku efektivnější)
    selectV1,
    shellSortV1,
    quickV1_1, #jako pivot bere poslední člen, vytváří pomocné listy
    quickV1_2, #jako pivot bere poslední člen, vytváří pomocné listy
    quickSortV2_1, #jako pivot bere poslední člen, nevytváří pomocné listy
    quickSortV2_2, #jako pivot bere prostřední člen, nevytváří pomocné listy
    mergeV1, 
    mergeV2 #stejný jako V1, ale lépe napsaný
]

def measureSorts():
    rozsah = range(od, do + 1, krok)

    listLens = [n for n in rozsah]

    comps = [[] for _ in funcList]
    times = [[] for _ in funcList]
    sortedFuncTime = []

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
        
        # speciální měření pro fuknci sorted, protože nevrací comparisons
        deepCopy = copy.deepcopy(lst)

        start = time.time()
        comp = sorted(deepCopy)
        end = time.time()

        print(sorted.__name__, n)
        
        sortedFuncTime.append(end - start)

    axs = plt.subplots(1, 2, figsize=(14, 5))[1]

    for i in range(len(comps)):
        axs[0].plot(listLens, comps[i], label=funcList[i].__name__)
    axs[0].legend()
    axs[0].set_xlabel('List Size')
    axs[0].set_ylabel('Comparisons')
    axs[0].set_title('Time Complexity (number of comparisons)')

    for i in range(len(times)):
        axs[1].plot(listLens, times[i], label=funcList[i].__name__)
    axs[1].plot(listLens, sortedFuncTime, label=sorted.__name__)
    axs[1].legend()
    axs[1].set_xlabel('List Size')
    axs[1].set_ylabel('Time')
    axs[1].set_title('Sorting Period')

    plt.tight_layout()
    plt.show()
    
measureSorts()
