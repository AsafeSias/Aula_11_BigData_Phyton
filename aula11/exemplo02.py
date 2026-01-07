import os
import random


def gerar_numeros(ini, fim, qtd):
    lst_num = [random.randint(ini, fim) for i in range(qtd)]
    return lst_num

# início do algoritmo
inicio = 1
final = 10
quant = 2
lst_numeros = gerar_numeros(inicio, final, quant)
print(lst_numeros)
print(lst_numeros[0])
print(lst_numeros[1])