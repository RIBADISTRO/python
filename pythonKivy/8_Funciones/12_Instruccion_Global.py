#Ambito Global
#Es el ambito de los modulos



#Escopo Global
num=10
print(num)

def funcion():
    global num
    num= 50
    print(num)
funcion()
print(num)