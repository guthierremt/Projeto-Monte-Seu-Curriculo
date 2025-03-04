import streamlit as st
import controller.controllerCliente as ct
import models.Cliente as cliente
from makePdf import gerar_pdf

def criar_curriculo():
    st.title("Criando meu Currículo")

    if "selected_model" not in st.session_state:
        st.warning("Selecione um modelo na página principal.")
        return

    modelo = st.session_state["selected_model"]

    if modelo == "Modelo 1":
        with st.form("my form"):
            st.write("Dados Pessoais")
            yourName = st.text_input('Nome Completo')
            yourFone = st.text_input('Telefone', max_chars=11)
            yourEmail = st.text_input('Email', max_chars=40)
            yourDate = st.text_input('Data de Nascimento', max_chars=10)
            st.divider()
            st.write("Formação Acadêmica")
            yourUniversity = st.text_input('Instituição de Ensino', max_chars=50)
            yourCourse = st.text_input('Curso', max_chars=30)
            yourSemester = st.text_input('Semestre Atual', max_chars=15)
            st.divider()
            yourExperience = st.text_area('Experiencia Profissional', max_chars=400)
            yourDescription = st.text_area('Descrição Pessoal', max_chars=260)
            yourCompetence = st.text_area('Competências', max_chars=200)
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

            pdf_output = gerar_pdf(cliente)

            st.download_button(
                label="Baixar Currículo em PDF",
                data=pdf_output,
                file_name="curriculo.pdf",
                mime="application/pdf"
            )
            
            st.success("Dados enviados com Sucesso!")
            
            
    if modelo == "Modelo 2":
        with st.form("my form"):
            st.write("Dados Pessoais")
            yourName = st.text_input('Nome')
            yourFone = st.text_input('Telefone', max_chars=11)
            yourEmail = st.text_input('Email', max_chars=40)
            yourDate = st.text_input('Data de Nascimento', max_chars=10)
            st.divider()
            st.write("Formação Acadêmica")
            yourUniversity = st.text_input('Instituição de Ensino', max_chars=50)
            yourCourse = st.text_input('Curso', max_chars=30)
            yourSemester = st.text_input('Semestre Atual', max_chars=15)
            st.divider()
            yourExperience = st.text_area('Experiencia Profissional', max_chars=400)
            yourDescription = st.text_area('Descrição Pessoal', max_chars=260)
            yourCompetence = st.text_area('Competências', max_chars=200)
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

            pdf_output = gerar_pdf(cliente)

            st.download_button(
                label="Baixar Currículo em PDF",
                data=pdf_output,
                file_name="curriculo.pdf",
                mime="application/pdf"
            )
            
            st.success("Dados enviados com Sucesso!")
            
    if modelo == "Modelo 3":
        with st.form("my form"):
            st.write("Dados Pessoais")
            yourName = st.text_input('Nome')
            yourFone = st.text_input('Telefone', max_chars=11)
            yourEmail = st.text_input('Email', max_chars=40)
            yourDate = st.text_input('Data de Nascimento', max_chars=10)
            st.divider()
            st.write("Formação Acadêmica")
            yourUniversity = st.text_input('Instituição de Ensino', max_chars=50)
            yourCourse = st.text_input('Curso', max_chars=30)
            yourSemester = st.text_input('Semestre Atual', max_chars=15)
            st.divider()
            yourExperience = st.text_area('Experiencia Profissional', max_chars=400)
            yourDescription = st.text_area('Descrição Pessoal', max_chars=260)
            yourCompetence = st.text_area('Competências', max_chars=200)
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

            pdf_output = gerar_pdf(cliente)

            st.download_button(
                label="Baixar Currículo em PDF",
                data=pdf_output,
                file_name="curriculo.pdf",
                mime="application/pdf"
            )
            
            st.success("Dados enviados com Sucesso!")

if __name__ == "__main__":
    criar_curriculo()
