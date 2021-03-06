#!/usr/bin/python3
from random import randint
from timeit import timeit
import sys
sys.setrecursionlimit(1000000)

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def geraLista(tam, caso): #1- melhor /2- medio /3- pior
	print ("Gerando a lista...")
	lista = []
	if (caso == "crescente"):
		for i in range(0, tam):
			lista.append(i)
	elif (caso == "aleatoria"):
		while len(lista) < tam:
			n = randint(0,1*(tam-1))
			if n not in lista: lista.append(n)
	elif (caso == "decrescente"):
		for i in range(tam-1, -1, -1):
			lista.append(i)
	return lista

def insertionSort(array):
	for i in range(1, len(array)):
		tmp = 0
		tmp = array[i]
		position = i
		while position > 0 and array[position - 1] > tmp:
			array[position] = array[position - 1]
			position -= 1
		array[position] = tmp
              
def bucketSort(array):
	code = hashing(array)
	buckets = [list() for _ in range( code[1] )]
	for i in array:
		x = re_hashing(i, code)
		buck = buckets[x]
		buck.append(i)
	for bucket in buckets:
		insertionSort(bucket)

	ndx = 0
	for b in range(len(buckets)):
		for v in buckets[b]:
	    		array[ndx] = v
			ndx = ndx + 1

def geraGraf(x, lab, y, xl, yl, filew):
	print ("Plotando o gráfico 1...")
	cores = ['blue', 'green', 'red', 'purple', 'black']
	fig = plt.figure(figsize=(10, 10))
	ax = fig.add_subplot(111)
	for i in range(0, len(lab)):
		ax.plot(x, y[i], label=lab[i], markerfacecolor=cores[i], markersize=12)
	ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
	plt.ylabel(yl)
	plt.xlabel(xl)
	fig.savefig(filew)

def geraGraf2(x, y, xl, yl, filew):
	print ("Plotando o gráfico 2...")
	fig = plt.figure(figsize=(10, 10))
	ax = fig.add_subplot(111)
	ax.plot(x, y, label="Decrescente")
	ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
	plt.ylabel(yl)
	plt.xlabel(xl)
	fig.savefig(filew)

series = [1000, 2000, 3000, 4000, 5000]
casos = ["crescente","aleatoria","decrescente"]
tempos = []

for tam in series:
	t = []
	for tipo in casos:
		lista = geraLista(tam, tipo)
		t.append(timeit("bucketSort({})".format(lista),setup="from __main__ import bucketSort", number=1))
	tempos.append(t)

print(tempos)
geraGraf(casos, series, tempos, "Casos", "Tempo", "series3casos.png")

series = [2000, 4000, 6000, 8000, 10000]
tempos = []

for tam in series:
	lista = geraLista(tam, "decrescente")
	tempos.append(timeit("bucketSort({})".format(lista),setup="from __main__ import bucketSort", number=1))

print(tempos)
geraGraf2(series, tempos, "Casos", "Tempo", "seriesDecrescente.png")


print("Finish")
