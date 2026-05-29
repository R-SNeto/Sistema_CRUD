from dados import dados_estoque

#Validações
def sair_funcao (variavel):
    if variavel == "0":
        return True
    else:
        return False

def esta_cadastrado (nome):
    if nome in dados_estoque.keys():
        return True
    else:
        return False
    
def caractere_especial (nome):
    auxnome = nome.replace(" ", "")
    return auxnome.isalnum()
    
#Processamento de dados
def processar_nome (nome):
    if esta_cadastrado(nome):
        raise ValueError("Produto já cadastrado")
    
    if not caractere_especial(nome):
        raise ValueError("Nome do produto não pode conter caracteres especiais (#, @...)")
    
    
    