from question import *
import pytest
class TestClass:    

    def test(self):
        question = perguntas("qual seu nome ",2)
        respostaa = resposta({"qual seu nome":True},"paulo")


        testa=respostaa.getrespostacerta("qual seu nome")
        print(testa)
        assert  testa== "paulo"

