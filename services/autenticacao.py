from models.usuario import Usuario
from database.db import buscar_usuario_por_email

class ResultadoLogin:
    def __init__(self, sucesso: bool, mensagem: str, usuario: Usuario | None = None):
        self.sucesso = sucesso
        self.mensagem = mensagem
        self.usuario = usuario

class AutenticacaoService:
    def fazer_login(self, email: str, senha: str) ->ResultadoLogin:
        usuario = buscar_usuario_por_email(email)
        
        if usuario is None:
            return ResultadoLogin(
                sucesso = False,
                mensagem = "Email não encontrado."
            )
        if not usuario.status:
            return ResultadoLogin(
                sucesso = False,
                mensagem = "Usuário inativo."
            )
        if usuario.senha != senha:
            return ResultadoLogin(
                sucesso = False,
                mensagem = "Senha incorreta"
            )
        
        return ResultadoLogin(
            sucesso = True,
            mensagem = f"Olá,{usuario.nome}.",
            usuario = usuario
        )