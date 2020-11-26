import pandas as pd
data = [['Fulano', 12, 7.0, True],
        ['Sicrano', 15, 3.5, False], 
        ['Beltrano', 18, 9.3, True]]
dados = pd.DataFrame(data,columns = ['Aluno', 'Idade', 'Nota', 'Aprovado'])

tipos_de_dados = pd.DataFrame(dados.dtypes, columns=['Tipos de dados']) 
tipos_de_dados.columns.name = 'Variaveis' 
print(tipos_de_dados)