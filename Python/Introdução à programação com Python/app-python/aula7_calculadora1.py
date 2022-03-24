# no python o metodo e definição conhecido por def.
class Calculadora:
    def __init__(self, num1, num2): #esse e o metodo que sempre ira chamar primeiro

        self.valor_a = num1
        self.valor_b = num2

    def soma(self): #metodos da soma ate a divisão
        return self.valor_a + self.valor_b

    def sub(self):
        return self.valor_a - self.valor_b

    def multi(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

valor_a = int(input('digite o primeiro valor: '))
valor_b = int(input('Digite o segundo valor: '))
calc = Calculadora(valor_a, valor_b) #Instanciando a classe calculadora
print(calc.valor_a, "E", valor_b)
print(calc.soma())
print(calc.sub())
print(calc.multi())
print(calc.divisao())