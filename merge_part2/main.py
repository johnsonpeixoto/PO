import timeit
from itertools import permutations           

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def mergeSort(lista):
	if len(lista) > 1: 
		mid = len(lista)//2 
		L = lista[:mid] 
		R = lista[mid:]

		mergeSort(L)
		mergeSort(R)

		i = j = k = 0
		  
		while i < len(L) and j < len(R):
			if L[i] < R[j]: 
				lista[k] = L[i] 
				i+=1
			else: 
				lista[k] = R[j] 
				j+=1
			k+=1
		  
		while i < len(L):
			lista[k] = L[i] 
			i+=1
			k+=1
		  
		while j < len(R): 
			lista[k] = R[j] 
			j+=1
			k+=1

def geraLista(tam): # lista de permutações com filtro de tupla
	lista = []
	permuts = list(permutations(range(tam))) # retorna uma lista de tuplas com permutações
	for i in range(0, len(permuts)): # for para remover as tuplas ()
		tupla = []
		for j in range(0, len(permuts[i])):
			tupla.append(permuts[i][j])
		lista.append(tupla)
	return lista

def tempListas(series): # executa ordenamento em cada caso
	tempo = []
	for serie in series:
		tempo.append(timeit.timeit("mergeSort({})".format(serie), setup="from __main__ import mergeSort", number=1))
	return tempo

#######################################################
########	INICIO DO PROGRAMA	###############
#######################################################

series = geraLista(6) # gera uma lista de series de tamanho 6 com todas as permutaçõess
tempos = tempListas(series) # lista com tempo de ordenamento de cada permutação
print ("O pior caso é a sequência: {} com tempo {}.".format(str(series[tempos.index(max(tempos))]), max(tempos)))
print ("O melhor caso é a sequência: {} com tempo {}.".format(str(series[tempos.index(min(tempos))]), min(tempos)))
