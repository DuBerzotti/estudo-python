#Utilizando tratamento de exceções, importancia e como customizar

class Error(Exception): # Para criar uma classe de exceção essa classe é obrigatória
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message


while True: # Fica executando enquanto verdade for verdade
    try:
        x = int(input('Entre com um nota de 0 a 10: '))
        print(x)
        if x > 10:
            # com o raise consigo forçar uma exceção
            raise InputError('Nota não pode ser maior que 10')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0')
        break
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números.')
    except InputError as ex:
        print(ex)