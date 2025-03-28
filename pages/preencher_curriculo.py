import streamlit as st
import controller.controllerCliente as ct
from models.Cliente import Cliente
from gerarPDF import gerarModelo1, gerarModelo2, gerarModelo3


def gerarCampos(modelo):
    if modelo == "Modelo 1":
        return {
            "yourName": st.text_input('Nome Completo'),
            "yourFone": st.text_input('Telefone', max_chars=15, placeholder='(99) 9 9999-9999'),
            "yourEmail": st.text_input('Email', max_chars=40),
            "yourAdress": st.text_input('Endereço', max_chars=100, placeholder='Rua Bandeirante - 1990'),
            "formation": st.header("Formação Acadêmica"),
            "yourUniversity": st.text_input('Instituição de Ensino', max_chars=50),
            "yourCourse": st.text_input('Curso', max_chars=30),
            "conclusionUniversity": st.text_input('Ano de Conclusão', max_chars=30, placeholder='De 2020 até 2021'),
            "formationInfo": st.text_area('Participação em projetos', max_chars=200),
            "profission": st.header("Experiência Profissional"),
            "yourTitle": st.text_input('Título Profissional', max_chars=30, placeholder='EX: Analista de Sistemas'),
            "company": st.text_input('Empresa', max_chars=50),
            "yourFunction": st.text_input('Seu cargo na empresa', max_chars=40),
            "conclusionCompany": st.text_input('Tempo de trabalho', max_chars=50, placeholder='De 2020 até 2021'),
            "descriptionAtv": st.text_area('Descrição da Atividade na empresa', max_chars=200),
            "infoComp": st.text_input('Imformações Complementares', max_chars=50),
            "especialization": st.text_area('Especialização', max_chars=250),
            "infoPerson": st.text_area('Informação Pessoal', max_chars=260),
            "interPerson": st.text_area('Interesse Pessoal', max_chars=200),
            "languages": st.text_input('Idiomas', max_chars=50),
        }
    elif modelo == "Modelo 2":
        return {
            "yourName": st.text_input('Nome Completo'),
            "yourFone": st.text_input('Telefone', max_chars=15, placeholder='(99) 9 9999-9999'),
            "yourEmail": st.text_input('Email', max_chars=40),
            "yourAdress": st.text_input('Endereço', max_chars=100, placeholder='Rua Bandeirante - 1990'),
            "yourObjective": st.text_area('Objetivos', max_chars=250),
            "formation": st.header("Formação Acadêmica"),
            "yourUniversity": st.text_input('Instituição de Ensino', max_chars=50),
            "yourCourse": st.text_input('Curso', max_chars=30),
            "conclusionUniversity": st.text_input('Ano de Conclusão', max_chars=30, placeholder='De 2020 até 2021'),
            "profission": st.header("Experiência Profissional"),
            "yourTitle": st.text_input('Título Profissional', max_chars=30),
            "yourFunction": st.text_input('Seu cargo na empresa', max_chars=40),
            "company": st.text_input('Empresa', max_chars=50),
            "conclusionCompany": st.text_input('Tempo de trabalho', max_chars=50, placeholder='De 2020 até 2021'),
            "descriptionAtv": st.text_area('Descrição da Atividade na empresa', max_chars=200),
        }
    
    ## Arrumar gerar PDF MODELO 3
    elif modelo == "Modelo 3":
        return {
            "yourPic": st.file_uploader('Faça o upload da sua foto'),
            "yourName": st.text_input('Nome Completo'),
            "yourFone": st.text_input('Telefone', max_chars=15, placeholder='(99) 9 9999-9999'),
            "yourEmail": st.text_input('Email', max_chars=40),
            "yourAdress": st.text_input('Endereço', max_chars=100),
            "yourObjective": st.text_area('Objetivos', max_chars=250),
            "formation": st.header("Formação Acadêmica"),
            "yourUniversity": st.text_input('Instituição de Ensino', max_chars=50),
            "yourCourse": st.text_input('Curso', max_chars=30),
            "conclusionUniversity": st.text_input('Ano de Conclusão', max_chars=30, placeholder='De 2020 até 2021'),
            "profission": st.header("Experiência Profissional"),
            "yourTitle": st.text_input('Título Profissional', max_chars=30),
            "yourFunction": st.text_input('Seu cargo na empresa', max_chars=40),
            "company": st.text_input('Empresa', max_chars=50),
            "conclusionCompany": st.text_input('Tempo de trabalho', max_chars=50, placeholder='De 2020 até 2021'),
            "descriptionAtv": st.text_area('Descrição da Atividade na empresa', max_chars=200),
            "languages": st.text_input('Idiomas', max_chars=50),
            "courseTecn": st.text_area('Cursos Técnicos', max_chars=200),
            "qualificationProfiss": st.text_area('Qualificação Profissional', max_chars=200),
        }

def criarCurriculo():
    st.title("Preencher Currículo")

    if "selected_model" not in st.session_state:
        st.warning("Selecione um modelo na outra página.")
        return

    modelo = st.session_state["selected_model"]

    with st.form('my form'):
        campos = gerarCampos(modelo)
        input_button = st.form_submit_button('Concluir')
        
    if input_button:
        cliente = Cliente()
        if modelo == "Modelo 1":
            cliente.modelo1(**campos)
            pdf_output = gerarModelo1(cliente)
            ct.IncluirUsuario(cliente)
            ct.IncluirInfoProfissional(cliente)
            ct.IncluirFormacaoAcademica(cliente)
            ct.IncluirModelo1(cliente)
        elif modelo == "Modelo 2":
            cliente.modelo2(**campos)
            pdf_output = gerarModelo2(cliente)
        elif modelo == "Modelo 3":
            cliente.modelo3(**campos)
            pdf_output = gerarModelo3(cliente)
    
        

        st.download_button(
            label="Baixar Currículo em PDF",
            data=pdf_output,
            file_name="curriculo.pdf",
            mime="application/pdf"
        )
        
        st.success("Dados enviados com Sucesso!")





criarCurriculo()
