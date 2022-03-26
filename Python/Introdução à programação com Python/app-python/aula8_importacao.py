#modulos são os arquivos py dentro de uma pasta
from aula7_televisão import Televisao # from e onde pega e o import sera a classe escolhida
from  aula7_calculadora1 import Calculadora
from  aula8_contador_palavras import contador_letras,teste

if __name__ =='__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(5, 10)
    print(calculadora.soma())

    lista = ['cachorro','gato', 'elefante']
    total_letras = contador_letras(lista)
    print('Total de letras por palavras de lista: {}'.format(total_letras))

    print(teste())