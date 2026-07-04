import streamlit as st
from pathlib import Path

st.set_page_config(
    layout="wide"
)

base_dir = Path(__file__).resolve().parent
pg = st.navigation([
    st.Page(str(base_dir/"pages"/"1_dados_do_culto.py"), title="Dados do culto"),
    st.Page(str(base_dir/"pages"/"2_novos_decididos.py"), title="Novos Decididos"),
])

pg.run()


