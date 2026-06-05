import menu_gerenciar_produtos as prod
import menu_gerenciar_estoque as estoq
from dados import dados_estoque

def main_menu():
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
                prod.menu_gerenciar_produtos()
            elif opcao == 2:
                if not dados_estoque:
                    print("\nLISTA VAZIA, ADICIONE ALGO ANTES")
                else:
                    estoq.menu_gerenciar_estoque()
            elif opcao == 3:
                print("Saindo...")
                break
            else:
                raise ValueError()
        except ValueError:
            print("\nSeleciona uma opção válida")
                        
                  
main_menu()
