import streamlit as st
from config import nome_programa, versao_programa

st.set_page_config(
    page_title="ReqFlow 1.0.0",
    page_icon="🎯",

)

st.title(f"Bem Vindo ao {nome_programa}")
st.markdown(f"""`versão: {versao_programa}`""" )

email = st.text_input("Email")
senha = st.text_input("Senha", type="password")
if st.button("Entrar"):  
    st.success(f"Bem-vindo! Você digitou o e-mail: {email} e a senha {senha}")