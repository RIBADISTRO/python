#FUNCIONEA ANIDADAS

#declaranto funcion
def func():
    print("func")

    #funcion interna
    def func_Interna():
        print("func_Interna")

    func_Interna()#invovacon de funcion interna
func()#invocacion de funcion externa