import timeit
from itertools import permutations           

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def insertionSort(serie):
	for i in range(1,len(serie)):
		valor = serie[i]
		indice = i

		while indice>0 and serie[indice-1]>valor:
			serie[indice]=serie[indice-1]
			indice = indice-1

		serie[indice]=valor
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

def tempListas(serie): # executa selection em cada caso
	tempo = []
	for i in range(0, len(serie)):
		print(serie[i])
		tempo.append(timeit.timeit("insertionSort({})".format(serie[i]),setup="from __main__ import insertionSort", number=1))
	return tempo

#######################################################
###########   INICIO DO PROGRAMA   ###################
#######################################################

series = geraLista(6) # gera uma lista de series de tamanho 6 com todas as permutaçõess
tempos = tempListas(series) # crio uma lista com tempo de ordenamento de cada permutação
print (tempos)
print ("O pior caso foi a sequência: "+str(series[tempos.index(max(tempos))]))
print ("O melhor caso foi a sequência: "+str(series[tempos.index(min(tempos))]))

