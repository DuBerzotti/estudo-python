## Conjuntos, como manipular e sua aplicação ##

# Para criar um conjunto uriliza a "{}"

conjunto = {1, 2, 3, 4, 2, 4} # O conjunto não imprime valores que estão duplicados
print(type(conjunto))
print(conjunto)

conjunto.add(5) # Incorpora elemento ao conjunto
print(conjunto)

conjunto.discard(2) # Remove elemento ao conjunto
print(conjunto)

conjunto2 = {1, 2, 3, 4, 5}
conjunto3 = {5, 6, 7, 8}
conjunt_uniao = conjunto2.union(conjunto3) #Une os dois conjuntos
print('União: {}'.format(conjunt_uniao))

conjunto_interseccao = conjunto2.intersection(conjunto3) # É tudo que tem nos dois conjuntos
print('Intersecção: {}'.format(conjunto_interseccao))

conjunto_diferenca1 = conjunto2.difference(conjunto3) # Vai imprimir somente os valores te tem no conjunto da esquerda, a ordem dos fatores neste altera o resultado.
print('Diferença 2 e 3: {}'.format(conjunto_diferenca1))
conjunto_diferenca2 = conjunto3.difference(conjunto2)
print('Diferença 3 e 2: {}'.format(conjunto_diferenca2))

conjunto_diff_simetrica = conjunto2.symmetric_difference(conjunto3) #É tudo que tem no "a e so tem no b".
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica))

conjunto_a = {1, 2, 3} #subset de "B"
conjunto_b = {1, 2, 3, 4, 5} #superset de "A" : Porque b tem todos elementos que tem em "A"
conjunto_subset = conjunto_a.issubset(conjunto_b) #Retorna se o conjunto é sub conjunto de outro conjunto
print('A é subconjunto de B: {}'.format(conjunto_subset)) # Retorna um booleano
conjunto_subset2 = conjunto_b.issubset(conjunto_a)
print('B é subconjunto de A: {}'.format(conjunto_subset2)) # Não é porque tem o 4 e o 5

conjunto_superset = conjunto_b.issuperset(conjunto_a) # Sempre que um conjunto for ao contrario de um subset de um conjunto ele é superset deste conjunto.
print('B é superconjunto de A: {}'.format(conjunto_superset))

#Convertendo a lista em conjunto, fazendo isso remove a duplicidade de valores
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista) # Convertendo lista em conjunto
print(conjunto_animais)

lista_animais = list(conjunto_animais) # Convertendo conjunto em lista
print(lista_animais)