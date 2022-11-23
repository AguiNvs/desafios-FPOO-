import os 
import re
os.system('cls')

regra1 = str('[x] A senha deve ter no mínimo 6 caracteres.')
regra2 = str('[x] A senha deve ter no máximo 12 caracteres.')
regra3 = str('[x] A senha deve ter pelo menos 1 letra minúscula entre a-z.')
regra4 = str('[x] A senha deve ter pelo menos 1 letra maiúscula entre A-Z.')
regra5 = str('[x] A senha deve ter pelo menos 1 número entre 0-9.')
regra6 = str('[x] A senha deve ter pelo menos 1 caractere especial: $#@.')


senha = []
z = 0

print("= FK News =")
print('')
print("Cadastre Sua Conta!")
print('')
email = str(input("Insira o seu e-mail: \n"))

while (z != 6):
    os.system('cls')
    print("= FK News =")
    print('')
    print("Cadastre Sua Conta!")
    print("e-mail: ",email)
    print('')
    print(regra1)
    print(regra2)
    print(regra3)
    print(regra4)
    print(regra5)
    print(regra6)
    print('')

#=============== verificação de senha ==========================
    senha = str(input("Insira a sua senha: \n"))

        # ============== verificar a quantidade de caracteres ===========================
    if len(senha) < 6:
        regra1 = ('[x] A senha deve ter no mínimo 6 caracteres.')
    else:
        regra1 = ('[✔] A senha deve ter no mínimo 6 caracteres.')
        z = z + 1
            
    if len(senha) > 12:
        regra2 = ('[x] A senha deve ter no máximo 12 caracteres.')
    else:
        regra2 = ('[✔] A senha deve ter no máximo 12 caracteres.')
        z = z + 1
        
    if re.search('[a-z]',senha) == None:
        regra3 = ('[x] A senha deve ter pelo menos 1 letra minúscula entre A-Z.')
    else:
        regra3 = ('[✔] A senha deve ter pelo menos 1 letra minúscula entre A-Z.')
        z = z + 1
        
    if re.search('[A-Z]',senha) == None:
        regra4 = ('[x] A senha deve ter pelo menos 1 letra maiúscula entre A-Z.')
    else:
        regra4 = ('[✔] A senha deve ter pelo menos 1 letra maiúscula entre A-Z.')
        z = z + 1
        
    if re.search('[0-9]',senha) == None:
        regra5 = ('[x] A senha deve ter pelo menos 1 número entre 0-9.')
    else:
        regra5 = ('[✔] A senha deve ter pelo menos 1 número entre 0-9.')
        z = z + 1

    if re.search('\W',senha) == None:
        regra6 = ('[x] A senha deve ter pelo menos 1 caractere especial: $#@.')           
    else:
        regra6 = ('[✔] A senha deve ter pelo menos 1 caractere especial: $#@.')
        z = z + 1        
        
os.system('cls')

print("= FK News =")
print('')
print("Conta Cadastrada com Sucesso!")
print("e-mail: ",email)
print("senha: ",senha)
print('')

