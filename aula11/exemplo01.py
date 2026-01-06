#Bibliotecas
import random

# random.randint -> Números inteiros
n = random.randint(1,10)
m = random.randint(1,10)
# print(n, m)

#-------------------------------------
# Gerar número decimais

n_decimal = random.uniform(1,10)
numero_decimal = round(n_decimal,3) #Arredonda
print(f'{n_decimal:.2f}') #Formatação para duas casas
print(numero_decimal)

#---------------------------------------
# Gerar número aleatórios dentro de uma lista
lst_numeros = [random.randint(1,10) for num in range(5)]
print(lst_numeros)