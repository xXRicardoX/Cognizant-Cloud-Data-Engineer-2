#Gere, copie, mova, escreva e leia informações de arquivos externos
import shutil

def escrever_arquivo(texto):
    diretorio = 'C:/Users/Ricardo/Documents/Dev/Git/DIO/Cognizant-Cloud-Data-Engineer-2/Python/Introdução à programação com Python/app-python/teste.txt'
    arquivo = open(diretorio, 'w') #o open pode abrir ou criar um arquivo, o 'W' e para escrever
    arquivo.write(texto)
    arquivo.close()#Quando fecha a abertura do arquivo

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open('notas.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    aluno_nota = arquivo.read()
   # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',') #mais uma quebra para virar lista em cada virgula
        aluno = lista_notas[0]
        lista_notas.pop(0) # foi usado o pop para remover um index
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)})
    return lista_media

def copiar_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/Ricardo/Documents/Dev/Git/DIO/Cognizant-Cloud-Data-Engineer-2/Python/Introdução à programação com Python/')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/Ricardo/Documents/Dev/Git/DIO/Cognizant-Cloud-Data-Engineer-2/Python/Introdução à programação com Python/')

if __name__ == '__main__':
    move_arquivo('notas.txt')
    # copiar_arquivo('notas.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    # escrever_arquivo('Primeira linha.\n')
    # aluno = '\nCesar ,7 , 9, 3, 8'
    # atualizar_arquivo('notas.txt', aluno)
    # # # ler_arquivo('teste.txt')
