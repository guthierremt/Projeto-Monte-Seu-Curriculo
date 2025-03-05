import streamlit as st
from pages import putInfo

# Função principal de navegação
def main():
    
    st.markdown(
    """
    <h1 style="text-align: left;">Modelos de Currículo</h1>
    """,
    unsafe_allow_html=True
    )

    st.write("\n")

    st.markdown(
        """
        <h4 style="text-align: left;">Selecione um dos modelos disponíveis</h4>
        """,
        unsafe_allow_html=True
    )
    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.header("Modelo 1")
        st.image("images\modelo1.png")
        if st.button("Selecionar Modelo 1"):
            st.session_state["selected_model"] = "Modelo 1"
            st.query_params = {"page": "Criar Currículo"}
    with col2:
        st.header("Modelo 2")
        st.image("images/modelo2.png")
        if st.button("Selecionar Modelo 2"):
            st.session_state["selected_model"] = "Modelo 2"
            st.query_params = {"page": "Criar Currículo"}
    with col3:
        st.header("Modelo 3")
        st.image("images/modelo3.png")
        if st.button("Selecionar Modelo 3"):
            st.session_state["selected_model"] = "Modelo 3"
            st.query_params = {"page": "Criar Currículo"}

if __name__ == "__main__":
    main()
