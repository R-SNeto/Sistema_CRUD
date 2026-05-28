from dados import dados_estoque

#Validações
def esta_cadastrado (nome):
    if nome in dados_estoque:
        return True
    else:
        return False
    
def caractere_especial (nome):
    auxnome = nome.replace(" ", "")
    
    return auxnome.isalnum()

def tamanho_minimo (nome):
    if (len(nome) < 3):
        return False
    else:
        return True
    
#Processamento de dados
def processar_nome (nome):
    if (caractere_especial (nome) and tamanho_minimo (nome) and esta_cadastrado (nome)):
        return False
    else:
        return True
