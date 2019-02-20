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

def selectionSort(serie): # arg.: lista com as series a seres ordenadas
	for i in range(len(serie)-1, 0, -1):
		menor = 0
		for j in range(1, i+1):
			if(serie[j] > serie[menor]):
				menor = j
		serie[i], serie[menor] = serie[menor], serie[i]
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
		t.append(timeit.timeit("selectionSort({})".format(geraLista(tam, c)),setup="from __main__ import selectionSort", number=1))
	tempos.append(t)
geraGraf(casos, series, tempos, "Casos", "Tempo", "tempos.png")

print("Finish")
