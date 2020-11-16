"""
INSTRUCION CONTINUE

Es la instrucion que interrumpe la ejecucion
de un unico ciclo

"""
print()
print("Inicion")

i = 0
while (i<10):
    i += 1
    if( i % 2 == 0):
        continue
    if(i>7):
        break
    print(i)
else:
    print("Else")

print("Fin")