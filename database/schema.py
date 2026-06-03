import sqlite3

CAMINHO_BANCO = "reqflow.db"
def inicializar_banco():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            nome    TEXT    NOT NULL,
            email   TEXT    NOT NULL UNIQUE,
            senha   TEXT    NOT NULL,
            cargo   TEXT    NOT NULL,
            status  INTEGER NOT NULL DEFAULT 1
        )
    """)
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    total = cursor.fetchone()[0]
    if total == 0:
        usuarios_iniciais = [
            ("Raquel",   "raquel@reqflow.com",   "1234", "analista",      1),
            ("Carlos",   "carlos@reqflow.com",   "1234", "gerente",       1),
            ("Marina",   "marina@reqflow.com",   "1234", "cliente",       1),
            ("Paulo",    "paulo@reqflow.com",    "1234", "desenvolvedor", 1),
            ("Fernanda", "fernanda@reqflow.com", "1234", "testador",      1),
            ("Inativo",  "inativo@reqflow.com",  "1234", "analista",      0),
            ]
        cursor.executemany(
            "INSERT INTO usuarios (nome, email, senha, cargo, status) VALUES (?, ?, ?, ?, ?)",
            usuarios_iniciais
        )

    conexao.commit()
    conexao.close()