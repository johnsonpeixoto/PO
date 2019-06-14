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

def montagem(array, n, i): 
	maior = i
	l = 2*i+1 
	r = 2*i+2

	if l < n and array[i] < array[l]: 
		maior = l 

	if r < n and array[maior] < array[r]:
		maior = r 

	if maior != i: 
		array[i],array[maior] = array[maior],array[i] # swap 
		montagem(array, n, maior) 

# Função principal de ordenamento
def heapSort(array): 
	n = len(array)
	for i in range(n, -1, -1): 
		montagem(array, n, i) 

	# Extrai um a um elemento
	for i in range(n-1, 0, -1): 
		array[i], array[0] = array[0], array[i] #swap 
		montagem(array, i, 0)

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

series = [10000, 20000, 30000, 40000, 50000]
casos = ["crescente","aleatoria","decrescente"]
tempos = []

for tam in series:
	t = []
	for tipo in casos:
		lista = geraLista(tam, tipo)
		t.append(timeit("heapSort({})".format(lista),setup="from __main__ import heapSort", number=1))
	tempos.append(t)

print(tempos)
geraGraf(casos, series, tempos, "Casos", "Tempo", "series3casos.png")

series = [10000, 20000, 30000, 40000, 50000]
tempos = []

for tam in series:
	lista = geraLista(tam, "decrescente")
	tempos.append(timeit("heapSort({})".format(lista),setup="from __main__ import heapSort", number=1))

print(tempos)
geraGraf2(series, tempos, "Casos", "Tempo", "seriesDecrescente.png")


print("Finish")
