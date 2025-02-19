import streamlit as st
from pages import firstPage
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
        st.image("images\GUthierre teixeira (1).png")
    with col2:
        st.header("Modelo 2")
        st.image("images\modelo2.png")
    with col3:
        st.header("Modelo 3")
        st.image("images\modelo3.png")


if __name__ == "__main__":
    main()
