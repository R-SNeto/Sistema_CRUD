from dados import dados_estoque

def criar (nome_produto, quantidade_produto, valor_venda):
    dados_estoque[nome_produto] = {'estoque' : quantidade_produto, 
                                   'valor' : valor_venda}

def ler ():
    texto = ""
    
    for nome_produto, dados in sorted(dados_estoque.items()):
        texto += f"Produto: {nome_produto} | Estoque: {dados['estoque']} | Preço: {dados['valor']}\n"
        
    return texto

def atualizar_nome (nome_antigo, novo_nome):
    dados_estoque[novo_nome] = dados_estoque.pop(nome_antigo)
    
def atualizar_valor (nome_produto, novo_valor):
    dados_estoque[nome_produto]['valor'] = novo_valor
        
def deletar (nome_produto):
    if nome_produto in dados_estoque:
        dados_estoque.pop(dados_estoque[nome_produto], -1)