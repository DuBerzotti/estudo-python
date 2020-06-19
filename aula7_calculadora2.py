### Metodos e funções, utilização de classes. ###

# Metodos no python se chama definição

class Calculadora:

    def soma(self, valor_a, valor_b): #Coloco o sef para conseguir acessar os valores da classe
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multipliciacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora() #Intanciar a classe
print(calculadora.soma(10 , 2))
print(calculadora.subtracao(5 , 3))
print(calculadora.multipliciacao(10 , 5))
print(calculadora.divisao(100 , 2))
