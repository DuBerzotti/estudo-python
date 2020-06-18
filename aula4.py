for x in range(101): # range pega todos os numeros de 0 à 99
    print (x)

###############verificando se numero é primo##################
a = int(input('Entre com um numero: '))

div = 0;
for x in range (1, a +1):
    resto = a % x
    print(x, resto)
    if resto == 0: #divisão bem sucedida
        div += 1

if div == 2 : #foi dividido por 2 números 1 e ele mesmo
    print('Número {} é primo'.format(a))
else:
    print('Numero {} não é primo'.format(a))
##############################################################

#####################Imprimindo somente numero primo##########

a = int(input('Entre com um valor: '))

for num in range(a):
    div = 0;
    for x in range (1, num+1):
        resto = num % x
        #print(x, resto)
        if resto == 0: #divisão bem sucedida
            div += 1

    if div == 2 : #foi dividido por 2 números 1 e ele mesmo
        print(num)
##############################################################

##### While #####

a = int(input('Primeiro Bimestre: '))

while a > 10:
    a = int(input('Você digitou errado. Primeiro Bimestre: '))

b = int(input('Segundo Bimestre: '))

while b > 10:
    b = int(input('Você digitou errado. Segundo Bimestre: '))

c = int(input('Terceiro Bimestre: '))

while c > 10:
    c = int(input('Você digitou errado. Terceiro Bimestre: '))

d = int(input('Quarto Bimestre: '))

while d > 10:
    d = int(input('Você digitou errado. Quarto Bimestre: '))

media = ( a + b + c + d) / 4

print ('Média: {}' .format(media))
