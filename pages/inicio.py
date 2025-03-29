import streamlit as st
import time



def home_page():

    st.set_page_config(
        page_title="Crie seu Curriculo",
        page_icon="😎",
    )


    st.title("📄 Crie seu currículo profissional em minutos!")
    st.markdown("""
        Escolha um modelo, preencha seus dados e **baixe um PDF pronto para enviar para vagas!**  
        """)
    
    tab1, tab2, tab3 = st.tabs(["Modelo Completo", "Modelo Objetivo", "Modelo Moderno"])

    with tab1:
        st.header("Modelo Completo")
        st.markdown("""
        Este é o modelo mais detalhado, com seções como **"Informação Pessoal"**, **"Interesse Pessoal"**, 
        **"Especialização"** e campos extras como **"Participação em projetos"**. 
        Ideal para quem quer destacar múltiplos aspectos da trajetória profissional e pessoal.  
        """)
        st.image("images/modelo1.png", width=500)
    with tab2:
        st.header("Modelo Objetivo")
        st.markdown("""
        Mais enxuto, focado em informações essenciais como **Formação**, **Experiência Profissional** e **Objetivos**.
        Não inclui seções complementares, sendo direto ao ponto 
        – perfeito para candidaturas que exigem clareza e concisão.  
        """)
        st.image("images/modelo2.png", width=500)
    with tab3:
        st.header("Modelo Moderno")
        st.markdown("""
        Inclui campos como **upload de foto** e seções como **"Cursos Técnicos"** e **"Qualificação Profissional"**, 
        que são relevantes para áreas mais dinâmicas (como tecnologia ou design). 
        O visual e a estrutura sugerem um formato mais atualizado.  
        """)
        st.image("images/modelo3.png", width=500)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("👉 Começar agora", type="primary"):
            st.switch_page("pages/selecionar_modelo.py")

    st.subheader("✨ Dicas para um bom currículo")


# No seu app principal:
if "current_page" not in st.session_state:
    st.session_state.current_page = "inicio"

if st.session_state.current_page == "inicio":
    home_page()
