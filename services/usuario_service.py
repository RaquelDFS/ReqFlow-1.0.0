from database.db import inserir_usuario, listar_usuarios, alterar_status_usuario
from models.usuario import Usuario


class UsuarioService:
    CARGOS_VALIDOS = ["analista", "gerente", "cliente", "desenvolvedor", "testador"]

    def cadastrar_usuario(self, nome: str, email: str, senha: str, cargo: str) -> tuple[bool, str]:
        if not nome.strip():
            return False, "O nome não pode estar vazio."

        if not email.strip() or "@" not in email:
            return False, "E-mail inválido."

        if len(senha) < 4:
            return False, "A senha deve ter pelo menos 4 caracteres."

        if cargo not in self.CARGOS_VALIDOS:
            return False, "Cargo inválido."

        inserido = inserir_usuario(nome.strip(), email.strip(), senha, cargo)

        if not inserido:
            return False, "Este e-mail já está cadastrado."

        return True, f"Usuário '{nome}' cadastrado com sucesso."

    def listar_usuarios(self) -> list[Usuario]:
        return listar_usuarios()

    def alternar_status(self, usuario_id: int, status_atual: bool) -> str:

        novo_status = not status_atual
        alterar_status_usuario(usuario_id, novo_status)
        acao = "ativado" if novo_status else "desativado"
        return f"Usuário {acao} com sucesso."