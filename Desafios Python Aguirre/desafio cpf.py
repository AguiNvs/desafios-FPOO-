import os

os.system('cls')

cpf = []
x = 0
y = 10
z = 0
acumulador1 = int(0)
acumulador2 = int(0)
odigito = int
ndigito = int
resto1 = int
resto2 = int

print("Validador de CPF!")
print('')
print("XXX.XXX.XXX-XX")
print('')
cpfstr = str(input("Insira seu CPF completo: \n"))
os.system('cls')

for x in cpfstr:
    cpf.append(int(x))

        
#bab = ((cpf[0]*10)+(cpf[1]*9)+(cpf[2]*8)+(cpf[3]*7)+(cpf[4]*6)+(cpf[5]*5)+(cpf[6]*4)+(cpf[7]*3)+(cpf[8]*2)) / 11
#restobab = ((cpf[0]*10)+(cpf[1]*9)+(cpf[2]*8)+(cpf[3]*7)+(cpf[4]*6)+(cpf[5]*5)+(cpf[6]*4)+(cpf[7]*3)+(cpf[8]*2)) % 11

while (y > 1):  
    mult = cpf[z] * y
    acumulador1 = acumulador1 + mult
    y = y - 1
    z = z + 1 
resto1 = acumulador1 % 11
print(resto1)

if (resto1 < 2):
    odigito = 0
else:
    odigito = (11-resto1)
    
while (y > 0):
    mult = cpf[z] * y
    acumulador2 = acumulador2 + mult
    z = z + 1
    if (z == 9):
        acumulador2 = (acumulador2 + (resto2 * 2))

resto2 = acumulador2 % 11