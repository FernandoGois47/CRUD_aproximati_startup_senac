class Usuario:
    def __init__(self, id=None, nome="", email="", senha="", tipo="", telefone="", cidade="", estado=""):
        self.id = id
        self.nome = nome
        self.__email = ""
        self.__senha = ""
        self.__telefone = ""
        self.set_email(email)
        self.set_senha(senha)
        self.set_telefone(telefone)
        self.tipo = tipo  # cliente ou tecnico
        self.cidade = cidade
        self.estado = estado

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if not email or "@" not in email:
            raise ValueError("Email deve conter @")
        self.__email = email.strip().lower()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if not value or "@" not in value:
            raise ValueError("Email deve conter @")
        self.__email = value.strip().lower()

    def set_senha(self, senha):
        if not senha or len(senha) < 3:
            raise ValueError("Senha deve ter pelo menos 3 caracteres")
        self.__senha = senha

    def get_senha(self):
        return self.__senha

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, telefone):
        if telefone and len(telefone.strip()) > 0:
            # Remove caracteres não numéricos 
            tel_limpo = ''.join(filter(str.isdigit, telefone))
            if len(tel_limpo) < 10:
                raise ValueError("Telefone deve ter pelo menos 10 dígitos")
            self.__telefone = telefone.strip()
        else:
            self.__telefone = ""
