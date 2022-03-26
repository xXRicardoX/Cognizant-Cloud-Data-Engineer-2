class Televisao():
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:  # if self automaticamente ja entende se a informaçao for verdadeira ja entra nessa condicicional
            self.ligada = False

        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

if __name__ == '__main__': #criando o main para que não pegue o resutado na hora da importação
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