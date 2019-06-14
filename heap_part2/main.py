import timeit
from itertools import permutations           

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

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
		tempo.append(timeit.timeit("heapSort({})".format(serie), setup="from __main__ import heapSort", number=1))
	return tempo

#######################################################
########	INICIO DO PROGRAMA	###############
#######################################################

series = geraLista(6) # gera uma lista de series de tamanho 6 com todas as permutaçõess
tempos = tempListas(series) # lista com tempo de ordenamento de cada permutação
print ("O pior caso é a sequência: {} com tempo {}.".format(str(series[tempos.index(max(tempos))]), max(tempos)))
print ("O melhor caso é a sequência: {} com tempo {}.".format(str(series[tempos.index(min(tempos))]), min(tempos)))
