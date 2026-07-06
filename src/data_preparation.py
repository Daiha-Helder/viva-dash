import pandas as pd
import numpy as np

def convert_year(data):
    day, month, year = data.split('/')
    year = "20" + year
    new_date = f"{year}-{month}-{day}"
    return new_date

def concatenando_dados(dados1, dados2):
    
    dados = pd.concat([dados1, dados2])
    dados['Dia'] = pd.to_datetime(dados['Dia'],  format='%d/%m/%Y')
    dados['Dia'] = [dados['Dia'].iloc[i].strftime('%d/%m/%Y') for i in range(dados.shape[0])]
    dados.drop('Carimbo de data/hora', axis=1, inplace=True)

    dados["Dia"] = pd.to_datetime(dados["Dia"], format="%d/%m/%Y")

    dados_dia = (
        dados.groupby("Dia", as_index=False)
        .sum(numeric_only=True)
    )

    dados_dia.insert(1, "Período do culto", "Total")

    dados_dia["Dia"] = dados_dia["Dia"].dt.strftime("%d/%m/%Y")
    dados_dia['Dia'] = pd.to_datetime(dados_dia['Dia'],  format='%d/%m/%Y')

    dados = pd.concat([dados, dados_dia])
    dados.fillna(0, inplace=True)
    dados['Novos decididos'] = dados[['Número de conversões', 
                                      'Número de reconciliações']].sum(axis=1)
    
    dados['Percentual de visitantes'] =  np.round(
        np.divide(
            100 * np.array(dados['Número de visitantes']),
            np.array(dados['Número total de pessoas']),
            out=np.zeros_like(np.array(dados['Número de visitantes']), dtype=float),
            where=np.array(dados['Número total de pessoas']) != 0
        ),
        2
    )

    dados['Percentual de novo decididos'] =  np.round(
        np.divide(
            100 * np.array(dados['Novos decididos']),
            np.array(dados['Número total de pessoas']),
            out=np.zeros_like(np.array(dados['Novos decididos']), dtype=float),
            where=np.array(dados['Número total de pessoas']) != 0
        ),
        2
    )

    dados['Novos decididos'] = dados[['Número de conversões', 'Número de reconciliações']].sum(axis=1)

    dados.sort_values(by='Dia', inplace=True)
    dados.reset_index(drop=True, inplace=True)
   
    
    return dados



# def gera_columns(dados):

#     dados['Dia'] = pd.to_datetime(dados['Dia'], dayfirst=True, errors='coerce')
#     dados['Frequência total'] = dados[['Frequência noite', 
#                                  'Frequência manhã']].sum(axis=1)
    
#     dados['Visitantes total'] = dados[['Visitantes noite', 
#                                  'Visitantes manhã']].sum(axis=1)
    
#     dados['Reconciliações total'] = dados[['Reconciliações noite', 
#                                      'Reconciliações manhã']].sum(axis=1)
    
#     dados['Conversões total'] = dados[['Conversões noite', 
#                                  'Conversões manhã']].sum(axis=1)
    
#     dados['Data'] = dados['Dia'].dt.strftime("%d-%B-%Y")
    
#     dados['Visitantes/Frequência manhã'] = np.round(
#     np.divide(
#         100 * np.array(dados['Visitantes manhã']),
#         np.array(dados['Frequência manhã']),
#         out=np.zeros_like(np.array(dados['Visitantes manhã']), dtype=float),
#         where=np.array(dados['Frequência manhã']) != 0
#     ),
#         3
#     )

#     dados['Visitantes/Frequência noite'] = np.round(
#         np.divide(
#             100 * np.array(dados['Visitantes noite']),
#             np.array(dados['Frequência noite']),
#             out=np.zeros_like(np.array(dados['Visitantes noite']), dtype=float),
#             where=np.array(dados['Frequência noite']) != 0
#         ),
#         3
#     )

#     dados['Visitantes/Frequência total'] = np.round(
#         np.divide(
#             100 * np.array(dados['Visitantes total']),
#             np.array(dados['Frequência total']),
#             out=np.zeros_like(np.array(dados['Visitantes total']), dtype=float),
#             where=np.array(dados['Frequência total']) != 0
#         ),
#         3
#     )

    
#     dados['ND manhã'] = dados[['Conversões manhã', 
#                                'Reconciliações manhã']].sum(axis=1)
    
#     dados['ND noite'] = dados[['Conversões noite', 
#                                'Reconciliações noite']].sum(axis=1)
    
#     dados['ND total'] = dados[['Conversões total', 
#                                'Reconciliações total']].sum(axis=1)
    
#     dados['Ano'] = dados['Dia'].dt.year
     
#     dados['Novos Decididos/Frequência manhã'] = np.round(
#         np.divide(
#             100 * np.array(dados['ND manhã']),
#             np.array(dados['Frequência manhã']),
#             out=np.zeros_like(np.array(dados['ND manhã']), dtype=float),
#             where=np.array(dados['Frequência manhã']) != 0
#         ),
#         3
#     )

#     dados['Novos Decididos/Frequência noite'] = np.round(
#         np.divide(
#             100 * np.array(dados['ND noite']),
#             np.array(dados['Frequência noite']),
#             out=np.zeros_like(np.array(dados['ND noite']), dtype=float),
#             where=np.array(dados['Frequência noite']) != 0
#         ),
#         3
#     )

#     dados['Novos Decididos/Frequência total'] = np.round(
#         np.divide(
#             100 * np.array(dados['ND total']),
#             np.array(dados['Frequência total']),
#             out=np.zeros_like(np.array(dados['ND total']), dtype=float),
#             where=np.array(dados['Frequência total']) != 0
#         ),
#         3
#     )

#     dados.sort_values(by='Dia', inplace=True)
#     dados.reset_index(drop=True, inplace=True)
  
#     return dados

def prepara_dados_batismo(dados):
    dados['Data'] = pd.to_datetime(dados['Data'].apply(convert_year))
    dados['Ano'] = dados['Data'].dt.year

    dados.sort_values(by='Data', inplace=True)
    dados.reset_index(drop=True, inplace=True)

    dados = dados.groupby(dados['Ano']).agg(soma=('Quantidade', 
                                                  'sum')
                                                  ).reset_index()

    dados.sort_values(by='Ano', inplace=True)
    dados.reset_index(drop=True, inplace=True)
    
    return dados

# def concatenando_dados(dados1, dados2):
    
#     dados = pd.concat([dados1, dados2])
#     dados['Dia'] = pd.to_datetime(dados['Dia'],  format='%d/%m/%Y')
#     dados['Dia'] = [dados['Dia'].iloc[i].strftime('%d/%m/%Y') for i in range(dados.shape[0])]
#     dcm = dados[dados['Período do culto']=='Manhã'][['Dia','Número total de pessoas', 
#                                             'Número de visitantes', 
#                                             'Número de conversões', 
#                                             'Número de reconciliações']].copy()

#     dcn = dados[dados['Período do culto']=='Noite'][['Dia','Número total de pessoas', 
#                                             'Número de visitantes', 
#                                             'Número de conversões', 
#                                             'Número de reconciliações']].copy()


#     dcm.rename(columns={'Número total de pessoas':'Frequência manhã',
#                         'Número de visitantes':'Visitantes manhã',
#                         'Número de conversões':'Conversões manhã',
#                         'Número de reconciliações':'Reconciliações manhã'}, inplace=True)

#     dcn.rename(columns={'Número total de pessoas':'Frequência noite',
#                         'Número de visitantes':'Visitantes noite',
#                         'Número de conversões':'Conversões noite',
#                         'Número de reconciliações':'Reconciliações noite'}, inplace=True)
    
#     dados = pd.merge(dcm, dcn, how = 'inner', on=['Dia'])
#     return dados

def resultados_anuais(dados1, dados2):
    dados = dados1[['Conversões total', 'Reconciliações total', 'ND total', 'Ano']].groupby(['Ano']).agg(CT=('Conversões total', 'sum'),
                                                                             RT=('Reconciliações total', 'sum'),
                                                                             NDT=('ND total', 'sum')).reset_index()


    dados = pd.merge(dados, dados2.groupby(['Ano']).agg(NTB=('Quantidade', 'sum')), how='inner', on='Ano')

    dados.rename(columns={'CT':'N° conversões',
                    'RT':'N° reconciliações',
                    'NDT':'N° novos decididos',
                    'NTB':'N° bastimos'}, inplace=True)

    dados['N° conversões/N° batismos'] = np.round(100*dados['N° bastimos']/dados['N° conversões'], 2)

    dados = dados[['Ano',
            'N° novos decididos',
            'N° conversões', 
            'N° reconciliações',
            'N° bastimos',
            'N° conversões/N° batismos']].copy()

    dados['Ano'] = dados['Ano'].astype(str)

    return dados

