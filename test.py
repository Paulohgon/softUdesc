from question import *
from usuario import *
import pytest
class TestClass:    

    def test1(self):
        question = perguntas("qual seu nome ",2)
        respostaa = resposta({"qual seu nome":True},"paulo")


        testa=respostaa.getrespostacerta("qual seu nome")
        print(testa)
        assert  testa== "paulo"

    def test2(self):
        respostaa = resposta({"qual a capital da amazonia":True},"ratanaba")
        question = perguntas("qual a capital da amazonia",2)
        aluno = estudante("paulo","paulo@paulo","masculo","30")
        if respostaa.getrespostacerta("qual a capital da amazonia")=='ratanaba':
            maispontos = question.getpontos()
            aluno.addpontos(maispontos)
        assert aluno.getpontos() == 2

    def test3(self):
        respostaa = resposta({"qual a capital da amazonia":True},"ratanaba")
        question = perguntas("qual a capital da amazonia",2)

        correta = respostaa.getrespostacerta(question.getenunciado())
        
        assert correta == "ratanaba"

    def test4(self):
        professor1 = professor("pai do brian","paidobrian@paizao.com","homem masculino macho",2,"nada","udesc")
        salacriada = professor1.criasala("ECC0001")
        assert salacriada.getnomesala()=="ECC0001"

    def test5(self):
        professor1 = professor("pai do brian","paidobrian@paizao.com","homem masculino macho",2,"nada","udesc")
        salacriada = professor1.criasala("ECC0001")
        aluno1 = estudante("brian","filhodopaidobria@filhao","loiro",24)
        aluno2 = estudante("bruno","amigodofilhodopaidobraia@amigao","3vezesnasemana",13)
        professor1.addalunosala("ECC0001",[aluno1,aluno2])
        professor1.removealunosala("ECC0001",[aluno1])
        assert len(salacriada.getalunos()) == 1
    def test6(self):
        professor1 = professor("pai do brian","paidobrian@paizao.com","homem masculino macho",2,"nada","udesc")
        salacriada = professor1.criasala("ECC0001")
        aluno1 = estudante("brian","filhodopaidobria@filhao","loiro",24)
        aluno2 = estudante("bruno","amigodofilhodopaidobraia@amigao","3vezesnasemana",13)
        professor1.addalunosala("ECC0001",[aluno1,aluno2])

        assert len(salacriada.getalunos()) == 2