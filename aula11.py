#Utilizando tratamento de exceções, importancia e como customizar

lista = [1, 10]

# Encadiamento
try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1 # Divisão por 0
    #numero = lista[3] # Acesso invalido de indice
    #x = a # Variavel 'a' não existe

except ZeroDivisionError: # trata o erro de 10/0
    print('Não é possivel realizar uma divisão por 0')

except ArithmeticError:  # trata o erro aritmético
    print('Houve um erro ao realizar uma operação aritmética')

except IndexError: #Trata o erro do index
    print('Erro ao acessar um indice inválido da lista')

except BaseException as ex:
    print('Erro desconhecido, Erro: {}'.format(ex)) # Estou pegando o pai das exceções, todas as exceções vem de BaseEception

else:
    print('Executa quando não ocorre exceção')

finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()

