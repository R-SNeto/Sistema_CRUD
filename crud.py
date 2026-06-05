import utils as utils
from dados import dados_estoque

def criar_produto (nome_produto, quantidade_produto, valor_venda):
    dados_estoque[nome_produto] = {'estoque' : quantidade_produto, 
                                   'valor' : valor_venda}

def ler_dados_produto ():
    texto = ""
    
    for nome_produto, dados in sorted(dados_estoque.items()):
        texto += f"Produto: {nome_produto} | Estoque: {dados['estoque']} | Preço: {dados['valor']}\n"
        
    return texto

def atualizar_nome_produto (nome_antigo, novo_nome):
    dados_estoque[novo_nome] = dados_estoque.pop(nome_antigo)
    
def atualizar_valor_produto (nome_produto, novo_valor):
    dados_estoque[nome_produto]['valor'] = novo_valor
    
def adicionar_qtd_estoque (nome_produto, qtd_produto):
    dados_estoque[nome_produto]['estoque'] += qtd_produto
    
def remover_qtd_estoque (nome_produto, qtd_produto):
    utils.valor_maior_que_estoque(nome_produto, qtd_produto)
    dados_estoque[nome_produto]['estoque'] -= qtd_produto
        
def deletar_produto (nome_produto):
    dados_estoque.pop(nome_produto)