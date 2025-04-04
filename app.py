import streamlit as st

preencher_curriculo = st.Page(
    page = "pages/preencher_curriculo.py", 
    title="Preencher Curriculo")

selecionar_modelo = st.Page(
    page = "pages/selecionar_modelo.py",
    title="Selecionar Modelo")

inicio = st.Page(
    page = "pages/inicio.py",
    title="Inicio",
    default=True,)

pg = st.navigation(pages=[inicio, preencher_curriculo, selecionar_modelo])

pg.run()

