from sala import sala
class usuario:
    def __init__(self,name,email,sexo,idade):
        self.name = name

        self.email = email
        self.sexo = sexo
        self.idade = idade

class estudante(usuario):
    def __init__(self,name, email, sexo, idade):
        super().__init__(name, email, sexo, idade)
        self.pontos = 0
        self.historico=[]
    def addpontos(self,pontos):
        self.pontos = self.pontos+pontos
    def getpontos(self):
        return self.pontos
class professor(usuario):
    def __init__(self,name, email, sexo, idade,formacao,nomeInst):
        super().__init__(name, email, sexo, idade)
        self.formacao = formacao
        self.instituicao=nomeInst
        self.salas=[]
    def criasala(self,nomesala):
        novasala = sala(nomesala)
        self.salas.append(novasala)
        return novasala
    def addalunosala(self,nomesala,alunos):
        for sala in self.salas:
            if sala.getnomesala()==nomesala:
                sala.addaluno(alunos)