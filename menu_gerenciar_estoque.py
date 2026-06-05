import utils as utils
import crud as crud
import menu_gerenciar_produtos as prod

def menu_gerenciar_estoque():
    while True:
        print("\n    GERENCIAR ESTOQUE   ")
        print("---------------------------")
        
        prod.listar_produtos()
        
        nome = input("1) Digite o nome do produto que terá seu estoque alterado (0 para sair): ")
        nome = utils.padronizar_nome(nome)
         
        if utils.sair_funcao(nome):
            break
        elif not utils.esta_cadastrado(nome):
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
            
            if opcao == 1:
                qtd_produtos = int(input("2) Quantidade de produtos que será adicionado: "))
                
                utils.processar_valor(qtd_produtos)
                crud.adicionar_qtd_estoque(nome, qtd_produtos)
                
                print("\nEstoque atualizado com sucesso!")
            elif opcao == 2:
                qtd_produtos = int(input("2) Quantidade de produtos que será removido: "))
                
                utils.processar_valor(qtd_produtos)
                crud.remover_qtd_estoque(nome, qtd_produtos)
                
                print("\nEstoque atualizado com sucesso!") 
            elif opcao == 3:
                print("\nRetornando ao menu...")
                break
            else:
                raise ValueError("Insira uma opção válida")
        
        except ValueError as e:
            print(f"Erro: {e}")