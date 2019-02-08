from random import randint
import time

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def geraLista(tam, caso): #1- melhor /2- medio /3- pior
	lista = []
    if (caso == 1):
        for i in range(0, tam):
            lista.append(n)
    elif (caso == 2):
        for i in range(0, tam):
            n = randint(1, 1 * tam)
            lista.append(n)
    elif (caso == 3):
        for i in range(tam-1, -1, -1):
            lista.append(n)
    else:
        print ("Caso errado")
        return False
    return lista

def bubbleSort(serie):
    n_swap = 0
    for passnum in range(len(serie) - 1, 0, -1):
        for i in range(passnum):
            if serie[i] > serie[i + 1]:
                temp = serie[i]
                serie[i] = serie[i + 1]
                serie[i + 1] = temp
                n_swap += 1
    return n_swap

def geraGraf(x,y,xl,yl,lb,filew):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label = lb)
    ax.legend(bbox_to_anchor=(1, 1),			bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(filew)

	#plt.show()
	#figS = plt.figure(figsize=(10, 8))

series = [10000, 20000, 30000, 40000, 50000]
swaps = []
tempos = []

for tam in series:
	lista = geraLista(tam)
	inicio = time.time()
	swp = bubbleSort(lista)
	tempo = time.time() - inicio
	#tempo = timeit.timeit("bubbleSort(lista)".format(100),setup="from __main__ import bubbleSort",number=1)
	swaps.append(swp)
	tempos.append(tempo)

geraGraf(series, swaps, "series", "swaps", "numero de swaps", "swaps.png")
geraGraf(series, tempos, "series", "tempo", "tempo de processo", "tempo.png")
