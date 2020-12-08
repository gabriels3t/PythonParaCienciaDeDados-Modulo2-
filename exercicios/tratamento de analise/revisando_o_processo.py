import pandas as pd

imoveis = pd.DataFrame([['Apartamento', None, 970, 68], 
                        ['Apartamento', 2000, 878, 112], 
                        ['Casa', 5000, None, 500], 
                        ['Apartamento', None, 1010, 170], 
                        ['Apartamento', 1500, 850, None], 
                        ['Casa', None, None, None], 
                        ['Apartamento', 2000, 878, None], 
                        ['Apartamento', 1550, None, 228], 
                        ['Apartamento', 2500, 880, 195]], 
                        columns = ['Tipo', 'Valor', 'Condominio', 'IPTU'])

# 1) Elimina os registros que não apresentam a variável Valor:
imoveis.dropna(subset=['Valor'],inplace=True)
#2) Elimina os imóveis do tipo Apartamento que não apresentam valor Condominio:
selecao = (imoveis['Tipo'] == 'Apartamento') & (imoveis['Condominio'].isnull())
imoveis = imoveis[~selecao]
# 3) Substitui os valores faltantes que restam nas variáveis Condominio e IPTU por zero:
imoveis = imoveis.fillna({'Condominio': 0, 'IPTU': 0})
# 4) Reconstrói o índice do DataFrame resultante:
imoveis.index = range(imoveis.shape[0])

print(imoveis)