#Retorno de valores multiples

'''
def func():
    return 20,30

x, y = funcion()
'''

"""
def func():
    return 20,30

x, y = func()

print(x)
print(y)

"""

def potencia(x):
    cuadrado = x**2
    cubo = x**3
    return cuadrado, cubo
q,c = potencia(10)

print(q)
print(c)
