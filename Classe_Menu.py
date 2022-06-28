from Classe_Estoque import *

class Menu:
    def __init__(self):
        estoque_prod = Estoque()

        ##iniciar menu
        while True:
            print('Menu de operações'
                  '\n1 - Cadastrar'
                  '\n2 - Listar todos'
                  '\n3 - Procurar produto'
                  '\n4 - Alterar produto'
                  '\n0 - Sair')
            entrada = input('Informe a operação desejada: ')

            if entrada == '1':
                estoque_prod.Salvar_Cadastro()
            elif entrada == '2':
                estoque_prod.Lista_Produtos()
            elif entrada == '3':
                estoque_prod.Lista_CodP()
            elif entrada == '4':
                estoque_prod.Alterar_Nome()
            elif entrada == '0':
                break
            else:
                print('opção errada!')