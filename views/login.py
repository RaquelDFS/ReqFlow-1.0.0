import streamlit as st
from services.autenticacao import AutenticacaoService

autenticacao = AutenticacaoService()

def exibir(usuario_logado):
    st.title("Bem-vindo ao ReqFlow")

    email = st.text_input("E-mail")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        resultado = autenticacao.fazer_login(email, senha)
        if resultado.sucesso:
            st.session_state.usuario_logado = resultado.usuario
            st.rerun()
        else:
            st.error(resultado.mensagem)