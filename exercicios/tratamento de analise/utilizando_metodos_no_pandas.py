import pandas as pd
dados = pd.DataFrame([1, 1, 2, 3, 3, 3, 4, 4], columns = ['X']) 
dados.drop_duplicates(inplace = True)
print(dados)
