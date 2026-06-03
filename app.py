import streamlit as st
from config import nome_programa, versao_programa
from database.schema import inicializar_banco
from views import login, gerente, analista, home

inicializar_banco()

st.set_page_config(
    page_title=f"{nome_programa} {versao_programa}",
    page_icon="🎯",
)

if "usuario_logado" not in st.session_state:
    st.session_state.usuario_logado = None

usuario = st.session_state.usuario_logado

if usuario is None:
    login.exibir(usuario)
elif usuario.cargo == "gerente":
    gerente.exibir(usuario)
elif usuario.cargo == "analista":
    analista.exibir(usuario)
else:
    home.exibir(usuario)