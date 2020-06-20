# Lambda é uma função anônima, é a forma de simplificar algo que vamos utilizar mais de uma vez no código

#Esta fazendo a mesma coisa que o contador_letras em aula8_contador de letras faz
# de ma forma simplificada
# Função anônima não precisa de um nome ela fica dentro de uma variavel
contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b


print(soma(5 , 10))
print(subtracao(15 , 10))

#Dicionário com funções lambda
calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda  a, b: a / b,
}

print(type(calculadora))
soma = calculadora['soma'] # soma passa a receber lambda a, b: a + b
multiplicacao = calculadora['multiplicacao']
print('A soma é: {}'.format(soma(10,5)))
print('A multiplicação é: {}'.format(multiplicacao(10,2)))