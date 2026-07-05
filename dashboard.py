import streamlit as st

st.set_page_config(
    layout="wide"
)


pg = st.navigation([
    st.Page("pages/1_dados_do_culto.py", title="Dados do culto"),
    st.Page("pages/2_novos_decididos.py", title="Novos Decididos")
])

pg.run()


