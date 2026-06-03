import sqlite3
from models.usuario import Usuario
from database.schema import CAMINHO_BANCO


def buscar_usuario_por_email(email: str) -> Usuario | None:
    conexao = sqlite3.connect(CAMINHO_BANCO)
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id, nome, email, senha, cargo, status FROM usuarios WHERE email = ?",
        (email,)
    )
    linha = cursor.fetchone()
    conexao.close()

    if linha is None:
        return None

    return Usuario(
        id=linha[0],
        nome=linha[1],
        email=linha[2],
        senha=linha[3],
        cargo=linha[4],
        status=bool(linha[5]) 
    )