import streamlit as st

def exibir(usuario):
    st.title(f"Olá, {usuario.nome}!")
    st.markdown(f"Você está logado como **{usuario.cargo}**.")
    st.info("Em breve, o painel correspondente ao seu perfil será exibido aqui.")

    if st.button("Sair"):
        st.session_state.usuario_logado = None
        st.rerun()