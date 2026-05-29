from dados import dados_estoque

def criar (nome_produto, quantidade_produto, valor_venda):
    dados_estoque[nome_produto] = {'estoque' : quantidade_produto, 
                                   'valor' : valor_venda}

def ler ():
    texto = ""
    
    for nome_produto, dados in dados_estoque.items():
        texto += f"Produto: {nome_produto} | Estoque: {dados['estoque']} | Preço: {dados['valor']}\n"
        
    return texto

def atualizar (nome_produto, nova_quantidade):
    if nome_produto in dados_estoque:
        dados_estoque[nome_produto] = nova_quantidade
        
def deletar (nome_produto):
    if nome_produto in dados_estoque:
        dados_estoque.pop(dados_estoque[nome_produto], -1)