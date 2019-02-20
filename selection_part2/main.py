import timeit
from itertools import permutations           

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def selectionSort(serie): # arg.: lista com as series a seres ordenadas
	for i in range(len(serie)-1, 0, -1):
		menor = 0
		for j in range(1, i+1):
			if(serie[j] > serie[menor]):
				menor = j
		serie[i], serie[menor] = serie[menor], serie[i] 
	return serie

def geraLista(tam): # lista de permutações com filtro de tupla
	lista = []
	permuts = list(permutations(range(tam))) # retorna uma lista de tuplas com permutações
	for i in range(0, len(permuts)): # for para remover as tuplas ()
		tupla = []
		for j in range(0, len(permuts[i])):
			tupla.append(permuts[i][j])
		lista.append(tupla)
	#print (lista)
	return lista

def tempListas(serie): # executa selection em cada caso
	tempo = []
	for i in range(0, len(serie)):
		tempo.append(timeit.timeit("selectionSort({})".format(serie),setup="from __main__ import selectionSort", number=1))
	return tempo

def retornaPiorCaso(s): # argumento com uma serie de tempo embaralhadas
	maximo = max(s) # tempo maximo da serie de tempos
	print (maximo)
	return s.index(maximo)
	

def geraGraf(x,y,xl,yl,lab, filew):
	fig = plt.figure(figsize=(10, 10))
	ax = fig.add_subplot(111)
	ax.plot(x, y, label= lab, marker='.', markerfacecolor='blue', markersize=12)
	ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
	plt.ylabel(yl)
	plt.xlabel(xl)
	fig.savefig(filew)

#######################################################
########	INICIO DO PROGRAMA	###############
#######################################################

series = geraLista(4) # gera uma lista de series de tamanho 6 com todas as permutaçõess
tempos = tempListas(series) # crio uma lista com tempo de ordenamento de cada permutação
print (tempos)
print ("O pior caso é a sequencia: "+str(series[retornaPiorCaso(tempos)]))
sortTempos = selectionSort(tempos) # ordeno a lista com tempos crescentes
print (sortTempos)
temps = []
temps.append(sortTempos[0]) # adiciono o menor tempo
temps.append(sortTempos[int(len(sortTempos)/2)]) # adiciono o tempo medio
temps.append(sortTempos[len(sortTempos)-1]) # adiciono o maior tempo
print (temps)
casos = ["melhor", "medio", "pior"]
geraGraf(casos, temps, "Casos", "Tempo", "função ordenação 6!", "tempos.png")
