import streamlit as st
from services.usuario_service import UsuarioService

usuario_service = UsuarioService()

def exibir(usuario):
    st.title(f"Painel do Gerente — {usuario.nome}")

    aba1, aba2, aba3, aba4 = st.tabs(["Dashboard", "Projetos", "Usuários", "Minha Conta"])

    with aba1:
        st.info("Dashboard — em construção.")

    with aba2:
        st.info("Projetos — em construção.")

    with aba3:
        _aba_usuarios()

    with aba4:
        st.info("Minha Conta — em construção.")

    if st.button("Sair"):
        st.session_state.usuario_logado = None
        st.rerun()


def _aba_usuarios():
    st.subheader("Cadastrar Novo Usuário")

    nome  = st.text_input("Nome")
    email = st.text_input("E-mail", key="email_cadastro")
    senha = st.text_input("Senha", type="password", key="senha_cadastro")
    cargo = st.selectbox("Cargo", ["analista", "gerente", "cliente", "desenvolvedor", "testador"])

    if st.button("Cadastrar"):
        sucesso, mensagem = usuario_service.cadastrar_usuario(nome, email, senha, cargo)
        if sucesso:
            st.success(mensagem)
        else:
            st.error(mensagem)

    st.divider()
    st.subheader("Usuários Cadastrados")

    usuarios = usuario_service.listar_usuarios()

    for u in usuarios:
        col1, col2, col3, col4 = st.columns([3, 2, 2, 2])
        col1.write(u.nome)
        col2.write(u.cargo)
        col3.write("Ativo" if u.status else "Inativo")

        rotulo = "Desativar" if u.status else "Ativar"
        if col4.button(rotulo, key=f"status_{u.id}"):
            mensagem = usuario_service.alternar_status(u.id, u.status)
            st.success(mensagem)
            st.rerun()