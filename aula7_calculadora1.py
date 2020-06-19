### Metodos e funções, utilização de classes. ###

# Metodos no python se chama definição

class Calculadora:

    def __init__(self, num1, num2): #Sempre que for instanciar a classe calculadora ele passa por aqui
        self.valor_a = num1 # O self é apra referenciar o próprio objeto
        self.valor_b = num2

    def soma(self): #Coloco o sef para conseguir acessar os valores da classe
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multipliciacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

calculadora = Calculadora(10, 2) #Intanciar a classe
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multipliciacao())
print(calculadora.divisao())