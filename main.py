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
        
        if opcao == 5:
            print("Saindo do sistema...")
            estado_sisema = False
    
        if opcao == 1:
            adicionar_produto ()
        elif opcao == 2:
            listar_produtos ()
        elif opcao == 3:
            modificar_produtos ()
        elif opcao == 4:
            remover_produtos ()
        else:
            print("Opção inválida, tente novamente\n")
            
def adicionar_produto ():
    while True:
        try:
            print("\n     ADICIONAR PRODUTOS  ")
            print("---------------------------")
            nome = input("1) Nome do produto (0 para sair): ")
            
            if sair_funcao (nome):
                break
            
            processar_nome (nome)
            
            quantidade_inicial = int(input("2) Quantidade inicial no estoque: "))
            valor_venda = float(input("3) Insira o valor de venda R$: "))
            
            criar(nome, quantidade_inicial, valor_venda)
            
            print("\nPRODUTO ADICIONADO COM SUCESSO\n")
                
            yn = input("Deseja adicionar outro produto (y/n)? ")
                
            if yn.lower() == "y":
                continue
            elif yn.lower() == "n":
                print("\nRETORNANDO AO MENU")
                break
            else:
                print("\nInsira um valor correto")
                
        except ValueError as e:
            print(f"\nErro: {e}")
            
            
    
def listar_produtos ():
    print("\n       LISTAR PRODUTOS   ")
    print("---------------------------")
    
    print(ler())

def modificar_produtos ():
    while True:
        print("\n     MODIFICAR PRODUTOS  ")
        print("---------------------------")
        nome = input("1) Nome do produto que será modificado (0 para sair): ")
        
        sair_funcao(nome)
        
        if not esta_cadastrado(nome):
            print("Produto não existente")
            continue
        else:
            menu_modificar_produtos (nome)
            break
        

def menu_modificar_produtos (nome):
    while True:
        print("\nSeleciona o que será modificado: ")
        print("---------------------------")
        print("[1] Modificar nome")
        print("[2] Alterar quantidade de produtos no estoque")
        print("[3] Alterar valor de venda")
        print("[4] Sair")
        print("---------------------------")
        opcao = int(input("Escolha uma opção: "))
            
        if opcao == 1:
            novo_nome = input("Escolha o novo nome: ")
            
            if processar_nome(novo_nome):
    
def remover_produtos ():
    print("\n      REMOVER PRODUTOS   ")
    print("---------------------------")
    
main_menu ()
