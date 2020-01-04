'''
Desempaquetamiento

Es la extraccion de los elementos  contenidos
en una estructura
    lista = [10, 20]

    def func(a, b):
        print()
    func(*lista)
    func(10, 20)
    func(a=10, b=20)

'''

"""
lista =[10, 20]
def func(a, b):
    print()

func(*lista)
func(10, 20)
func(a=10, b=20)
"""
def persona(nombre, apellido,edad):
    print(nombre)
    print(apellido)
    print(edad)
#tupla = "Julio","Rivera", 23
#persona(tupla[0], tupla[1], tupla[2])
#persona(*tupla)

#diccionario
d = {"nombre":"Julio", "apellido":"Rivera", "edad":23}
persona(**d)
