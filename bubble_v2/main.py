from random import randint
import timeit

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def geraLista(tam, caso): #1- melhor /2- medio /3- pior
	lista = []
	if (caso == "melhor"):
		for i in range(0, tam):
			lista.append(i)
	elif (caso == "medio"):
		while len(lista) < tam:
			n = randint(1,1*tam)
			if n not in lista: lista.append(n)

	elif (caso == "pior"):
		for i in range(tam-1, -1, -1):
			lista.append(i)
	else:
		print ("Caso errado")
		return False
	
	return lista



def bubbleSort(serie): # sem numero de swaps
    for num in range(len(serie) - 1, -1, -1):
        for i in range(num):
            if serie[i] > serie[i+1]:
                temp = serie[i]
                serie[i] = serie[i + 1]
                serie[i + 1] = temp

def geraGraf(x,y,xl,yl,lab, filew):
	fig = plt.figure(figsize=(10, 10))
	ax = fig.add_subplot(111)
	ax.plot(x, y, label= lab, marker='o', markerfacecolor='blue', markersize=12)
	ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
	plt.ylabel(yl)
	plt.xlabel(xl)
	fig.savefig(filew)

series = [1000, 2000, 3000, 4000, 6000]
casos = ["melhor","medio","pior"]
#swaps = []
tempos = []

for tam in series:
	print(tempos)
	tempos = []
	for c in casos:
        	lista = geraLista(tam, c)
        	#bubbleSort(lista)
        	tempos.append(timeit.timeit("bubbleSort({})".format(lista),setup="from __main__ import bubbleSort", number=1))
	geraGraf(casos, tempos, "Casos", "Tempo", "Tempo da Serie "+str(tam), "casos de "+str(tam)+".png")

print("Finish")
