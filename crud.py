from dados import dados_estoque

def criar (nome_produto, quantidade_produto):
    dados_estoque[nome_produto] = quantidade_produto

def ler ():
    texto = ""
    
    for nome_produto, quantidade_produto in dados_estoque.items():
        texto += f"Produto: {nome_produto} | Estoque: {quantidade_produto}\n"
        
    return texto

def atualizar (nome_produto, nova_quantidade):
    if nome_produto in dados_estoque:
        dados_estoque[nome_produto] = nova_quantidade
        
def deletar (nome_produto):
    if nome_produto in dados_estoque:
        dados_estoque.pop(dados_estoque[nome_produto], -1)