#a = 10
#b = 12
#c = 60

#x = int(input("Digite Un numero: "))

#if(x == a or x == b or x ==c):
#if(x in [10,12,60]):
#if (x in [a, b, c]):
#    print("El numero esta contenido")
#else:
#    print("NO ESTA CONTENIDO")

#--------------------------------------------------------

colores = ["Azul", "Amarilla","Verde"]
while True:
    dColor = input("Digite un color 0 para salir  del programa:")
    if(dColor == '0'):
        break
    if dColor in colores:
        print("Este color se encuentra contenido")
    else:
        print("El color no esta contenido")
print("Fin del programa... Saliendo")