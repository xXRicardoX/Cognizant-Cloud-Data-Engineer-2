a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

#print(type()) serve para ver a classe
resultado ='Soma: {soma}. \nSubtração: {subtracap}.\nMultiplicação: {multiplicacao}. \nDivisão: {divisao}. \nResto: {resto}'.format(soma = soma, subtracap = subtracao,multiplicacao=multiplicacao,divisao=divisao,resto=resto)

print("Resultado:\n", resultado)


# print('subtração: ' + str(subtracao)) # O str faz a conversão do numero para string
# print(multiplicacao)
# print(int(divisao))
# print(resto)

# x = 1
# soma2 = int(x) + 1
# print(soma2)