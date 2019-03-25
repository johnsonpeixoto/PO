import timeit
from itertools import permutations           

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

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
		tempo.append(timeit.timeit("shellSort({})".format(serie, 0, len(serie)-1), setup="from __main__ import shellSort", number=1))
	return tempo

#######################################################
########	INICIO DO PROGRAMA	###############
#######################################################

series = geraLista(6) # gera uma lista de series de tamanho 6 com todas as permutaçõess
tempos = tempListas(series) # lista com tempo de ordenamento de cada permutação
print ("O pior caso é a sequência: {} com tempo {}.".format(str(series[tempos.index(max(tempos))]), max(tempos)))
print ("O melhor caso é a sequência: {} com tempo {}.".format(str(series[tempos.index(min(tempos))]), min(tempos)))
