class Usuario:
    def __init__(self, id: int, nome: str, email: str, senha: str, cargo: str, status: bool):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha     
        self.cargo = cargo      
        self.status = status 
