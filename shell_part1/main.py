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

def shellSort(arr): 
	n = len(arr) 
	pivo = n//2
	while pivo > 0:
		for i in range(pivo,n):  
			temp = arr[i] 
			j = i 
			while j >= pivo and arr[j-pivo] >temp: 
				arr[j] = arr[j-pivo] 
				j -= pivo
			arr[j] = temp 
		pivo //= 2

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
		t.append(timeit("shellSort({})".format(lista),setup="from __main__ import shellSort", number=1))
	tempos.append(t)

print(tempos)
geraGraf(casos, series, tempos, "Casos", "Tempo", "series3casos.png")

series = [2000, 4000, 6000, 8000, 10000]
tempos = []

for tam in series:
	lista = geraLista(tam, "decrescente")
	tempos.append(timeit("shellSort({})".format(lista),setup="from __main__ import shellSort", number=1))

print(tempos)
geraGraf2(series, tempos, "Casos", "Tempo", "seriesDecrescente.png")

print("Finish")
