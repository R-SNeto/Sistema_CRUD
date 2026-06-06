# Arraial Modas Teresina — Sistema de Gerenciamento de Estoque

Sistema CRUD de linha de comando desenvolvido em Python para gerenciamento de produtos e estoque de uma loja de moda.

---

## Funcionalidades

- **Gerenciamento de Produtos**
  - Adicionar novos produtos (nome, quantidade inicial e valor de venda)
  - Listar todos os produtos cadastrados
  - Modificar nome ou valor de venda de um produto
  - Remover produtos do estoque

- **Gerenciamento de Estoque**
  - Registrar entrada de produtos no estoque
  - Registrar saída de produtos do estoque

---

## Estrutura do Projeto

```
Sistema_CRUD/
│
├── main.py                     # Ponto de entrada, menu principal
├── crud.py                     # Operações de Create, Read, Update e Delete
├── dados.py                    # Armazenamento dos dados 
├── utils.py                    # Validações e funções utilitárias
├── menu_gerenciar_produtos.py  # Interface de gerenciamento de produtos
└── menu_gerenciar_estoque.py   # Interface de gerenciamento de estoque
```

---

## Como executar

**Pré-requisitos:** Python 3.x instalado

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/Sistema_CRUD.git

# Acesse a pasta do projeto
cd Sistema_CRUD

# Execute o sistema
python main.py
```

## Tecnologias

- Python 3.x
