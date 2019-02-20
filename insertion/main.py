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
	return lista

def insertionSort(serie):
	for i in range(1,len(serie)):
		valor = serie[i]
		indice = i

		while indice>0 and serie[indice-1]>valor:
			serie[indice]=serie[indice-1]
			indice = indice-1

		serie[indice]=valor

	return serie

def geraGraf(x,y,xl,yl,lab, filew):
	fig = plt.figure(figsize=(10, 10))
	ax = fig.add_subplot(111)
	ax.plot(x, y, label= lab, marker='o', markerfacecolor='blue', markersize=12)
	ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
	plt.ylabel(yl)
	plt.xlabel(xl)
	fig.savefig(filew)

series = [10000, 20000, 30000, 40000, 60000]
casos = ["melhor","medio","pior"]
tempos = []
for tam in series:
	tempos = []
	for c in casos:
		lista = geraLista(tam, c)
		tempos.append(timeit.timeit("insertionSort({})".format(lista),setup="from __main__ import insertionSort", number=1))
	print(tempos)
	geraGraf(casos, tempos, "Casos", "Tempo", "Tempo da Serie "+str(tam), "casos de "+str(tam)+".png")

print("Finish")
