
#Lista
#====================================================
"""
NO SIRVE ESTE ALGORITMO

lista_numero = [100,200,300,400]
for item in lista_numero:#Ciclo de repeticion
    item += 1000
print(lista_numero)

"""
#====================================================
'''
lista_numero = [100, 200, 300, 400, 500,600,700,800]
lista_indice= range(4)
for item in lista_indice:#Ciclo de repeticion
    lista_numero[item] += 1000
print(lista_numero)

'''
#====================================================
#Funcione de
lista_numero = [100, 200, 300, 400, 500,600,700,800]
for idx, item in enumerate(lista_numero):#Ciclo de repeticion
    lista_numero[idx]+= 1000
print(lista_numero)

