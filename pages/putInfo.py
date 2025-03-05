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
            yourName = st.text_input('Nome e ultimo Sobrenome')
            yourFone = st.text_input('Telefone', max_chars=11)
            yourEmail = st.text_input('Email', max_chars=40)
            yourAdress = st.text_input('Endereço', max_chars=100)
            st.divider()
            st.write("Objetivos")
            yourObjective = st.text_area('Quais são seus objetivos ?', max_chars=250)
            st.divider()
            st.write("Formação Acadêmica")
            yourUniversity = st.text_input('Instituição de Ensino', max_chars=50)
            yourCourse = st.text_input('Curso', max_chars=30)
            conclusionUniversity = st.text_input('Ano de Conclusão', max_chars=30)
            formationInfo = st.text_area('Participaçao em projetos', max_chars=200)
            st.divider()
            st.write("Experiência Profissional")
            yourTitle = st.text_input('Seu Titulo', max_chars=30)
            yourFunction = st.text_input('Seu cargo na empresa', max_chars=40)
            company = st.text_input('Empresa', max_chars=50)
            conclusionCompany = st.text_input('Tempo de trabalho', max_chars=50)
            descriptionAtv = st.text_area('Descrição da Atividade', max_chars=200)
            especialization = st.text_area('Especialização', max_chars=250)
            infoPerson = st.text_area('Informação Pessoal', max_chars=260)
            interPerson = st.text_area('Interesse Pessoal', max_chars=200)
            st.divider()
            languages = st.text_input('Idiomas', max_chars=50)
            input_button = st.form_submit_button('Concluir')

        if input_button:
            cliente.modelo1(yourName, yourTitle, yourFone, yourAdress, yourEmail,
            yourObjective, yourUniversity, yourCourse, conclusionUniversity, formationInfo, 
            yourFunction, company, conclusionCompany, descriptionAtv, languages, especialization,
            infoPerson, interPerson)
    
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
            yourName = st.text_input('Nome e ultimo Sobrenome')
            yourFone = st.text_input('Telefone', max_chars=11)
            yourEmail = st.text_input('Email', max_chars=40)
            yourObjective = st.text_input('Objetivos', max_chars=250)
            st.divider()
            st.write("Formação Acadêmica")
            yourUniversity = st.text_input('Instituição de Ensino', max_chars=50)
            yourCourse = st.text_input('Curso', max_chars=30)
            conclusionUniversity = st.text_input('Ano de Conclusão', max_chars=30)
            st.divider()
            yourTitle = st.text_area('Seu Titulo', max_chars=30)
            yourFunction = st.text_area('Seu cargo na empresa', max_chars=40)
            company = st.text_area('Empresa', max_chars=50)
            conclusionCompany = st.text_area('Tempo de trabalho', max_chars=50)
            descriptionAtv = st.text_area('Descrição da Atividade', max_chars=200)
            input_button = st.form_submit_button('Concluir')

        if input_button:
            cliente.modelo2(yourName, yourTitle, yourFone, yourEmail, 
            yourObjective, yourUniversity, yourCourse, conclusionUniversity, 
            yourFunction, company, conclusionCompany, descriptionAtv)

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
            yourName = st.text_input('Nome e ultimo Sobrenome')
            yourFone = st.text_input('Telefone', max_chars=11)
            yourEmail = st.text_input('Email', max_chars=40)
            yourAdress = st.text_input('Endereço', max_chars=100)
            yourObjective = st.text_input('Objetivos', max_chars=250)
            st.divider()
            st.write("Formação Acadêmica")
            yourCourse = st.text_input('Curso', max_chars=30)
            conclusionUniversity = st.text_input('Ano de Conclusão', max_chars=30)
            st.divider()
            yourFunction = st.text_area('Seu cargo na empresa', max_chars=40)
            company = st.text_area('Empresa', max_chars=50)
            conclusionCompany = st.text_area('Tempo de trabalho', max_chars=50)
            descriptionAtv = st.text_area('Descrição da Atividade', max_chars=200)
            languages = st.text_area('Idiomas', max_chars=50)
            courseTecn = st.text_area('Cursos Tecnicos', max_chars=200)
            qualificationProfiss = st.text_area('Qualificação Profissional', max_chars=200)
            input_button = st.form_submit_button('Concluir')

        if input_button:
            cliente.modelo1(yourName, yourFone, yourEmail, yourAdress, 
            yourObjective, yourCourse, conclusionUniversity,
            yourFunction, company, conclusionCompany, descriptionAtv, 
            courseTecn, languages, qualificationProfiss)

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
