
lista = [1, 10]

try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]

except ZeroDivisionError:
    print('Não é possivel realizar divisão por Zero')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritimetica')
except IndexError:
    print('Erro ao acessar um indice invalido da lista')
except Exception as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre exceção')

finally:
    print("Semre executa")
    print('Fechando arquivo')
    arquivo.close()