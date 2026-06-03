from models.usuario import Usuario

_usuarios: list[Usuario] = [
    Usuario(
            id=1,
            nome="Raquel",
            email="raquel@reqflow.com", 
            senha="1234", 
            cargo="analista",     
            status=True
            ),

    Usuario(
            id=2,
            nome="Nicole",     
            email="nicole@reqflow.com",  
            senha="1234", 
            cargo="gerente",      
            status=True,
            ),
    Usuario(
            id=3,
            nome="Marina",
            email="marina@reqflow.com",
            senha="1234",
            cargo="cliente",
            status=True
            ),
    Usuario(
            id=4,
            nome="Thiago",
            email="thiago@reqflow.com",
            senha="1234",
            cargo="desenvolvedor",
            status=True
            ),
    Usuario(
            id=5,
            nome="Eduarda",
            email="eduarda@reqflow.com",
            senha="1234",
            cargo="testador",
            status=True
            ),
    Usuario(   
            id=6,
            nome="Matehus",
            email="matheus@reqflow.com",
            senha="1234",
            cargo="analista",
            status=False
            )
]


def buscar_usuario_por_email(email: str) -> Usuario | None:
    for usuario in _usuarios:
        if usuario.email == email:
            return usuario
    return None