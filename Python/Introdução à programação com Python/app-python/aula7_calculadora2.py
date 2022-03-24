# no python o metodo e definição conhecido por def.
class Calculadora:
    def __init__(self,):
        pass #passa o vazio, nada acontece

    def soma(self, valor_a, valor_b): #metodos da soma ate a divisão
        return valor_a + valor_b

    def sub(self, valor_a, valor_b):
        return valor_a - valor_b

    def multi(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b


calc = Calculadora() #Instanciando a classe calculadora

print(calc.soma(3, 4))
print(calc.sub(5, 7))
print(calc.multi(21, 9))
print(calc.divisao(10, 5))