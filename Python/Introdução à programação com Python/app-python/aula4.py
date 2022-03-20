## Comando FOR, While e Range(numeros aleatorios)
a = int(input('Primeiro Bimestre: '))
while a > 10:
    a = int(input('Voce digitiou errado.\nPrimeiro Bimestre: '))
b = int(input('Segundo Bimestre: '))
while b > 10:
    b = int(input('Voce digitiou errado.\nSegundo Bimestre: '))
c = int(input('Terceiro Bimestre: '))
while c > 10:
    c = int(input('Voce digitiou errado.\nTerceiro Bimestre: '))
d = int(input('Quarto Bimestre: '))
while d > 10:
    d = int(input('Voce digitiou errado.\nQuarto Bimestre: '))
media = (a+b+c+d)/4
print('Media: {}'.format(media))
if media >= 7:
    print("O aluno passou de ano!!! ")
elif media > 4 and media < 7:
    print("O aluno esta de recuperação ")
else:
    print("O aluno foi reprovado!!! ")

# nota = int(input('Entre com a nota: '))
# while nota > 10:
#     nota = int(input('Nota invalida. Entre com a nota correta: '))

# a = 0
# while a <=10:
#     print(a)
#     a += 1

# a = int(input('Entre com um valor: '))
# for num in range(a +1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#        #print(x, resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)

# a = int(input("Entre com o número: "))
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#    # print(x, resto)
#     if resto == 0:
#         div += 1
# if div == 2:
#     print('Número {} é primo'.format(a))
# else:
#     print('Número {} não e primo'.format(a))

# for x in range(101):
#     print(x)

