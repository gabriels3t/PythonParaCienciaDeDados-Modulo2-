import pandas as pd 
precos = pd.DataFrame([['Feira', 'Cebola', 2.5], 
                        ['Mercado', 'Cebola', 1.99], 
                        ['Supermercado', 'Cebola', 1.69], 
                        ['Feira', 'Tomate', 4], 
                        ['Mercado', 'Tomate', 3.29], 
                        ['Supermercado', 'Tomate', 2.99], 
                        ['Feira', 'Batata', 4.2], 
                        ['Mercado', 'Batata', 3.99], 
                        ['Supermercado', 'Batata', 3.69]], 
                        columns = ['Local', 'Produto', 'Preço'])

produtos = precos.groupby('Produto')
estatisticas = ['mean', 'std', 'min', 'max']
nomes ={
        'mean': 'Média', 'std': 'Desvio Padrão',
        'min': 'Mínimo', 'max': 'Máximo'
        }

print(produtos['Preço'].aggregate(estatisticas).rename(columns = nomes).round(2))


