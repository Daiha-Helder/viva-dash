import pandas as pd
import numpy as np
import plotly.graph_objects as go



def data_preparation(dados1, dados2):
    
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

    dados['Percentual de novos decididos'] =  np.round(
        np.divide(
            100 * np.array(dados['Novos decididos']),
            np.array(dados['Número total de pessoas']),
            out=np.zeros_like(np.array(dados['Novos decididos']), dtype=float),
            where=np.array(dados['Número total de pessoas']) != 0
        ),
        2
    )

    float_colunas = dados.select_dtypes(include=['float64']).columns.tolist()
    dados[float_colunas] = dados[float_colunas].fillna(value=0)

    dados.sort_values(by='Dia', inplace=True)
    dados.reset_index(drop=True, inplace=True)
   
    
    return dados
