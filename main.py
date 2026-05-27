def main_menu ():
    estado_sisema = True
    
    while estado_sisema:
        print("  ARRAIAL MODAS TERESINA   ")
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
    print("     ADICIONAR PRODUTOS    ")
    print("---------------------------")
    
def listar_produtos ():
    print("       LISTAR PRODUTOS     ")
    print("---------------------------")
def modificar_produtos ():
    print("     MODIFICAR PRODUTOS    ")
    print("---------------------------")
def remover_produtos ():
    print("      REMOVER PRODUTOS     ")
    print("---------------------------")
    
main_menu ()
