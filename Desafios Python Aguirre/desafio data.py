import os
import re
os.system('cls')

data = []
confirma = int(0)

os.system('cls')

print('Agui.exe o Validador de Dias, Meses, Anos')
print('')
print("Exemplo de Data: XX/XX/XXXX")
datastr = str(input("Insira a data a ser avaliada: \n"))
os.system('cls')

# condicional para evitar erro de digitação
if re.search('[a-zA-Z]',datastr) or len(datastr) != 10:
    print('Inserção de data inválida!')
else:
    # separar a string em um vetor com 3 indices: dia, mês e ano
    for x in datastr.split('/',3):
        data.append(int(x))

# inserção dos valores dos indices nas suas respectivas variáveis
dia = data[0]
mes = data[1]
ano = data[2]

print('Agui.exe o Validador de Dias, Meses, Anos')
print('')
print('Data:',data)
print('')
print('Dia:',dia)
print('Mês:',mes)
print('Ano:',ano)
print('')

# inicio das condicionais para validação da data

    # evitar exageros digitados
if (mes > 12) or (dia > 31):
    confirma = 1

    # evitar inserção errada de quantidade de dias em mês específicos
elif (mes == 2,4,6,9,11) and (dia > 30):
    confirma = 2

    # evitar erro de ano bissexto e dias errados em fevereiro
if (ano%4==0) and (ano%100 !=0) or (ano%400 == 0):
    if (mes == 2) and (dia != 29):
        confirma = 3
else:
    if (mes == 2) and (dia != 28):
        confirma = 4

# confirmação da data, ou amostragem do possível erro
if confirma == 0:
    print('Data Válida')
else:
    print('Data Inválida')
    print('')
    print('Erro:',confirma)