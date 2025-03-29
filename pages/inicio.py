import streamlit as st

from pages import selecionar_modelo as sm

st.set_page_config(
    page_title="Crie seu Curriculo",
    page_icon="😎",
)

def home_page():

    st.title("📄 Crie seu currículo profissional em minutos!")
    st.markdown("""
        Escolha um modelo, preencha seus dados e **baixe um PDF pronto para enviar para vagas!**  
        """)
    
    st.image("images/modelo1.png", caption="Modelos disponíveis", width=600)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("👉 Começar agora", type="primary"):
            st.switch_page("pages/selecionar_modelo.py")

    st.subheader("✨ Dicas para um bom currículo")

    st.html("""
    <div style="background-color: #ffffff; padding: 20px; border: 2px solid #4CAF50; border-radius: 15px;">
        
        <h2 style="color: #000000; font-size: 24px;">1. Seja objetivo e claro</h2>
        <p style="font-size: 18px; color: #333333;">Evite enrolação, mantenha as informações diretas e bem organizadas. Use tópicos para destacar experiências e habilidades importantes.</p>

        <h2 style="color: #000000; font-size: 24px;">2. Personalize para a vaga</h2>
        <p style="font-size: 18px; color: #333333;">Adapte seu currículo para cada vaga. Destaque experiências, competências e realizações que sejam mais relevantes para a posição desejada.</p>

        <h2 style="color: #000000; font-size: 24px;">3. Destaque resultados, não apenas responsabilidades</h2>
        <p style="font-size: 18px; color: #333333;">Mostre como suas ações geraram impacto. Por exemplo, em vez de dizer "Gerenciei uma equipe de vendas", diga "Aumentei as vendas em 25% ao liderar uma equipe de 10 pessoas".</p>

        <h2 style="color: #000000; font-size: 24px;">4. Use um design limpo e profissional</h2>
        <p style="font-size: 18px; color: #333333;">Escolha uma fonte legível e um layout bem estruturado. Evite poluição visual com excesso de cores ou elementos desnecessários.</p>

        <h2 style="color: #000000; font-size: 24px;">5. Inclua palavras-chave do setor</h2>
        <p style="font-size: 18px; color: #333333;">Muitas empresas utilizam sistemas automatizados para triagem de currículos. Verifique a descrição da vaga e incorpore palavras-chave relacionadas às habilidades exigidas.</p>
    </div>
    """)

# No seu app principal:
if "current_page" not in st.session_state:
    st.session_state.current_page = "inicio"

if st.session_state.current_page == "inicio":
    home_page()
