class sala:
    def __init__(self,nome):
        self.nomesala=nome
        self.listaaluno=[]
    def addaluno(self,alunos):
        for aluno in alunos:
            self.listaaluno.append(aluno)
    def removealuno(self,alunos):
        for aluno in alunos:
            self.listaaluno.remove(aluno)
    def getnomesala(self):
        return self.nomesala
    def getalunos(self):
        return self.listaaluno