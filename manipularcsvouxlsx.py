import pandas as pd

#Dados de exemplo

dados = {
    "Nome": ["João", "Maria", "Pedro"],
    "Idade":[25, 30, 35],
    "Cidade": ["São Paulo", "Rio de Janeiro", 'Belo Horizonte']
}
#
# #Criar DataFrame
df = pd.DataFrame(dados)

# #Salvar Dataframe como arquivo CSV com enconding utf-8-sig
df.to_csv("meuCSV.csv", index=False, encoding="utf-8-sig")

#ler o arquivo
df = pd.read_csv("meuCSV.csv")

#exibir as primeiras linhas do DataFrame
print(df.head())

#ler o arquivo
df = pd.read_csv("meuCSV.csv", sep=",")

# #ler só uma coluna
cid = df["Cidade"]

#printar
print(cid)


#ler arquivo
df = pd.read_csv("meuCSV.csv", sep=",")

# #Encontrar linha com um objeto específico "Rio de Janeiro"
linha = df[df["Cidade"] == "Rio de Janeiro"]
#
# #mostrar linha
print(linha)

#ler arquivo
df = pd.read_csv("meuCSV.csv", sep=",")

#Adicionar nova coluna
dados_nova_coluna2 = ['Algodão', 'Malha', 'Poliester']
df['Materiais'] = dados_nova_coluna2

#salvar
df.to_csv("meuCSV.csv", index=False)
print(df)
