'''
INSTRUCCION NONLOCAL

Es la instruccion que permite acceder a
miebro no globales y no locales, miebros
contenidos en el ambito externo
'''
#Ambito no global

def funcion():
    var_local=10
    def func_interna():
        nonlocal var_local
        var_local +=1
        print(var_local)
    func_interna()
funcion()
#--------------------------------------------
#global
x= 23
def funcionX():
    global x
    return x
print(funcionX())