### ler e escrever arquivos, manipular informações, gerar e escrever arquivos ###
import shutil # Biblioteca para copiar e mover arquivo

def escrever_arquivo(texto):
    diretorio = 'C:/Users/Berzotti/OneDrive - Fatec Centro Paula Souza/Estudo Python/estudo-python/teste.txt'
    arquivo = open(diretorio, 'w') # Escrever utilizamos o 'w'
    arquivo.write(texto) #escreve no arquivo, ele faz uma nova escrita
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo , 'a') # Se precisar atualizar um arquivo já criado usamos o 'a'
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r') # Utilizamos o 'r' para leitura
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n') # Passo o comando para ele inserir em uma lista
    #print(aluno_nota)
    lista_media = []

    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        print(aluno)
        lista_notas.pop(0)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4 # Retorno convertido a lista por inteiro faço o sum e divido por 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media
        #print(sum(lista_notas))

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/Berzotti/OneDrive - Fatec Centro Paula Souza/Estudo Python/notas_alunos.txt')

def move_arquivo (nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/Berzotti/OneDrive - Fatec Centro Paula Souza/Estudo Python/') # Caso coloca o nome no final ele move e renomeia

if __name__ == '__main__':
    #copia_arquivo('notas.txt')
    move_arquivo('notas.txt')
    #lista_media = media_notas('notas.txt')
    #print(lista_media)
    #escrever_arquivo('Primeira linha.\n')
    #aluno = 'Augusto,7,9,3,8\n'
    #atualizar_arquivo('notas.txt', aluno)
    #ler_arquivo('teste.txt')