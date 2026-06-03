import streamlit as st
from config import nome_programa, versao_programa
from database.db import buscar_usuario_por_email

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
        usuario = buscar_usuario_por_email(email)

        if usuario is None:
            st.error("E-mail não encontrado.")
        elif not usuario.status:
            st.error("Usuário inativo. Contate o administrador.")
        elif usuario.senha != senha:
            st.error("Senha incorreta.")
        else:
            st.session_state.usuario_logado = usuario
            st.rerun()  

def tela_home(usuario):
    st.title(f"Olá, {usuario.nome}!")
    st.markdown(f"**{usuario.cargo}**.")
    st.info("Dashboard")

    if st.button("Sair"):
        st.session_state.usuario_logado = None
        st.rerun()

if st.session_state.usuario_logado is None:
    tela_login()
else:
    tela_home(st.session_state.usuario_logado)