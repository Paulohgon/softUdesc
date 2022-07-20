class usuario:
    def __init__(self,name,email,sexo,idade):
        self.name = name

        self.email = email
        self.sexo = sexo
        self.idade = idade

class estudante(usuario):
    def __init__(self,name, email, sexo, idade,pontos,historico):
        super().__init__(name, email, sexo, idade)
        self.pontos = pontos
        self.historico=historico
    def addpontos(self,pontos):
        self.pontos = self.pontos+pontos
    def getpontos(self):
        return self.pontos
class professor(usuario):
    def __init__(self,historico,nomeInst):
        self.historico = historico
        self.instituicao=nomeInst
