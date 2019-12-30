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


lista =[10, 20]
def func(a, b):
    print()

func(*lista)
func(10, 20)
func(a=10, b=20)
