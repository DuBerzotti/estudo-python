a = int(input('Primeiro Bimestre: '))

if a > 10:
    a = int(input('Você digitou errado. Primeiro Bimestre: '))

b = int(input('Segundo Bimestre: '))

if b > 10:
    b = int(input('Você digitou errado. Segundo Bimestre: '))

c = int(input('Terceiro Bimestre: '))

if c > 10:
    c = int(input('Você digitou errado. Terceiro Bimestre: '))

d = int(input('Quarto Bimestre: '))

if d > 10:
    d = int(input('Você digitou errado. Quarto Bimestre: '))


media = ( a + b + c + d) / 4

print ('Média: {}' .format(media))

# if a <= 10 and b <= 10 and c <= 10 and d < 10:
#     print ('Média: {}' .format(media))
# else:
#     print('Foi informado uma nota errada')

# a = int(input('Entre com primeiro valor: '))
# b = int(input('Entre com segundo valor: '))
#
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or resto_b == 0: #Ou um ou outro (or not) caso a afirmação não for verdadeira
#     print('Foi digitado um número é par')
# else:
#     print('Nenhum número par foi digirado')



# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# if a > b and a > c:
#     print('O maior numero é {}' .format(a)) # Esta dentro do if
# elif b > a and b > c:
#     print('O maior numero é {}'.format(b))
# else:
#     print('O maior numero é {}'.format(c))
#
# print('Final do prog2rama') #Esta fora do bloco if