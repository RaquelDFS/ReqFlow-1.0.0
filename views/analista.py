import streamlit as st

def exibir(usuario):
    st.title(f"Painel do Analista — {usuario.nome}")
    st.info("Projetos — em construção.")

    if st.button("Sair"):
        st.session_state.usuario_logado = None
        st.rerun()