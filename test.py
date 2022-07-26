from question import *
from usuario import *
import pytest
class TestClass:    

    def test1(self):#testa resosta correta
        question = perguntas("qual seu nome ",2)
        respostaa = resposta({"qual seu nome":True},"paulo")


        testa=respostaa.getrespostacerta("qual seu nome")
        print(testa)
        assert  testa== "paulo"

    def test2(self):#testa os pontos 
        respostaa = resposta({"qual a capital da amazonia":True},"ratanaba")
        question = perguntas("qual a capital da amazonia",2)
        aluno = estudante("paulo","paulo@paulo","masculino","30")
        if respostaa.getrespostacerta("qual a capital da amazonia")=='ratanaba':
            maispontos = question.getpontos()
            aluno.addpontos(maispontos)
        assert aluno.getpontos() == 2

    def test3(self):#testa resposta correta da pergunta pelo enunciado
        respostaa = resposta({"qual a capital da amazonia":True},"ratanaba")
        question = perguntas("qual a capital da amazonia",2)

        correta = respostaa.getrespostacerta(question.getenunciado())
        
        assert correta == "ratanaba"

    def test4(self):#cria sala pelo professor
        professor1 = professor("pedro","pedro@pedro.com","masculino",54,"EE","udesc")
        salacriada = professor1.criasala("ECC0001")
        assert salacriada.getnomesala()=="ECC0001"

    def test5(self):#remove um aluno da sala
        professor1 = professor("pedro","pedro@pedro.com","masculino",54,"EE","udesc")
        salacriada = professor1.criasala("ECC0001")
        aluno1 = estudante("brian","brian@brian","masculino",20)
        aluno2 = estudante("bruno","bruno@bruno","masculino",21)
        professor1.addalunosala("ECC0001",[aluno1,aluno2])
        professor1.removealunosala("ECC0001",[aluno1])
        assert len(salacriada.getalunos()) == 1

    def test6(self):#testa se o aluno esta na sala adicionando pelo professor
        professor1 = professor("pedro","pedro@pedro.com","masculino",54,"EE","udesc")
        salacriada = professor1.criasala("ECC0001")
        aluno1 = estudante("brian","brian@brian","masculino",20)
        aluno2 = estudante("bruno","bruno@bruno","masculino",21)
        professor1.addalunosala("ECC0001",[aluno1,aluno2])

        assert len(salacriada.getalunos()) == 2
    def test7(self):#testa se a pontuação dos alunos esta somando
        resposta1 = resposta({"qual a capital da amazonia":True},"ratanaba")
        question1 = perguntas("qual a capital da amazonia",2)
        question2 = perguntas("qual a capital de rondonia",5)
        resposta2 = resposta({"qual a capital de rondonia":True},"porto velho")
        aluno = estudante("paulo","paulo@paulo","masculo","30")
        aluno2 = estudante("braia","braia@braia","homi",30)
        if resposta1.getrespostacerta("qual a capital da amazonia")=='ratanaba':
            maispontos = question1.getpontos()
            aluno.addpontos(maispontos)
            aluno2.addpontos(maispontos)
        if resposta2.getrespostacerta("qual a capital de rondonia")=='porto velho':
            maispontos2 = question2.getpontos()
            aluno2.addpontos(maispontos2)
        assert aluno.getpontos()<aluno2.getpontos()
    def test8(self):#testa add historico
        respostaa = resposta({"qual a capital da amazonia":True},"ratanaba")
        question = perguntas("qual a capital da amazonia",2)
        aluno = estudante("paulo","paulo@paulo","masculo","30")
        if respostaa.getrespostacerta("qual a capital da amazonia")=='ratanaba':
            aluno.addhistorico(question)
        assert len(aluno.gethistorico()) == 1
    
    def test9(self):#testa a soma dos pontos no historico
        resposta1 = resposta({"qual a capital da amazonia":True},"ratanaba")
        question1 = perguntas("qual a capital da amazonia",2)
        question2 = perguntas("qual a capital de rondonia",5)
        resposta2 = resposta({"qual a capital de rondonia":True},"porto velho")
        aluno2 = estudante("braia","braia@braia","homi",30)
        soma =0
        if resposta1.getrespostacerta("qual a capital da amazonia")=='ratanaba':
            maispontos = question1.getpontos()
            aluno2.addpontos(maispontos)
            aluno2.addhistorico(question1)
        if resposta2.getrespostacerta("qual a capital de rondonia")=='porto velho':
            maispontos2 = question2.getpontos()
            aluno2.addpontos(maispontos2)
            aluno2.addhistorico(question2)
        
        for perguntascerta in aluno2.gethistorico():
            soma = perguntascerta.getpontos() + soma
        assert soma ==7