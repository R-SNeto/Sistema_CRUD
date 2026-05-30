from crud import *
from utils import *

def main_menu ():
    while True:
        try:
            print("\n  ARRAIAL MODAS TERESINA ")
            print("---------------------------")
            print("[1] Gerenciamento de produtos")
            print("[2] Gerenciamento de estoque")
            print("[3] Sair")
            print("---------------------------")
            opcao = int(input("Escolha uma opção: "))
            
            if opcao == 1:
                menu_gerenciar_produtos()
            elif opcao == 2:
                if not dados_estoque:
                    print("\nLISTA VAZIA, ADICIONE ALGO ANTES")
                else:
                    menu_gerenciar_estoque()
            elif opcao == 3:
                print("Saindo...")
                break
        except ValueError:
            print("\nSeleciona uma opção válida")
        
def menu_gerenciar_produtos ():
    estado_sisema = True
    
    while estado_sisema:
        try:
            print("\n  GERENCIAR PRODUTOS     ")
            print("---------------------------")
            print("[1] Adicionar produtos ao estoque")
            print("[2] Listar produtos do estoque")
            print("[3] Modificar produtos no estoque")
            print("[4] Remover produtos do estoque")
            print("[5] Retornar ao menu principal")
            print("---------------------------")
            opcao = int(input("Escolha uma opção: "))
            
            if opcao == 5:
                print("Retornando ao menu princiapl...")
                estado_sisema = False
            elif opcao == 1:
                adicionar_produto ()
            elif opcao == 2:
                listar_produtos ()
            elif opcao == 3:
                modificar_produtos ()
            elif opcao == 4:
                remover_produtos ()
            else:
                raise ValueError("Insira uma opção válida")
        except ValueError as e:
            print(f"Erro: {e}")
            
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
            processar_valor(quantidade_inicial)
            valor_venda = float(input("3) Insira o valor de venda R$: "))
            processar_valor(valor_venda)
            
            criar_produto(nome, quantidade_inicial, valor_venda)
            
            print("\nPRODUTO ADICIONADO COM SUCESSO\n")
                
            yn = input("Deseja adicionar outro produto (y/n)? ")
                
            if sim_nao(yn):
                continue
            elif not sim_nao(yn):
                print("\nIndo para o menu...")
                break
                
        except ValueError as e:
            print(f"\nErro: {e}")            
    
def listar_produtos ():
    print("\n       LISTAR PRODUTOS   ")
    print("---------------------------")
    
    if not dados_estoque:
        print("\nLISTA VAZIA")
    else:
        print(ler_produto())

def modificar_produtos ():
    while True:
        if not dados_estoque:
            print("\nLISTA VAZIA")
            break
        
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
        try:
            print("\nSeleciona o que será modificado: ")
            print("---------------------------")
            print("[1] Modificar nome")
            print("[2] Alterar valor de venda")
            print("[3] Sair")
            print("---------------------------")
            opcao = int(input("\nEscolha uma opção: "))
            
            if opcao == 3:
                break
                
            if opcao == 1:
                novo_nome = input("\Digite o novo nome: ")
                
                processar_nome(novo_nome)
                atualizar_nome(nome, novo_nome)
                
                print("\nNome atribuído com SUCESSO!")
                break
            elif opcao == 2:
                novo_valor = float(input("\nDigite o novo valor de venda: "))
                
                processar_valor(novo_valor)
                atualizar_valor(nome, novo_valor)

                print("\nValor atualizado com sucesso!")
                break
            
        except ValueError as e:
            print(f"Erro: {e}")
    
def remover_produtos ():
    while True:
        try:
            if not dados_estoque:
                print("\nLISTA VAZIA")
                break
            
            print("\n      REMOVER PRODUTOS   ")
            print("---------------------------")
            nome = input("1) Nome do produto que será deletado (0 para sair): ")
            
            if sair_funcao(nome):
                break
            
            yn = input("2) Você tem CERTEZA disso (y/n)? ")
            
            if sim_nao(yn):
                deletar_produto(nome)
                print("\nProduto deletado com sucesso!")
                break
            elif not sim_nao(yn):
                print("\nRetornando ao menu...")
                break
            
        except ValueError as e:
            print(f"Erro: {e}")

def menu_gerenciar_estoque ():
    while True:
        print("\n    GERENCIAR ESTOQUE   ")
        print("---------------------------")
        
        listar_produtos()
        
        nome = input("1) Digite o nome do produto que terá seu estoque alterado (0 para sair): ")
         
        if sair_funcao (nome):
            break
        elif not esta_cadastrado(nome):
            print("\nProduto não cadastrado")
        else:
            menu_adicionar_remover(nome)  
                
def menu_adicionar_remover(nome):
    while True:
        try:
            print("---------------------------")
            print("[1] Registrar adição de produtos ao estoque")
            print("[2] Registrar remoção de produtos do estoque")
            print("[3] Sair")
            print("---------------------------")
            opcao = int(input("Escolha uma opção: "))
            
            if opcao == 3:
                print("\nRetornando ao menu...")
                break
            
            if opcao == 1:
                qtd_produtos = int(input("2) Quantidade de produtos que será adicionado: "))
                
                processar_valor(qtd_produtos)
                adicionar_qtd_estoque(nome, qtd_produtos)
                
                print("\nEstoque atualizado com sucesso!")
            elif opcao == 2:
                qtd_produtos = int(input("2) Quantidade de produtos que será removido: "))
                
                processar_valor(qtd_produtos)
                remover_qtd_estoque(nome, qtd_produtos)
                
                print("\nEstoque atualizado com sucesso!")
            else:
                raise ValueError("Insira uma opção válida")
        
        except ValueError as e:
            print(f"Erro: {e}")
                  
main_menu()
