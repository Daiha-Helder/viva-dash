import streamlit as st


pg = st.navigation([
    st.Page("pages/1_Dados_dos_encontros.py", title="Analise dos Grupos de Crescimento"),
    st.Page("pages/2_Novos_decididos.py", title="Novos Decididos"),
])

pg.run()


