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

def inserir_usuario(nome: str, email: str, senha: str, cargo: str) -> bool:

    try:
        conexao = sqlite3.connect(CAMINHO_BANCO)
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nome, email, senha, cargo, status) VALUES (?, ?, ?, ?, ?)",
            (nome, email, senha, cargo, 1)
        )
        conexao.commit()
        conexao.close()
        return True
    except sqlite3.IntegrityError:
        return False

def listar_usuarios() -> list:
   
    conexao = sqlite3.connect(CAMINHO_BANCO)
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, email, senha, cargo, status FROM usuarios")
    linhas = cursor.fetchall()
    conexao.close()

    return [
        Usuario(
            id=linha[0],
            nome=linha[1],
            email=linha[2],
            senha=linha[3],
            cargo=linha[4],
            status=bool(linha[5])
        )
        for linha in linhas
    ]

def alterar_status_usuario(usuario_id: int, novo_status: bool) -> None:
    conexao = sqlite3.connect(CAMINHO_BANCO)
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE usuarios SET status = ? WHERE id = ?",
        (int(novo_status), usuario_id)
    )
    conexao.commit()
    conexao.close()