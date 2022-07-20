class usuario:
    def __init__(self,name,nome,email,sexo,idade):
        self.name = name
        self.nome = nome
        self.email = email
        self.sexo = sexo
        self.idade = idade

class estudante(usuario):
    def __init__(self,pontos,historico):
        self.pontos = pontos
        self.historico=historico
class professor(usuario):
    def __init__(self,historico,nomeInst):
        self.historico = historico
        self.instituicao=nomeInst