import pandas as pd

# ler arquivo excel
df = pd.read_excel('dados.xlsx')
# selecionar apenas as colunas de meses
meses = df.columns[1:]
# criar um novo DataFrame com as informações dos estados
dados_estados = df.loc[1:].reset_index(drop=True)
# renomear a primeira coluna para "ESTADO"
dados_estados = dados_estados.rename(columns={dados_estados.columns[0]: 'ESTADO'})
# salvar informações dos estados em um arquivo CSV
dados_estados.to_csv('dados_estados.csv', index=False)
# criar um novo DataFrame com as informações totais por mês
dados_totais = pd.DataFrame(df.iloc[0, 1:].values, columns=['TOTAL'])
# adicionar coluna de meses ao DataFrame
dados_totais['MES'] = meses
# salvar informações totais por mês em um arquivo CSV
dados_totais.to_csv('dados_totais.csv', index=False)
