### Metodos e funções, utilização de classes. ###
###Utilizar e interagir com modulos e funções anônimas (lambda) ###

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada: # Não preciso colocar == true em variaveis booleanas para saber se são verdadeiras
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

if __name__ == '__main__': #Somente executa quando esse trecho se for chamado pelo proprio arquivo
    televisao = Televisao()
    print('Televisão esta ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão esta ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão esta ligada: {}'.format(televisao.ligada))
    print('Canal: {}'.format(televisao.canal))
    televisao.power()
    print('Televisão esta ligada: {}'.format(televisao.ligada))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.diminui_canal()
    print('Canal: {}'.format(televisao.canal))