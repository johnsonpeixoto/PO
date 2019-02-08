from random import randint
import time 

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def geraLista(tam, caso): #1- melhor /2- medio /3- pior
	lista = []
	if (caso == 1):
		for i in range(0, tam):
			lista.append(i)
	elif (caso == 2):
		for i in range(0, tam):
			n = randint(1, 1 * tam)
			lista.append(n)
	elif (caso == 3):
		for i in range(tam-1, -1, -1):
			lista.append(i)
	else:
		print ("Caso errado")
		return False
	return lista

def bubbleSort(serie): # sem numero de swaps
    for num in range(len(serie) - 1, 0, -1):
        for i in range(num):
            if serie[i] > serie[i + 1]:
                temp = serie[i]
                serie[i] = serie[i + 1]
                serie[i + 1] = temp

def geraGraf(x,y,xl,yl,lb,filew):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label = lb)
    ax.legend(bbox_to_anchor=(1, 1),			bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(filew)

series = [1000, 2000, 3000, 4000, 6000]
casos = [1,2,3]
swaps = []
tempos = []

for tam in series:
    tempos = []
    for c in casos:
        lista = geraLista(tam,c)
        inicio = time.time()
        bubbleSort(lista)
        tempo = time.time() - inicio
        #tempo = timeit.timeit("bubbleSort({})".format(lista),setup="from __main__ import bubbleSort",number=1)
        tempos.append(tempo)
    geraGraf(casos, tempos, "series", "tempo", "tempo de processo", str(tam)+"_"+str(casos)+".png")

print("Finish")