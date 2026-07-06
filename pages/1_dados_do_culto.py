import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import locale
import os
from dotenv import load_dotenv
load_dotenv()

import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
from src.utils import data_preparation

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
ws, hs = 900*1.5, 400*1.5


st.title("Dados do culto")


dcp = pd.read_csv(os.environ["CULTO_ANTIGO"])
dca = pd.read_csv(os.environ["CULTO"])
df = data_preparation(dca, dcp)


# DateInput
data_inicial = st.sidebar.date_input(
    "Data inicial",
    value=df["Dia"].min().date(),
    format="DD/MM/YYYY"
)

data_final = st.sidebar.date_input(
    "Data final",
    value=df["Dia"].max().date(),
    format="DD/MM/YYYY"
)


periodo = st.sidebar.pills(
    "Período do culto:",
    options=df['Período do culto'].unique(),
    default=df['Período do culto'].unique(),
    selection_mode="multi"
)

df_filtrado = df[
    (df['Dia'] >= pd.to_datetime(data_inicial)) &
    (df['Dia'] <= pd.to_datetime(data_final)) &
    (df['Período do culto'].isin(periodo))
    ]

dados_frequencia = [
        go.Scatter(
            x=df_filtrado[df_filtrado['Período do culto']==periodo]["Dia"],
            y=df_filtrado[df_filtrado['Período do culto']==periodo]["Número total de pessoas"],
            mode="lines+markers+text",
            textposition='top center',
            text=df_filtrado[df_filtrado['Período do culto']==periodo]["Número total de pessoas"],
            name=periodo
        ) for periodo in df_filtrado['Período do culto'].unique()]

figF = go.Figure(dados_frequencia)


figF.update_layout(
    title={
        "text": "Frequência no culto",
        "x": 0.5,
        "xanchor": "center",
        "font": {"size": 34}
    },
    xaxis_title="Data",
    xaxis_tickangle=-45,  
    yaxis_title="Número total de pessoas",
    template="plotly_dark",
    yaxis_rangemode='normal',
    width=ws,
    height=hs,
    hovermode="x unified"
)

col1 = st.columns(1)[0]
with col1:
    st.plotly_chart(figF, use_container_width=True)

st.divider()


dados_visitantes = [
        go.Scatter(
            x=df_filtrado[df_filtrado['Período do culto']==periodo]["Dia"],
            y=df_filtrado[df_filtrado['Período do culto']==periodo]["Número de visitantes"],
            mode="lines+markers+text",
            textposition='top center',
            text=df_filtrado[df_filtrado['Período do culto']==periodo]["Número de visitantes"],
            name=periodo
        ) for periodo in df_filtrado['Período do culto'].unique()]

figV = go.Figure(dados_visitantes)


figV.update_layout(
    title={
        "text": "Visitantes no culto",
        "x": 0.5,
        "xanchor": "center",
        "font": {"size": 34}
    },
    xaxis_title="Data",
    xaxis_tickangle=-45,  
    yaxis_title="Número de visitantes",
    template="plotly_dark",
    yaxis_rangemode='normal',
    width=ws,
    height=hs,
    hovermode="x unified"
)

col2 = st.columns(1)[0]
with col2:
    st.plotly_chart(figV, use_container_width=True)

st.divider()

dados_per_visitantes = [
        go.Scatter(
            x=df_filtrado[df_filtrado['Período do culto']==periodo]["Dia"],
            y=df_filtrado[df_filtrado['Período do culto']==periodo]["Percentual de visitantes"],
            mode="lines+markers+text",
            textposition='top center',
            text=df_filtrado[df_filtrado['Período do culto']==periodo]["Percentual de visitantes"],
            name=periodo
        ) for periodo in df_filtrado['Período do culto'].unique()]

figPV = go.Figure(dados_per_visitantes)


figPV.update_layout(
    title={
        "text": "Percentual de visitantes no culto",
        "x": 0.5,
        "xanchor": "center",
        "font": {"size": 34}
    },
    xaxis_title="Data",
    xaxis_tickangle=-45,  
    yaxis_title="Percentual de visitantes",
    template="plotly_dark",
    yaxis_rangemode='normal',
    width=ws,
    height=hs,
    hovermode="x unified"
)

col3 = st.columns(1)[0]
with col3:
    st.plotly_chart(figPV, use_container_width=True)

st.divider()

dados_per_novos_decididos = [
        go.Scatter(
            x=df_filtrado[df_filtrado['Período do culto']==periodo]["Dia"],
            y=df_filtrado[df_filtrado['Período do culto']==periodo]["Percentual de novos decididos"],
            mode="lines+markers+text",
            textposition='top center',
            text=df_filtrado[df_filtrado['Período do culto']==periodo]["Percentual de novos decididos"],
            name=periodo
        ) for periodo in df_filtrado['Período do culto'].unique()]

figPND = go.Figure(dados_per_novos_decididos)


figPND.update_layout(
    title={
        "text": "Percentual de novos decididos no culto",
        "x": 0.5,
        "xanchor": "center",
        "font": {"size": 34}
    },
    xaxis_title="Data",
    xaxis_tickangle=-45,  
    yaxis_title="Percentual de novos decididos",
    template="plotly_dark",
    yaxis_rangemode='normal',
    width=ws,
    height=hs,
    hovermode="x unified"
)

col4 = st.columns(1)[0]
with col4:
    st.plotly_chart(figPND, use_container_width=True)

st.divider()

dados_carros = [
        go.Scatter(
            x=df_filtrado[df_filtrado['Período do culto']==periodo]["Dia"],
            y=df_filtrado[df_filtrado['Período do culto']==periodo]["Número de carros"],
            mode="lines+markers+text",
            textposition='top center',
            text=df_filtrado[df_filtrado['Período do culto']==periodo]["Número de carros"],
            name=periodo
        ) for periodo in df_filtrado['Período do culto'].unique()]

figPC = go.Figure(dados_carros)


figPC.update_layout(
    title={
        "text": "Número de carros no culto",
        "x": 0.5,
        "xanchor": "center",
        "font": {"size": 34}
    },
    xaxis_title="Data",
    xaxis_tickangle=-45,  
    yaxis_title="Número de carros",
    template="plotly_dark",
    yaxis_rangemode='normal',
    width=ws,
    height=hs,
    hovermode="x unified"
)

col5 = st.columns(1)[0]
with col5:
    st.plotly_chart(figPC, use_container_width=True)
