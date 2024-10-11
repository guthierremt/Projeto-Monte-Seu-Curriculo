import streamlit as st
import controller.controllerCliente as ct
import models.Cliente as cliente

st.title("Criando meu Currículo")

with st.form("my form"):
    st.write("Dados Pessoais")
    yourName = st.text_input('Nome Completo')
    yourFone = st.text_input('Telefone')
    yourEmail = st.text_input('Email')
    yourDate = st.text_input('Data de Nascimento')
    st.divider()
    st.write("Formação Acadêmica")
    yourUniversity = st.text_input('Instituição de Ensino')
    yourCourse = st.text_input('Curso')
    yourSemester = st.text_input('Semestre Atual')
    st.divider()
    yourExperience = st.text_area('Experiencia Profissional')
    yourDescription = st.text_area('Descrição Pessoal')
    yourCompetence = st.text_area('Competências')
    input_button = st.form_submit_button('Concluir')

if input_button:
    cliente.nome = yourName
    cliente.email = yourEmail
    cliente.data_nascimento = yourDate
    cliente.telefone = yourFone
    cliente.universidade = yourUniversity
    cliente.curso = yourCourse
    cliente.semestre = yourSemester
    cliente.experiencia = yourExperience
    cliente.descricao = yourDescription
    cliente.competencia = yourCompetence

    ct.IncluirDados(cliente)

    
    st.success("Dados enviados com Sucesso !")