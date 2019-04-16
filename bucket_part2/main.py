import timeit
from itertools import permutations           

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def insertionSort(b):
	for i in range(1, len(b)): 
		up = b[i]
		j = i - 1
		while j >=0 and b[j] > up:  
			b[j + 1] = b[j] 
			j -= 1
		b[j + 1] = up     
	return b      
              
def bucketSort(serie): 
	arr = []
	slot_num = 10 
	for i in range(slot_num): 
		arr.append([]) 
	  
	for j in serie: 
		index_b = int(slot_num * j)  
		arr[index_b].append(j) 

	# Ordena buckets individualmente  
	for i in range(slot_num):
		arr[i] = insertionSort(arr[i]) 

	# concatena o resultado
	k = 0
	for i in range(slot_num): 
		for j in range(len(arr[i])): 
			serie[k] = arr[i][j] 
			k += 1
	return serie

def geraLista(tam): # lista de permutações com filtro de tupla
	lista = []
	permuts = list(permutations(range(tam))) # retorna uma lista de tuplas com permutações
	for i in range(0, len(permuts)): # for para remover as tuplas ()
		tupla = []
		for j in range(0, len(permuts[i])):
			tupla.append(permuts[i][j])
		lista.append(tupla)
	return lista

def tempListas(series): # executa selection em cada caso
	tempo = []
	for serie in series:
		tempo.append(timeit.timeit("bucketSort({})".format(serie),setup="from __main__ import bucketSort", number=1))
	return tempo

#######################################################
########	INICIO DO PROGRAMA	###############
#######################################################

series = geraLista(6) # gera uma lista de series de tamanho 6 com todas as permutaçõess
tempos = tempListas(series) # crio uma lista com tempo de ordenamento de cada permutação
print ("O pior caso é a sequência: {} com tempo {}.".format(str(series[tempos.index(max(tempos))]), max(tempos)))
print ("O melhor caso é a sequência: {} com tempo {}.".format(str(series[tempos.index(min(tempos))]), min(tempos)))
