import timeit
from itertools import permutations           

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def quickSort(serie, start, end):
	if start < end:
		pivot = partition(serie,start,end)
		quickSort(serie,start,pivot-1)
		quickSort(serie,pivot+1,end)

def partition(serie,start,end):
	x = serie[end]
	i = start-1
	for j in range(start, end+1, 1):
		if serie[j] <= x:
			i += 1
			if i<j:
				z = serie[i]
				serie[i] = serie[j]
				serie[j] = z    
	return i

def geraLista(tam): # lista de permutações com filtro de tupla
	lista = []
	permuts = list(permutations(range(tam))) # retorna uma lista de tuplas com permutações
	for i in range(0, len(permuts)): # for para remover as tuplas ()
		tupla = []
		for j in range(0, len(permuts[i])):
			tupla.append(permuts[i][j])
		lista.append(tupla)
	return lista

def tempListas(serie): # executa ordenamento em cada caso
	tempo = []
	for i in range(0, len(serie)):
		print(serie)
		tempo.append(timeit.timeit("quickSort({},{},{})".format(serie, 0, len(serie)-1), setup="from __main__ import quickSort", number=1))
	return tempo

#######################################################
########	INICIO DO PROGRAMA	###############
#######################################################

series = geraLista(6) # gera uma lista de series de tamanho 6 com todas as permutaçõess
tempos = tempListas(series) # lista com tempo de ordenamento de cada permutação
print ("O pior caso é a sequência: {} com tempo {}.".format(str(series[tempos.index(max(tempos))]), max(tempos)))
print ("O melhor caso é a sequência: {} com tempo {}.".format(str(series[tempos.index(min(tempos))]), min(tempos)))
