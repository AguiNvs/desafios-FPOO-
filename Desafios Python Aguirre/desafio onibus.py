from array import array
import os
os.system('cls')

precopassagem = float(100)

acumuladorvlrpassagem = float(0)
contadorpassagem = int(0)

fileira1janela = ["1","2","3","4","5"]
fileira2corredor = ["1","2","3","4","5"]
fileira3corredor = ["1","2","3","4","5"]
fileira4janela = ["1","2","3","4","5"]

#======================================================================Inicio do Programa============================================================================================
print("AGUI-TRANSPORTES!")
print('')
print("Deseja iniciar o serviço?")
inicio = str(input("[s/n]\n"))
os.system('cls')
#================================================================Inicio do While e Tabela de Opções====================================================================================
if(inicio == "s")or(inicio == "S"):
    while(inicio == "s") or (inicio == "S"):
        print("AGUI-TRANSPORTES!")
        print('')
        print("1 - Venda de Passagem")
        print("2 - Ver Poltronas Disponíveis")
        print("3 - Finalizar Vendas")
        print("4 - Encerrar/Sair do Programa")
        print(' ')
        opcao = int(input("Opção: "))
        os.system('cls')
#=======================================================================Opção 01 - Venda de Passagem=======================================================================================
        if(opcao == 1):
            print("AGUI-TRANSPORTES!")
            print('')
            print("1 - Sim")
            print("2 - Não")
            opcaovenda = int(input("Deseja realmente realizar uma compra?\n"))
            os.system('cls')
            
            if(opcaovenda == 1):
            
                nome = str(input("Favor insira o nome do passageiro:\n"))  #===== Nome do Passageiro
                os.system('cls')
            
                print("AGUI-TRANSPORTES!")
                print('')
                print("Passageiro:",nome)
                print('')
                print("(Passageiros de 5 anos ou menos, e 65 anos ou mais, recebem um desconto de 50%)")
                print('')
                idade = int(input("Por favor insira a idade do passageiro:\n"))  #==== Idade do Passageiro
                os.system('cls')
            
                print("AGUI-TRANSPORTES!")
                print('')
                print("Passageiro:",nome)
                print("Idade do Passageiro:",idade)
                print('')
            
                if (idade <= 5) or (idade >= 65):   #==== Desconto Aplicado com Base na Idade do Passageiro
                    precopassagem = (0.5 * precopassagem)
                    print("Desconto de 50% Aplicado!")

                print("Cadeiras Disponíveis:")
                print('') 
                print("Fileira 01 - Janela Esquerda: ",fileira1janela)
                print("Fileira 02 - Corredor Esquerdo: ",fileira2corredor)
                print("Fileira 03 - Corredor Direito: ",fileira3corredor)
                print("Fileira 04 - Janela Direita:",fileira4janela)
                print('')
                print("1 - Janela Esquerda")
                print("2 - Corredor Esquerdo")
                print("3 - Corredor Direito")
                print("4 - Janela Direita")
                print('')
                escolhafileira = int(input("Escolha sua fileira:\n"))
                os.system('cls')
                
                print("AGUI-TRANSPORTES!")
                print('')
                print("Passageiro:",nome)
                print("Idade do Passageiro:",idade)
                print('')
                print("Cadeiras Disponíveis:")
                print('') 
                print("Fileira 01 - Janela Esquerda: ",fileira1janela)
                print("Fileira 02 - Corredor Esquerdo: ",fileira2corredor)
                print("Fileira 03 - Corredor Direito: ",fileira3corredor)
                print("Fileira 04 - Janela Direita:",fileira4janela)
                print('')
                print("Fileira Selecionada:",escolhafileira)
                print('')
                escolhacadeira = int(input("Escolha sua cadeira:\n"))
                os.system('cls')                
                
                
                #================= INSERÇÃO DE DADOS FILEIRA 01 =================================#
                if(escolhafileira == 1) and (escolhacadeira == 1) and (fileira1janela[0] == "1"):
                    acumuladorvlrpassagem = (acumuladorvlrpassagem + precopassagem)
                    contadorpassagem = (contadorpassagem + 1)
                    fileira1janela.insert(0,nome)
                    del fileira1janela[1]
                elif(escolhafileira == 1) and (escolhacadeira == 2) and (fileira1janela[1] == "2"):
                    acumuladorvlrpassagem = (acumuladorvlrpassagem + precopassagem)
                    contadorpassagem = (contadorpassagem + 1)
                    fileira1janela.insert(1,nome)
                    del fileira1janela[2]
                elif(escolhafileira == 1) and (escolhacadeira == 3) and (fileira1janela[2] == "3"):
                    acumuladorvlrpassagem = (acumuladorvlrpassagem + precopassagem)
                    contadorpassagem = (contadorpassagem + 1)
                    fileira1janela.insert(2,nome)
                    del fileira1janela[3]
                elif(escolhafileira == 1) and (escolhacadeira == 4) and (fileira1janela[3] == "4"):
                    acumuladorvlrpassagem = (acumuladorvlrpassagem + precopassagem)
                    contadorpassagem = (contadorpassagem + 1)
                    fileira1janela.insert(3,nome)
                    del fileira1janela[4]
                elif(escolhafileira == 1) and (escolhacadeira == 5) and (fileira1janela[4] == "5"):
                    acumuladorvlrpassagem = (acumuladorvlrpassagem + precopassagem)
                    contadorpassagem = (contadorpassagem + 1)
                    fileira1janela.insert(4,nome)
                    del fileira1janela[5]
                #================= INSERÇÃO DE DADOS FILEIRA 02 ===================================#    
                elif(escolhafileira == 2) and (escolhacadeira == 1) and (fileira2corredor[0] == "1"):
                    acumuladorvlrpassagem = (acumuladorvlrpassagem + precopassagem)
                    contadorpassagem = (contadorpassagem + 1)
                    fileira2corredor.insert(0,nome)
                    del fileira2corredor[1]
                elif(escolhafileira == 2) and (escolhacadeira == 2) and (fileira2corredor[1] == "2"):
                    acumuladorvlrpassagem = (acumuladorvlrpassagem + precopassagem)
                    contadorpassagem = (contadorpassagem + 1)
                    fileira2corredor.insert(1,nome)
                    del fileira2corredor[2]
                elif(escolhafileira == 2) and (escolhacadeira == 3) and (fileira2corredor[2] == "3"):
                    acumuladorvlrpassagem = (acumuladorvlrpassagem + precopassagem)
                    contadorpassagem = (contadorpassagem + 1)
                    fileira2corredor.insert(2,nome)
                    del fileira2corredor[3]
                elif(escolhafileira == 2) and (escolhacadeira == 4) and (fileira2corredor[3] == "4"):
                    acumuladorvlrpassagem = (acumuladorvlrpassagem + precopassagem)
                    contadorpassagem = (contadorpassagem + 1)
                    fileira2corredor.insert(3,nome)
                    del fileira2corredor[4]
                elif(escolhafileira == 2) and (escolhacadeira == 5) and (fileira2corredor[4] == "5"):
                    acumuladorvlrpassagem = (acumuladorvlrpassagem + precopassagem)
                    contadorpassagem = (contadorpassagem + 1)
                    fileira2corredor.insert(4,nome)
                    del fileira2corredor[5]    
                #================= INSERÇÃO DE DADOS FILEIRA 03 ===================================#    
                elif(escolhafileira == 3) and (escolhacadeira == 1) and (fileira3corredor[0] == "1"):
                    acumuladorvlrpassagem = (acumuladorvlrpassagem + precopassagem)
                    contadorpassagem = (contadorpassagem + 1)
                    fileira3corredor.insert(0,nome)
                    del fileira3corredor[1]
                elif(escolhafileira == 3) and (escolhacadeira == 2) and (fileira3corredor[1] == "2"):
                    acumuladorvlrpassagem = (acumuladorvlrpassagem + precopassagem)
                    contadorpassagem = (contadorpassagem + 1)
                    fileira3corredor.insert(1,nome)
                    del fileira3corredor[2]
                elif(escolhafileira == 3) and (escolhacadeira == 3) and (fileira2corredor[2] == "3"):
                    acumuladorvlrpassagem = (acumuladorvlrpassagem + precopassagem)
                    contadorpassagem = (contadorpassagem + 1)
                    fileira3corredor.insert(2,nome)
                    del fileira3corredor[3]
                elif(escolhafileira == 3) and (escolhacadeira == 4) and (fileira2corredor[3] == "4"):
                    acumuladorvlrpassagem = (acumuladorvlrpassagem + precopassagem)
                    contadorpassagem = (contadorpassagem + 1)
                    fileira3corredor.insert(3,nome)
                    del fileira3corredor[4]
                elif(escolhafileira == 3) and (escolhacadeira == 5) and (fileira2corredor[4] == "5"):
                    acumuladorvlrpassagem = (acumuladorvlrpassagem + precopassagem)
                    contadorpassagem = (contadorpassagem + 1)
                    fileira3corredor.insert(4,nome)
                    del fileira3corredor[5]
                #================= INSERÇÃO DE DADOS FILEIRA 04 ==================================#    
                elif(escolhafileira == 4) and (escolhacadeira == 1) and (fileira4janela[0] == "1"):
                    acumuladorvlrpassagem = (acumuladorvlrpassagem + precopassagem)
                    contadorpassagem = (contadorpassagem + 1)
                    fileira4janela.insert(0,nome)
                    del fileira4janela[1]
                elif(escolhafileira == 4) and (escolhacadeira == 2) and (fileira1janela[1] == "2"):
                    acumuladorvlrpassagem = (acumuladorvlrpassagem + precopassagem)
                    contadorpassagem = (contadorpassagem + 1)
                    fileira4janela.insert(1,nome)
                    del fileira4janela[2]
                elif(escolhafileira == 4) and (escolhacadeira == 3) and (fileira1janela[2] == "3"):
                    acumuladorvlrpassagem = (acumuladorvlrpassagem + precopassagem)
                    contadorpassagem = (contadorpassagem + 1)
                    fileira4janela.insert(2,nome)
                    del fileira4janela[3]
                elif(escolhafileira == 4) and (escolhacadeira == 4) and (fileira1janela[3] == "4"):
                    acumuladorvlrpassagem = (acumuladorvlrpassagem + precopassagem)
                    contadorpassagem = (contadorpassagem + 1)
                    fileira4janela.insert(3,nome)
                    del fileira4janela[4]
                elif(escolhafileira == 4) and (escolhacadeira == 5) and (fileira1janela[4] == "5"):
                    acumuladorvlrpassagem = (acumuladorvlrpassagem + precopassagem)
                    contadorpassagem = (contadorpassagem + 1)
                    fileira4janela.insert(4,nome)
                    del fileira4janela[5]    
                #===================== CASO A CADEIRA SELECIONADA JÁ ESTEJA OCUPADA======================#        
                else:
                    os.system('cls')
                    print("Cadeira já ocupada!")
                    print("Insira novamente seus dados")
                    print('')
#================================================================Opção 02 - Cadeiras Disponíveis======================================================================================            
        elif(opcao == 2):
            print("AGUI-TRANSPORTES!")
            print('')
            print("Cadeiras Disponíveis:")
            print('')      
            print("Fileira 01 - Janela Esquerda: ",fileira1janela)
            print('')
            print("Fileira 02 - Corredor Esquerdo: ",fileira2corredor)
            print('')
            print("Fileira 03 - Corredor Direito: ",fileira3corredor)
            print('')
            print("Fileira 04 - Janela Direita:",fileira4janela)
            print('')
#==========================================================================================================================================================================================                
        elif(opcao == 3):
            if (contadorpassagem >= 10):
                inicio = "n"
                print("AGUI-TRANSPORTES")
                print('')
                print("Quantidade de Assentos Ocupados: ",contadorpassagem)
                print('')
                print("Valor Faturado: R$",acumuladorvlrpassagem)
                print('')
            elif (contadorpassagem <=9):
                inicio = "n"
                print("AGUI-TRANSPORTES!")
                print('')
                print("A Viagem foi cancelada!")
                print('')
                print("A Viagem não atingiu o minimo de 50% dos assentos ocupados.")  
                print('')
        
        elif(opcao == 4):
            inicio = "n"
            print("Fim do Programa.")
        
        else:
            inicio = "s"      
else:
    
    os.system('cls')
    print("Fim do Programa.")