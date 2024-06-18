import pandas as pd
discografia = [
    {'Nome do artista': 'Sorriso Maroto', 'Álbum': 'Sorriso Eu Gosto – No Pagode', 'Ano do Lançamento': 2023, 'Vendas do Álbum': '25 milhões'}
]

df = pd.DataFrame(discografia)
df.to_csv("discografia.csv", index=False, encoding='utf-8-sig')
print(df)