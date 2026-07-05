import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os
from dotenv import load_dotenv
load_dotenv()

# import sys
# # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
# from src.data_preparation import gera_columns, prepara_dados_batismo, concatenando_dados, resultados_anuais
# from src.gera_figuras import gera_figura, gera_figura_atributo, gera_figura_batismo, gera_figura_media, prepara_dados_anuais_plot, prepara_dados_mensais_plot, ComparaDadosAnuais

st.title("Dados do culto")
 