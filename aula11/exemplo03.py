import os
import random

lst_numeros = []

def gerar_numeros(ini, fim, qtd):
    lst_num = [random.randint(ini, fim) for i in range(qtd)]
    return lst_num


def soma(n1, n2):
    op_soma = n1 + n2
    return op_soma


def sub (n1,n2):
    op_sub = n1 - n2
    return op_sub


def mult (n1,n2):
    op_mult = n1 * n2
    return op_mult


def div (n1,n2):
    op_div = n1 / n2
    return op_div


inicio = 1
final = 10
quant = 2
lst_numeros = gerar_numeros(inicio, final, quant)
print(lst_numeros)

num1 = lst_numeros[0]
num2 = lst_numeros[1]
soma = soma(num1, num2)
print(soma)
sub = sub(num1, num2)
print(sub)
mult = mult(num1, num2)
print(sub)
div = div(num1, num2)
print(div)