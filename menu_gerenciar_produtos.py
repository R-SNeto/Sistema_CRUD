import utils as utils
import crud as crud
from dados import dados_estoque

def menu_gerenciar_produtos():
    estado_sisema = True
    
    while estado_sisema:
        try:
            print("\n  GERENCIAR PRODUTOS")     
            print("---------------------------")
            print("[1] Adicionar produtos ao estoque")
            print("[2] Listar produtos do estoque")
            print("[3] Modificar produtos no estoque")
            print("[4] Remover produtos do estoque")
            print("[5] Retornar ao menu principal")
            print("---------------------------")
            opcao = int(input("Escolha uma opção: "))
            
            if opcao == 1:
                adicionar_produto()
            elif opcao == 2:
                listar_produtos()
            elif opcao == 3:
                modificar_produtos()
            elif opcao == 4:
                remover_produtos()
            elif opcao == 5:
                print("Retornando ao menu princiapl...")
                estado_sisema = False
            else:
                raise ValueError("Insira uma opção válida")
        except ValueError as e:
            print(f"Erro: {e}")
   
   
def adicionar_produto():
    while True:
        try:
            print("\n     ADICIONAR PRODUTOS  ")
            print("---------------------------")
            nome = input("1) Nome do produto (0 para sair): ")
            nome = nome.strip().title()
            
            if utils.sair_funcao (nome):
                break
            
            utils.processar_nome (nome)
            
            quantidade_inicial = int(input("2) Quantidade inicial no estoque: "))
            utils.processar_valor(quantidade_inicial)
            valor_venda = float(input("3) Insira o valor de venda R$: "))
            utils.processar_valor(valor_venda)
            
            crud.criar_produto(nome, quantidade_inicial, valor_venda)
            
            print("\nPRODUTO ADICIONADO COM SUCESSO\n")
                
            yn = input("Deseja adicionar outro produto (y/n)? ")
                
            if utils.sim_nao(yn):
                continue
            elif not utils.sim_nao(yn):
                print("\nIndo para o menu...")
                break
                
        except ValueError as e:
            print(f"\nErro: {e}")     


def listar_produtos():
    print("\n       LISTAR PRODUTOS   ")
    print("---------------------------")
    
    if not dados_estoque:
        print("\nLISTA VAZIA")
    else:
        print(crud.ler_produto())

   
def modificar_produtos():
    while True:
        if not dados_estoque:
            print("\nLISTA VAZIA")
            break
        
        print("\n     MODIFICAR PRODUTOS  ")
        print("---------------------------")
        nome = input("1) Nome do produto que será modificado (0 para sair): ")
        
        if utils.sair_funcao(nome):
            break
        
        if not utils.esta_cadastrado(nome):
            print("Produto não existente")
            continue
        else:
            extensao_modificar_produtos (nome)
            break


def extensao_modificar_produtos(nome):
    while True:
        try:
            print("\nSeleciona o que será modificado: ")
            print("---------------------------")
            print("[1] Modificar nome")
            print("[2] Alterar valor de venda")
            print("[3] Sair")
            print("---------------------------")
            opcao = int(input("\nEscolha uma opção: "))
                
            if opcao == 1:
                novo_nome = input("\nDigite o novo nome: ")
                novo_nome = novo_nome.strip().title()
                
                utils.processar_nome(novo_nome)
                crud.atualizar_nome(nome, novo_nome)
                
                print("\nNome atribuído com SUCESSO!")
                break
            elif opcao == 2:
                novo_valor = float(input("\nDigite o novo valor de venda: "))
                
                utils.processar_valor(novo_valor)
                crud.atualizar_valor(nome, novo_valor)

                print("\nValor atualizado com sucesso!")
                break
            elif opcao == 3:
                break
            
        except ValueError as e:
            print(f"Erro: {e}")


def remover_produtos():
    while True:
        try:
            if not dados_estoque:
                print("\nLISTA VAZIA")
                break
            
            print("\n      REMOVER PRODUTOS   ")
            print("---------------------------")
            nome = input("1) Nome do produto que será deletado (0 para sair): ")
            
            if utils.sair_funcao(nome):
                break
            
            yn = input("2) Você tem CERTEZA disso (y/n)? ")
            
            if utils.sim_nao(yn):
                crud.deletar_produto(nome)
                print("\nProduto deletado com sucesso!")
                break
            elif not utils.sim_nao(yn):
                print("\nRetornando ao menu...")
                break
            
        except ValueError as e:
            print(f"Erro: {e}")        