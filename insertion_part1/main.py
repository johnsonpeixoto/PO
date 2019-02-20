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

def geraGraf(x, lab, y, xl, yl, filew):
	cores = ['blue', 'green', 'red', 'purple', 'black']
	fig = plt.figure(figsize=(10, 10))
	ax = fig.add_subplot(111)
	for i in range(0, len(lab)):
		ax.plot(x, y[i], label=lab[i], markerfacecolor=cores[i], markersize=12)
	ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
	plt.ylabel(yl)
	plt.xlabel(xl)
	fig.savefig(filew)

series = [1000, 2000, 3000, 4000, 6000]
casos = ["melhor","medio","pior"]
tempos = []
for tam in series:
	t = []
	for c in casos:
		t.append(timeit.timeit("insertionSort({})".format(geraLista(tam, c)),setup="from __main__ import insertionSort", number=1))
	tempos.append(t)
	#print(tempos)

geraGraf(casos, series, tempos, "Casos", "Tempo", "tempos.png")

print("Finish")
