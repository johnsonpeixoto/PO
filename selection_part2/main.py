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
	return lista

def tempListas(series): # executa selection em cada caso
	tempo = []
	for serie in series:
		tempo.append(timeit.timeit("selectionSort({})".format(serie),setup="from __main__ import selectionSort", number=1))
	return tempo

#######################################################
########	INICIO DO PROGRAMA	###############
#######################################################

series = geraLista(6) # gera uma lista de series de tamanho 6 com todas as permutaçõess
tempos = tempListas(series) # crio uma lista com tempo de ordenamento de cada permutação
print ("O pior caso é a sequência: {} com tempo {}.".format(str(series[tempos.index(max(tempos))]), max(tempos)))
print ("O melhor caso é a sequência: {} com tempo {}.".format(str(series[tempos.index(min(tempos))]), min(tempos)))
