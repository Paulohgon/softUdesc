import string


class questionario:
    def __init__(self,qtdperg,nome):
        self.qtdperg = qtdperg
        self.nome = nome
    def addpergunta(self,enunciado,resposta):
        self.pergunta = perguntas(enunciado,resposta)
    def setquestionario(self,qtdperg,nome):
        return questionario(qtdperg,nome)
    def getquestionario(self):
        return self.qtdperg,self.nome
class perguntas:
    def __init__(self,enunciado,pontos):
        self.enunciado = enunciado
        self.pontos = pontos
    def addresposta(self,texto):
        self.newresposta = resposta({self.enunciado:True},texto)
    def getresposta(self,enunciado):
        self.respostaa = resposta.getrespostacerta(enunciado)
        print(self.respostaa)
    def getpontos(self):
        return self.pontos
    def getenunciado(self):
        return self.enunciado
    def setperguntas(self,enunciado,pontos):
        return perguntas(enunciado,pontos)

    
class resposta:
    def __init__(self,certo,texto):
        self.texto = texto
        self.certo = certo
    def getrespostacerta(self,enunciado):
        for pergunta in self.certo:
            if pergunta == enunciado:
                if self.certo[pergunta]==True:
                    return self.texto
    def setresposta(self,certo,texto):
        return resposta(texto,certo)
    def getresposta(self):
        return self.texto,self.certo