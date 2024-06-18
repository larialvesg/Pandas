import pandas as pd
historico_pedidos = [
    {'ID': 1, 'Nome': 'João', 'Endereço': 'Rua das Flores, 123', 'Produto': 'Camiseta', 'Quantidade': 2, 'Preço':50, 'Data': '01/01/2023'},
    {'ID': 2, 'Nome': 'Mariana', 'Endereço': 'Avenida Central, 456', 'Produto': 'Tênis', 'Quantidade': 1, 'Preço':120, 'Data': '02/01/2023'},
    {'ID': 3, 'Nome': 'Carlos', 'Endereço': 'Praça da Estação, 789', 'Produto': 'Mochila', 'Quantidade': 1, 'Preço':80, 'Data': '03/01/2023'},
    {'ID': 4, 'Nome': 'Joaquim', 'Endereço': 'Alameda dos Anjos, 101', 'Produto': 'Relógio', 'Quantidade': 1, 'Preço':150, 'Data': '04/01/2023'},
]

df = pd.DataFrame(historico_pedidos)
df.to_csv("historico_pedidos.csv", index=False, encoding='utf-8-sig')

df = pd.read_csv("historico_pedidos.csv")
preco =df['Preço']
print(preco)

dados_nova_coluna = preco * 0.2
df['Desconto'] = dados_nova_coluna

# #salvar
df.to_csv("historico_pedidos.csv", index=False)
print(df)


# Criar coluna 2
df = pd.read_csv("historico_pedidos.csv")
preco = df['Preço']
qtd = df['Quantidade']

print(preco)
print(qtd)
#
dados_nova_coluna2 = preco * qtd
df['Valor por item'] = dados_nova_coluna2
# #
df.to_csv("historico_pedidos.csv", index=False, encoding='utf-8-sig')
print(df)