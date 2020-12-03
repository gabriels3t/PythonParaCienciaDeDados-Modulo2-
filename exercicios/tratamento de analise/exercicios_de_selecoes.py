import pandas as pd
alunos = pd.DataFrame({'Nome': ['Ary', 'Cátia', 'Denis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'], 
                        'Sexo': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'], 
                        'Idade': [15, 27, 56, 32, 42, 21, 19, 35], 
                        'Notas': [7.5, 2.5, 5.0, 10, 8.2, 7, 6, 5.6], 
                        'Aprovado': [True, False, False, True, True, True, False, False]}, 
                        columns = ['Nome', 'Idade', 'Sexo', 'Notas', 'Aprovado'])

print('-='*30)
print('DATAFRAME \n')
print(alunos)
print('-='*30)
print('')

#Crie um DataFrame somente com os alunos aprovados.
print('-='*30)
print('Crie um DataFrame somente com os alunos aprovados. \n')
selecao = (alunos['Aprovado'] == True)
aprovados = alunos[selecao]
print(aprovados)
print('-='*30)
print()

# Crie um DataFrame somente com as alunas aprovadas.
print('-='*30)
print('Crie um DataFrame somente com as alunas aprovadas. \n')
selecao = (alunos['Aprovado'] == True) & (alunos['Sexo'] == 'F')
aprovadas = alunos[selecao]
print(aprovadas)
print('-='*30)
print()

# Crie apenas uma visualização dos alunos com idade entre 10 e 20 anos ou com idade maior ou igual a 40 anos.
print('-='*30)
print('Crie apenas uma visualização dos alunos com idade entre 10 e 20 anos ou com idade maior ou igual a 40 anos. \n')

selecao = ((alunos['Idade'] > 10) & (alunos['Idade'] < 20)) | (alunos['Idade'] >= 40)
grupo = alunos[selecao]
print(grupo)
print('-='*30)
print()

# Crie um DataFrame somente com os alunos reprovados e mantenha neste DataFrame apenas as colunas Nome, Sexo e Idade, nesta ordem.
print('-='*30)
print('Crie um DataFrame somente com os alunos reprovados e mantenha neste DataFrame apenas as colunas Nome, Sexo e Idade, nesta ordem. \n')
selecao = (alunos['Aprovado'] == False)
reprovados = alunos.loc[selecao,['Nome','Sexo','Idade']]
# OU
selecao = alunos['Aprovado'] == False
reprovados = alunos[['Nome', 'Sexo', 'Idade']][selecao]
print(reprovados)
print('-='*30)
print()

#Crie uma visualização com os três alunos mais novos.
print('-='*30)
print('Crie uma visualização com os três alunos mais novos. \n')
alunos.sort_values(by = ['Idade'], inplace = True)
print(alunos.iloc[:3])
print('-='*30)
print()


