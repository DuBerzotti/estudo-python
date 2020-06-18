lista = [12, 10, 5, 7]

lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

#Tupla é imutavel, lista é mutavel
#Não consigo alterar um objeto da tupla

tupla = (1, 10, 12, 14) # Para declarar uma tupla basta colocar em parênteses
print(tupla)
print(tupla[2])
print(len(tupla)) #Retorna quantos elementos na tupla
print(len(lista)) #Retorna quantos elementos na lista

tupla_animal = tuple(lista_animal) #converter uma lista em uma tupla
print(type(tupla_animal))
print(tupla_animal)

lista_numerica = list(tupla) # Converte tupla em lista
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)

lista.sort() # ordena a lista
lista_animal.sort()
print(lista)
print(lista_animal)

lista_animal.reverse() # Ordena de forma reversa, do final ao começo
print(lista_animal)

print(lista_animal[1]) #Com isso vou acessar o gato, python começa a contar em 0

for x in lista_animal:
    print(x)

print(sum(lista)) #Soma todos os numeros da lista de inteiros

print(max(lista)) #Maior valor da lista

print(min(lista)) #Menor valor da lista

print(min(lista_animal)) #Trás menor palavra em comparação a primeira letra.
                         # Ex: a < b,  b > a : Trás a palavra com inicial A.

print(max(lista_animal)) #Trás maior palavra em comparação a primeira letra.
                         # Ex: a < b,  b > a : Trás a palavra com inicio de B.

if 'gato' in lista_animal: #Verifica se tem o elemento gato dentro da lista
    print('Existe um gato na lista')
else:
    print('Não existe um gato na lista')

nova_lista = lista_animal * 3 # Multiplico os valores da lista
print(nova_lista)

if 'Lobo' in lista_animal: #Verifica se tem o elemento gato dentro da lista
    print('Existe um gato na Lobo')
else:
    print('Não existe um gato na Lobo, será incluido.')
    lista_animal.append('Lobo') # append inclui novos itens na lista
    print(lista_animal)

lista_animal.pop() #Retira a ultima posição da lista se não passar paremetro
print(lista_animal)

lista_animal.pop(0) #Retira item da lista informando a posição
print(lista_animal)

lista_animal.remove('elefante') # Remove o elemento que ja conhço
print(lista_animal)

