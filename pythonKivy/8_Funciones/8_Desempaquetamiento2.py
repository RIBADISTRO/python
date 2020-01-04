#DESEMPAQUETAMIENTO


lista = [11,23,45]
tupla= 11,23,45

def func(a,b,c):
    print(a)
    print(b)
    print(c)

#Parte de la ista
'''
lista.sort()
func(*lista)
'''
#Parte de la tupla
'''
l =[*tupla]
l.sort()
func(*tupla)
'''

#Otra forma de organizar los elementos zip
func(**dict(zip(("a","b","c"), lista)))