from question import *
import pytest
class TestClass:    

    def test(self):
        question = perguntas("qual seu nome ",2)
        respostaa = resposta({"qual seu nome ":True},"paulogaraio")

        #question.addresposta("bom dia")

        
        assert respostaa.getrespostacerta("qual seu nome") == "paulo"

# question = perguntas("qual seu nome caralho",2)
# respostaa = resposta({"qual seu nome caralho":True},"paulogaraio")

# question.addresposta("bom dia")
# respostaa.getrespostacerta("qual seu nome caralho")