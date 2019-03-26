import timeit
from itertools import permutations           

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def countSort(lista):
	maior = max(lista)
	output = [0 for i in range(maior+1)] 
	count = [0 for i in range(maior+1)]
	ans = ["" for _ in lista] 

	for i in lista:
		count[i] += 1

	for i in range(maior): 
		count[i] += count[i-1] 

	for i in range(len(lista)): 
		output[count[lista[i]]-1] = lista[i] 
		count[lista[i]] -= 1

	for i in range(len(lista)): 
		ans[i] = output[i] 
	return ans  

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
		tempo.append(timeit.timeit("countSort({})".format(serie), setup="from __main__ import countSort", number=1))
	return tempo

#######################################################
########	INICIO DO PROGRAMA	###############
#######################################################

series = geraLista(6) # gera uma lista de series de tamanho 6 com todas as permutaçõess
tempos = tempListas(series) # lista com tempo de ordenamento de cada permutação
print ("O pior caso é a sequência: {} com tempo {}.".format(str(series[tempos.index(max(tempos))]), max(tempos)))
print ("O melhor caso é a sequência: {} com tempo {}.".format(str(series[tempos.index(min(tempos))]), min(tempos)))
