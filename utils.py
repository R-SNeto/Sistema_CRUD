from dados import dados_estoque

#Validações

#Retorna ao menu caso o usuário digite '0'
def sair_funcao(variavel):
    if variavel == "0":
        return True
    else:
        return False

#Verifica se o nome já está cadastrado. Retorna True caso o nome já exista
def esta_cadastrado (nome):
    if nome in dados_estoque.keys():
        return True
    else:
        return False

#Verifica se o nome é vazio. Retorna True caso esteja vazio
def nome_vazio(nome):
    if nome.strip():
        return False
    else:
        return True

#Verifica se existe caracteres especiais (#, @, %...) no nome. Retorna true caso não tenha e false caso tenha
def caractere_especial(nome):
    auxnome = nome.replace(" ", "")
    return auxnome.isalnum()

#Verifica se o valor passado como parâmetro é positivo. Retorna False caso seja negativo
def numero_positivo(valor):
    if valor >= 0:
        return True
    else:
        return False
    
def valor_maior_que_estoque(nome_produto, qtd_produto):
    if qtd_produto > dados_estoque[nome_produto]['estoque']:
        raise ValueError("Valor digitado maior que o estoque atual")
    
#Processamento de dados

#Processa e valida o nome. Lança uma excessão caso o nome não esteja correto
def processar_nome(nome):
    if esta_cadastrado(nome):
        raise ValueError("Produto já cadastrado")
    
    if not caractere_especial(nome):
        raise ValueError("Nome do produto não pode conter caracteres especiais (#, @...)")
    
    if nome_vazio(nome):
        raise ValueError("Insira um nome válido")

#Processa e valida o valor. Lança uma excessão caso seja um valor negativo
def processar_valor(valor):
    if not numero_positivo(valor):
        raise ValueError("Números negativos não são aceitos")
    
#Utilitários

#Confirma uma ação do usuário
def sim_nao(resposta):
    if resposta.lower() == "y":
        return True
    elif resposta.lower() == "n":
        return False
    else:
        raise ValueError("Por favor, seleciona 'y' ou 'n'!")