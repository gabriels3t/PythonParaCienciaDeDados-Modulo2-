# Relatorio e analise 1 
## Importando a base de dados

import pandas as pd 
dados = pd.read_csv('data/aluguel.csv', sep=';')
print(dados.info()) #mosta as informações
print(dados.head(10)) # mostra os 5 primeiros no default, podendo colocar o valor de linhas que voce quer ver

## informações gerais sobre a base de dados
#print(dados.dtypes) #mostrar o tipo de dados object = str
print(pd.DataFrame(dados.dtypes)) # mostrar de uma forma mais bonita 