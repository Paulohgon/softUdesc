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
        aluno = estudante("paulo","paulo@paulo","masculo","30",0,"")
        if respostaa.getrespostacerta("qual a capital da amazonia")=='ranaba':
            maispontos = question.getpontos()
            aluno.addpontos(maispontos)
            assert aluno.getpontos() == 2