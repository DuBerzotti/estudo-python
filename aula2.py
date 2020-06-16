#Interação com usuário
a = int(input('Entre com o primeiro valor: ')) #Estou recebendo o valor como string e convertendo em inteiro
b = int(input('Entre com o segundo valor: '))

soma = a + b

subtracao = a - b

multiplicacao = a * b

divisao = a / b

resto = a % b # Trás o resto da divisão

# print(type (soma)) Mostra o tipo da variável

# soma = str(soma) Estou convertendo inteiro para string

print('Soma: ' + str(soma)) # Não é a melhor maneira de trabalhar com string

print('Soma: {}' .format(soma)) # Com format ele vai concatenar independente do tipo da variável

resultado = ('Soma: {soma}. \nSubtração: {sub}. '
      '\nMultiplicação: {mult}. \nDivisão: {div}. '
      '\nResto: {resto}. ' .format(soma=soma, sub=subtracao,
                                   mult=multiplicacao, div=divisao, resto=resto))
                                   # Colocando dentro da chave é um apelido e deixar explicito qual variavel corresponde a esse apelido
                                   # Colocando o \n eu quebro uma linha

print(resultado)

print(int(divisao)) # O resultado da divisão é um float, tranformei em inteiro e tirei a segunda casa do resultado

x = '1'
soma2 = int(x) + 1 # converto string em inteiro
print(soma2)

# Comentar mais de
# uma linha seleciona as linhas
# e clica "ctrl + /"


