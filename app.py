import streamlit as st

preencher_curriculo = st.Page(
    page = "pages/preencher_curriculo.py", 
    title="Preencher Curriculo")

selecionar_modelo = st.Page(
    page = "pages/selecionar_modelo.py",
    title="Selecionar Modelo")

pg = st.navigation(pages=[preencher_curriculo, selecionar_modelo])

pg.run()

