import os
os.system('cls')

c = []

print('Agui, o Validador de RG! ')
print('')
rg = str(input("Insira o seu RG para ser validado! \n"))
os.system('cls')

for x in rg.split('.-',1):
    c.append(float(x))

p1 = c[0]
p2 = c[1]
p3 = c[2]
d = c[3]

print('Agui, o Validador de RG! ')
print('')
print('parte 1:',p1)
print('parte 2:',p2)
print('parte 3:',p3)
print('digito:',d)




