class Error(Exception):
    pass
class InputErro(Error):
    def __init__(self, message):
        self.message = message
while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise  InputErro('Nota não pode ser maior que dez')
        elif x < 0:
            raise  InputErro("Nota menor que zero")
        break
    except ValueError:
        print('Valor invalido. Deve-se digitar apenas números')
    except InputErro as ex:
        print(ex)
