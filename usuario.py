class Usuario:
    def __init__(self, id=None, nome="", email="", senha="", tipo="", telefone="", cidade="", estado=""):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo = tipo  # cliente ou tecnico
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado
