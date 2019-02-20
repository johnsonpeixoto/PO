import matplotlib.pyplot as plt
from timeit import timeit
from random import randint
import itertools as it

# the idea is always look for the smaller array element and insert it on the vector top.
# any ideas why the graph looks so stranger? I dont

def selectionSort(listToSort):
    for j in range(len(listToSort)-1,0,-1):
        x = 0
        for i in range(1,j+1):
            if listToSort[i]>listToSort[x]:
                x = i
        listToSort[j],listToSort[x] = listToSort[x],listToSort[j]
    return listToSort

#generate unSorted array with gave lenght
def listGenerator(lenList):
    generated = []
    for i in range(lenList):
        while len(generated) != lenList:
            n = randint(1,1*lenList)
            if n not in generated: generated.append(n)
    return generated

def drawGraph(listQt,medium,best,worst,xl = "Elementos", yl = "Tempo"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(listQt,medium, label = "Caso Medio")
    ax.plot(listQt,best, label = "Melhor Caso")
    ax.plot(listQt,worst, label="Pior Caso")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()
    fig.savefig('selectionSort2.png')

#lenghts to diferent arrays
length = [1000,2000,3000,4000,5000]

#array to store the necessary time to sort each array
mediumTimes = []
bestTimes = []
worstTimes = []

for i in length:
    mediumList = listGenerator(i)
    bestList = sorted(mediumList)
    worstList = sorted(bestList, reverse=True)

    mediumTimes.append(timeit("selectionSort({})".format(mediumList),setup="from __main__ import selectionSort",number=1))
    bestTimes.append(timeit("selectionSort({})".format(bestList),setup="from __main__ import selectionSort",number=1))
    worstTimes.append(timeit("selectionSort({})".format(worstList),setup="from __main__ import selectionSort",number=1))

drawGraph(length, mediumTimes, bestTimes, worstTimes)

# Verify the worst case
worstCaseExperience = list(it.permutations([1,2,3,4,5,6],6))

# permutimes and worstcase will have the same len, so the index is equivalent each other
permuTimes = []
for permutation in worstCaseExperience:
    listToSort = list(permutation)
    permuTimes.append(timeit("selectionSort({})".format(listToSort),setup="from __main__ import selectionSort",number=1))

smallerTime = min(permuTimes)
smallerTimeIndex = permuTimes.index(smallerTime)
# worst case list
print(worstCaseExperience[smallerTimeIndex])
