'''
FUNCIONES VARIADICA

Es toda funciones capaz de recibir cantidades arbitrarias de parametros


def fun(*args, **kwargs):
    pass

'''

def listaArgumentos(*lista):
    print(lista)

def listaArgumentosAsociativa(**diccionario):
    print(diccionario)


def argumento(*args, **kwargs):
    print(args)
    print(kwargs)
argumento(1,2,3,4,do=2,tre=3,cua=4)
'''
listaArgumentosAsociativa(a=1, b=2, c=3, e=4)
listaArgumentosAsociativa(uno=1,dos=2,tres=3)

listaArgumentos(1,2,3,4,5,6,7)
listaArgumentos("Julio", "Rivera", "Estudio")
'''