import os
os.system('cls')

m100 = int(0)
m50 = int(0)
m10 = int(0) 
m5 = int(0)
m1 = int(0) 

print('CAIXA DE MERRECA by: Agui')
print('-----------------')
print(' Saldo: Infinito ')
print('-----------------')
print('')
qtd = int(input('Quanto você deseja sacar? \n'))


while qtd != 0:
    if qtd >= 100:
        m100 = m100 + 1
        qtd = qtd - 100
    elif qtd >= 50:
        m50 = m50 + 1
        qtd = qtd - 50
    elif qtd >= 10:
        m10 = m10 + 1
        qtd = qtd - 10
    elif qtd >= 5:
        m5 = m5 + 1
        qtd = qtd - 5
    else:
        m1 = m1 + 1
        qtd = qtd - 1


os.system('cls')
print('CAIXA DE MERRECA by: Agui')
print('-----------------')
print(' Saldo: Infinito ')
print('-----------------')
print('')
print('Quantidade sacada:')
print('')
print(m100,' cédulas de M$ 100')
print(m50,' cédulas de M$ 50')
print(m10,' cédulas de M$ 10')
print(m5,' cédulas de M$ 5')
print(m1,' cédulas de M$ 1')




