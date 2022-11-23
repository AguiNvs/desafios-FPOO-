import os
import re

os.system('cls')

print('Agui.exe o Validador de Placa!')
print('')
placa = str(input("Insira a sua placa para ser avaliada: \n"))
os.system('cls')

print('Agui.exe o Validador de Placa!')
print('')
print("Placa: ",placa)
print('')

if len(placa) != 7:
    print('A placa não tem 7 caracteres.')

# Avaliador de Placa viaRegex

elif re.search('[a-z]',placa) or re.search('\s',placa):
    print("Placa Inválida!")

elif re.search('[A-Z]{3}[0-9]{1}\w{1}[0-9]{2}',placa):
    print('Placa Válida!')

else:
    print('Placa Inválida!')
