import plotly.graph_objects as go
import numpy as np
import pandas as pd
from functools import reduce

def gera_figura(dados, 
                _period, 
                ws, 
                hs):

    data = [go.Scatter(x=dados['Data'], 
                         y=dados[f'Frequência {_period}'], 
                         name='Frequência',
                         mode='lines+markers+text', 
                         textposition='top center',
                         text=dados[f'Frequência {_period}']),
              go.Scatter(x=dados['Data'], 
                         y=dados[f'Visitantes {_period}'], 
                         name='Nº de visitantes',
                         mode='lines+markers+text',
                         textposition='top center',
                         text=dados[f'Visitantes {_period}']),     
              go.Scatter(x=dados['Data'], 
                         y=dados[f'Conversões {_period}'], 
                         name='Nº de conversões',
                         mode='lines+markers+text', 
                         textposition='top center',
                         text=dados[f'Conversões {_period}']),    
             go.Scatter(x=dados['Data'], 
                        y=dados[f'Reconciliações {_period}'], 
                        name='Nº de reconciliações',
                        mode='lines+markers+text', 
                        textposition='top center',
                        text=dados[f'Reconciliações {_period}']),                      
                ]
    
    fig = go.Figure(data)
    fig.update_layout(title=f'Gráfico de Frequência: {_period.title()}',
                    xaxis_title='Data',
                    yaxis_title='Número de pessoas',
                    yaxis_rangemode='normal',
                    width=ws,
                    height=hs,
                    template='plotly_dark')

    return fig

def gera_figura_atributo(dados, 
                         atributo, 
                         ws, 
                         hs, 
                         _period, 
                         _colunay='Número de pessoas'):

    data = []
    _ynote = []

    for _per in _period:
        data.append(go.Scatter(x=dados['Data'], 
                            y=dados[f'{atributo} {_per}'], 
                            name=f'{atributo} {_per}',
                            mode='lines+markers+text', 
                            textposition='top center',
                            text=dados[f'{atributo} {_per}']))
        
        _ynote.append(np.mean(dados[f'{atributo} {_per}']))
    
    fig = go.Figure(data)
    fig.update_layout(title=f'Gráfico de {atributo.title()}',
                    xaxis_title='Data',
                    yaxis_title=_colunay,
                    yaxis_rangemode='normal',
                    width=ws,
                    height=hs,
                    template='plotly_dark')

    return fig


def gera_figura_batismo(dados, 
                        x, 
                        y, 
                        periodo, 
                        ws, 
                        hs):

    data = [go.Scatter(x=dados[x], 
                         y=dados[y], 
                         name='Número de pessoas batizadas',
                         mode='lines+markers+text', 
                         textposition='top center',
                         text=dados[y])]
    
    fig = go.Figure(data)
    

    fig.update_layout(title=f'Número de batizados por {periodo}',
                    xaxis_title='Data',
                    yaxis_title='Número de pessoas',
                    yaxis_rangemode='normal',
                    width=ws,
                    height=hs,
                    template='plotly_dark')

    return fig

def gera_figura_media(dados, 
                      titulo, 
                      ws, 
                      hs):
    
    fig = go.Figure(dados)

    fig.update_layout(title=titulo,
                  width=ws,
                  height=hs,
                  template='plotly_dark')
    
    return fig

def prepara_dados_anuais_plot(dados):

    dados_absolutos = [go.Bar(x=dados['Ano'], 
                  y=dados[_col], 
                  name=_col, 
                  text=dados[_col], 
              textposition='auto') for _col in dados.columns[1:dados.shape[1]-1].to_list()]

    dados_percentuais = [go.Bar(x=dados['Ano'], 
                   y=dados['N° conversões/N° batismos'], 
                   name='Ano', 
                   text=dados['N° conversões/N° batismos'], 
                   textposition='auto')]
    
    return dados_absolutos, dados_percentuais

def prepara_dados_mensais_plot(dados):
    dados = dados.copy()
    dados.drop('Data', axis=1, inplace=True)
    dados['Dia'] = [_dia.strftime('%Y-%m-%d') for _dia in dados['Dia']]
    dados['Dia'] = pd.to_datetime(dados['Dia'])
    dados = dados.groupby(pd.Grouper(key='Dia', freq='MS')).mean().reset_index()
    float_colunas = dados.select_dtypes(include=['float64']).columns.tolist()
    dados[float_colunas] = dados[float_colunas].fillna(value=0)
    dados[float_colunas] = np.around(dados[float_colunas], 3)

    dN = dados[['Dia']+[_cls for _cls in dados.columns.tolist() if _cls.endswith('noite') == True]].copy()
    dM = dados[['Dia']+[_cls for _cls in dados.columns.tolist() if _cls.endswith('manhã') == True]].copy()
    dT = dados[['Dia']+[_cls for _cls in dados.columns.tolist() if _cls.endswith('total') == True]].copy()

    dados_frequencia_mensal = [go.Scatter(x=dM['Dia'], y=dM['Frequência manhã'], name='Manhã', text=dM['Frequência manhã'], 
                        mode='lines+markers+text', textposition='top center'),
            go.Scatter(x=dN['Dia'], y=dN['Frequência noite'], name='Noite', text=dN['Frequência noite'],
                        mode='lines+markers+text', textposition='top center'),
            go.Scatter(x=dT['Dia'], y=dT['Frequência total'], name='Total', text=dT['Frequência total'],
                        mode='lines+markers+text', textposition='top center')]


    dados_visitantes_mensais = [go.Scatter(x=dM['Dia'], y=dM['Visitantes manhã'], name='Manhã', text=dM['Visitantes manhã'], 
                        mode='lines+markers+text', textposition='top center'),
            go.Scatter(x=dN['Dia'], y=dN['Visitantes noite'], name='Noite', text=dN['Visitantes noite'],
                        mode='lines+markers+text', textposition='top center'),
            go.Scatter(x=dT['Dia'], y=dT['Visitantes total'], name='Total', text=dT['Visitantes total'],
                        mode='lines+markers+text', textposition='top center')]
    
    dados_media_novos_decididos = [go.Scatter(x=dM['Dia'], y=dM['ND manhã'], name='Manhã', text=dM['ND manhã'], 
                    mode='lines+markers+text', textposition='top center'),
         go.Scatter(x=dN['Dia'], y=dN['ND noite'], name='Noite', text=dN['ND noite'],
                    mode='lines+markers+text', textposition='top center'),
         go.Scatter(x=dT['Dia'], y=dT['ND total'], name='Total', text=dT['ND total'],
                    mode='lines+markers+text', textposition='top center')]
    
    return dados_frequencia_mensal, dados_visitantes_mensais, dados_media_novos_decididos 

class ComparaDadosAnuais():
    
    def __init__(self, dados, colunas):
        self.dados = dados
        self.colunas = colunas
        self.position = ['bottom left', 'top left', 
                         'bottom right', 'top right']
    
    def gera_conjunto_de_dados(self):
        dados_filter = self.dados[self.colunas].copy()
        dados_filter['Ano'] = dados_filter[self.colunas[0]].dt.year

        dfs = []
        for _year in dados_filter['Ano'].unique():
            dados_anos = dados_filter[dados_filter['Ano']==_year].sort_values(by='Dia')
            dados_anos.reset_index(drop=True, inplace=True)
            dados_anos['Dia'] = dados_anos['Dia'].astype(str)
            dados_anos.rename(columns={_cols:_cols + ' ' +str(_year) for _cols in self.colunas+['Ano']}, 
                    inplace=True)
            dados_anos['Id'] = dados_anos.index.tolist()
            # dados_anos['Position' + ' ' +str(_year)] = 0 if _year % 2 == 0 else 1
            dfs.append(dados_anos)

        return dfs, dados_filter
    
    def merge_conjuto_de_dados(self):
        dfs, dados_filter = self.gera_conjunto_de_dados()
        dados_merge = reduce(lambda left, right: pd.merge(left, 
                                                      right, 
                                                      how='inner', 
                                                      on=['Id']), 
                                                      dfs)
        return dados_merge, dados_filter
    
    def dados_de_plot(self, colunas_id, coluna_alvo):
        dados_merge, dados_filter = self.merge_conjuto_de_dados()
        
        dados_compara_anos = [go.Scatter(x=dados_merge[colunas_id], 
                                 y=dados_merge[coluna_alvo+' '+str(_year)], 
                                 text=dados_merge[coluna_alvo+' '+str(_year)].astype(str),
                                  mode='lines+markers+text', 
                                #  mode='lines+markers', 
                                 textposition=self.position[0 if _year % 2 == 0 else 1],
                                 showlegend=False) for _year in dados_filter['Ano'].unique()]

        dados_compara_anos += [go.Scatter(x=dados_merge[colunas_id], 
                                        y=dados_merge[coluna_alvo+' '+str(_year)], 
                                        name=coluna_alvo + ' ' +str(_year), 
                                        text=dados_merge[self.colunas[0]+' '+str(_year)],
                                        mode='lines+markers+text',
                                        # mode='lines+markers', 
                                        textposition=self.position[2 if _year % 2 == 0 else 3]
                                        ) for _year in dados_filter['Ano'].unique()]
        
      
        
        return dados_compara_anos

    def plot_grafico(self, colunas_id, coluna_alvo, ws, hs):
        
        dados_compara_anos = self.dados_de_plot(colunas_id, coluna_alvo)

        fig = go.Figure(dados_compara_anos)

        fig.update_layout(title=f'Comparação anual {coluna_alvo}',
                            xaxis_title=self.colunas[0],
                            yaxis_title=f'{coluna_alvo}',
                            yaxis_rangemode='normal',
                            width=ws,
                            height=hs,
                            template='plotly_dark')
        return fig