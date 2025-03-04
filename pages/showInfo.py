import streamlit as st
import controller.controllerCliente as ct
import models.Cliente as cliente

def Header():
    st.title("Informações dos Usuários")
    

def Exibir():
    listaDados = ct.MostrarDados(cliente)
    
    for i in listaDados:
        st.subheader(f"Seu Currículo está pronto {i.nome}")
        st.write(f"**NOME:** {i.nome}")
        st.write(f"**TELEFONE:** {i.telefone}")
        st.write(f"**EMAIL:** {i.email}")
        st.write(f"**DATA DE NASCIMENTO:** {i.data}")
        st.write(f"**UNIVERSIDADE:** {i.universidade}")
        st.write(f"**CURSO:** {i.curso}")
        st.write(f"**SEMESTRE:** {i.semestre}")
        st.write(f"**EXPERIENCIA:** {i.experiencia}")
        st.write(f"**DESCRICAO:** {i.descricao}")
        st.write(f"**COMPETENCIA:** {i.competencia}")
        st.write("---------------")

Header()

Exibir()
ct.MostrarDados(cliente)

