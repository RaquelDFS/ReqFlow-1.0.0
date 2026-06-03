import streamlit as st
from config import nome_programa, versao_programa
from services.autenticacao import AutenticacaoService

autenticacao = AutenticacaoService()
st.set_page_config(
    page_title="ReqFlow 1.0.0",
    page_icon="🎯",
)

if "usuario_logado" not in st.session_state:
    st.session_state.usuario_logado = None
#session_state!!


def tela_login():
    st.title(f"Bem-vindo ao {nome_programa}")
    st.markdown(f"`versão: {versao_programa}`")

    email = st.text_input("E-mail")
    senha = st.text_input("Senha", type="password")
    
    if st.button("Entrar"):
        resultado = autenticacao.fazer_login(email, senha)
        if resultado.sucesso:
            st.session_state.usuario_logado = resultado.usuario
            st.rerun()
        else:
            st.error(resultado.mensagem)

def tela_home(usuario):
    st.title(f"Olá, {usuario.nome}!")
    st.markdown(f"**`{usuario.cargo}`**")
    st.info("Dashboard")

    if st.button("Sair"):
        st.session_state.usuario_logado = None
        st.rerun()

if st.session_state.usuario_logado is None:
    tela_login()
else:
    tela_home(st.session_state.usuario_logado)