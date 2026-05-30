from dados import dados_estoque

#Validações

#Retorna ao menu caso o usuário digite '0'
def sair_funcao (variavel):
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

#Verifica se existe caracteres especiais (#, @, %...) no nome. Retorna true caso não tenha e false caso tenha
def caractere_especial (nome):
    auxnome = nome.replace(" ", "")
    return auxnome.isalnum()

#Verifica se o valor passado como parâmetro é positivo. Retorna False caso seja negativo
def numero_positivo (valor):
    if valor >= 0:
        return True
    else:
        return False
    
#Processamento de dados

#Processa e valida o nome. Lança uma excessão caso o nome não esteja correto
def processar_nome (nome):
    if esta_cadastrado(nome):
        raise ValueError("Produto já cadastrado")
    
    if not caractere_especial(nome):
        raise ValueError("Nome do produto não pode conter caracteres especiais (#, @...)")

#Processa e valida o valor. Lança uma excessão caso seja um valor negativo
def processar_valor (valor):
    if not numero_positivo:
        raise ValueError("Números negativos não são aceitos")