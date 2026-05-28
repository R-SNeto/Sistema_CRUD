from crud import *
from utils import *

def main_menu ():
    estado_sisema = True
    
    while estado_sisema:
        print("\n  ARRAIAL MODAS TERESINA ")
        print("---------------------------")
        print("[1] Adicionar produtos ao estoque")
        print("[2] Listar produtos do estoque")
        print("[3] Modificar produtos no estoque")
        print("[4] Remover produtos do estoque")
        print("[5] Sair")
        print("---------------------------")
        opcao = int(input("Escolha uma opção: "))
    
        if opcao == 1:
            adicionar_produto ()
        elif opcao == 2:
            listar_produtos ()
        elif opcao == 3:
            modificar_produtos ()
        elif opcao == 4:
            remover_produtos ()
        elif opcao == 5:
            print("Saindo do sistema...")
            estado_sisema = False
        else:
            print("Opção inválida, tente novamente\n")
            
def adicionar_produto ():
    estado_funcao = True
    
    while estado_funcao:
        print("\n     ADICIONAR PRODUTOS  ")
        print("---------------------------")
        nome = input("1) Nome do produto (sem caracteres especiais): ")
        quantidade_inicial = int(input("2) Quantidade inicial no estoque: "))
    
        if processar_nome (nome): 
            criar(nome, quantidade_inicial)
            print("\nPRODUTO ADICIONADO COM SUCESSO\n")
            
            yn = input("Deseja adicionar outro produto (y/n)? ")
            
            if yn.lower() == "y":
                adicionar_produto ()
            elif yn.lower() == "n":
                print("\nRETORNANDO AO MENU")
                main_menu()
            
        else:
            print("\nPRODUTO NÃO FOI CADASTRADO DEVIDO À INCOERÊNCIAS")
        
    
def listar_produtos ():
    print("\n       LISTAR PRODUTOS   ")
    print("---------------------------")
    
    print(ler())

def modificar_produtos ():
    print("\n     MODIFICAR PRODUTOS  ")
    print("---------------------------")
def remover_produtos ():
    print("\n      REMOVER PRODUTOS   ")
    print("---------------------------")
    
main_menu ()
