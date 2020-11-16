'''
ARGUMENTOS
POSICIONALES  X NOMBRADOS


def func(para1, para2, para3):
    pass
'''

def datosPersonale(nombre, sobrenombre, edad, sexo):
    print("Nombre: {}\nSobrenobre: {}\nEdad: {}\nSexo: {}".format(nombre,sobrenombre,edad,sexo))

#datosPersonale("Julio","Rivera",23,True)
datosPersonale(nombre="JUlio", sobrenombre = "Rivera",edad = 23, sexo = True)

