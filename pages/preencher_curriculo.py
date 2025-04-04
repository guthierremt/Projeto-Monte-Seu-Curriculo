import streamlit as st
import time
import controller.controllerCliente as ct
from models.Cliente import Cliente
from gerarPDF import generateModel1, generateModel2, generateModel3


# Instanciando o Cliente
cliente = Cliente()

# Função pra geração de cada modelo

def generateFields(model):
    if model == "Modelo 1":
        return {
            "informacao": st.header("Informações Pessoais"),
            "yourName": st.text_input('Nome Completo'),
            "yourFone": st.text_input('Telefone', max_chars=15, placeholder='(99) 9 9999-9999'),
            "yourEmail": st.text_input('Email', max_chars=40),
            "yourAdress": st.text_input('Endereço', max_chars=100, placeholder='Rua Bandeirante - 1990'),
            "yourTitle": st.text_input('Título Profissional', max_chars=30, placeholder='EX: Analista de Sistemas'),
            "formation": st.header("Formação Acadêmica"),
            "yourUniversity": st.text_input('Instituição de Ensino', max_chars=50),
            "yourCourse": st.text_input('Curso', max_chars=30),
            "conclusionUniversity": st.text_input('Ano de Conclusão', max_chars=30, placeholder='De 2020 até 2021'),
            "formationInfo": st.text_area('Participação em projetos', max_chars=200),
            "profission": st.header("Experiência Profissional"),
            "company": st.text_input('Empresa na qual já trabalhou', max_chars=50),
            "yourFunction": st.text_input('Seu cargo na empresa', max_chars=40),
            "conclusionCompany": st.text_input('Tempo de trabalho', max_chars=50, placeholder='De 2020 até 2021'),
            "descriptionAtv": st.text_area('Descrição da Atividade na empresa', max_chars=200),
            "infoComp": st.text_input('Imformações Complementares', max_chars=50),
            "especialization": st.text_area('Possui alguma especialização na área?', max_chars=250),
            "infoPerson": st.text_area('Informação Pessoal', max_chars=260),
            "interPerson": st.text_area('Interesse Pessoal', max_chars=200),
            "languages": st.text_input('Idiomas', max_chars=50),
        }
    elif model == "Modelo 2":
        return {
            "informacao": st.header("Informações Pessoais"),
            "yourName": st.text_input('Nome Completo'),
            "yourFone": st.text_input('Telefone', max_chars=15, placeholder='(99) 9 9999-9999'),
            "yourEmail": st.text_input('Email', max_chars=40),
            "yourAdress": st.text_input('Endereço', max_chars=100, placeholder='Rua Bandeirante - 1990'),
            "yourObjective": st.text_area('Quais são seus objetivos profissionais?', max_chars=250),
            "yourTitle": st.text_input('Título Profissional', max_chars=30),
            "formation": st.header("Formação Acadêmica"),
            "yourUniversity": st.text_input('Instituição de Ensino', max_chars=50),
            "yourCourse": st.text_input('Curso', max_chars=30),
            "conclusionUniversity": st.text_input('Ano de Conclusão', max_chars=30, placeholder='De 2020 até 2021'),
            "profission": st.header("Experiência Profissional"),
            "company": st.text_input('Empresa na qual já trabalhou', max_chars=50),
            "yourFunction": st.text_input('Seu cargo na empresa', max_chars=40),
            "conclusionCompany": st.text_input('Tempo de trabalho', max_chars=50, placeholder='De 2020 até 2021'),
            "descriptionAtv": st.text_area('Descrição da Atividade na empresa', max_chars=200),
        }
    
    elif model == "Modelo 3":
        return {
            "informacao": st.header("Informações Pessoais"),
            "yourPic": st.file_uploader('Faça o upload da sua foto'),
            "yourName": st.text_input('Nome Completo'),
            "yourTitle": st.text_input('Título Profissional', max_chars=30),
            "yourFone": st.text_input('Telefone', max_chars=15, placeholder='(99) 9 9999-9999'),
            "yourEmail": st.text_input('Email', max_chars=40),
            "yourAdress": st.text_input('Endereço', max_chars=100),
            "formation": st.header("Formação Acadêmica"),
            "yourUniversity": st.text_input('Instituição de Ensino', max_chars=50),
            "yourCourse": st.text_input('Curso', max_chars=30),
            "conclusionUniversity": st.text_input('Ano de Conclusão', max_chars=30, placeholder='De 2020 até 2021'),
            "profission": st.header("Experiência Profissional"),
            "company": st.text_input('Empresa na qual já trabalhou', max_chars=50),
            "yourFunction": st.text_input('Seu cargo na empresa', max_chars=40),
            "conclusionCompany": st.text_input('Tempo de trabalho', max_chars=50, placeholder='De 2020 até 2021'),
            "descriptionAtv": st.text_area('Descrição da Atividade na empresa', max_chars=200),
            "formation": st.header("Informações Complementares"),
            "languages": st.text_input('Idiomas', max_chars=50),
            "courseTecn": st.text_area('Cursos Técnicos', max_chars=200),
            "qualificationProfiss": st.text_area('Qualificação Profissional', max_chars=200),
            "yourObjective": st.text_area('Quais são seus objetivos profissionais? ', max_chars=250),
        }

# Função de Criar o curriculo
def createResume():
    st.title("Preencha abaixo com os campos do Currículo")

    if "selected_model" not in st.session_state:
        st.warning("Selecione um modelo primeiro.")
        return

    model = st.session_state["selected_model"]

    with st.form('my form'):
        field = generateFields(model)
        input_button = st.form_submit_button('Concluir')
        
    if input_button:
        if model == "Modelo 1":
            cliente.modelo1(**field)
            pdf_output = generateModel1(cliente)
            ct.IncludeUser(cliente)
            ct.IncludeInfoProfessional(cliente)
            ct.IncludeInfoProfessional(cliente)
            ct.IncludeModel1(cliente)
        elif model == "Modelo 2":
            cliente.modelo2(**field)
            pdf_output = generateModel2(cliente)
            ct.IncludeUser(cliente)
            ct.IncludeInfoProfessional(cliente)
            ct.IncludeInfoProfessional(cliente)
            ct.IncludeModel2(cliente)
        elif model == "Modelo 3":
            cliente.modelo3(**field)
            pdf_output = generateModel3(cliente)
            ct.IncludeUser(cliente)
            ct.IncludeInfoProfessional(cliente)
            ct.IncludeInfoProfessional(cliente)
            ct.IncludeModel3(cliente)  
        
        with st.spinner("Enviando dados..."):
            time.sleep(5)

        st.success("Dados enviados com Sucesso!")

        st.download_button(
            label="Baixar Currículo",
            data=pdf_output,
            file_name="curriculo.pdf",
            mime="application/pdf",
            icon=":material/download:"
        )
        
      


createResume()

