a = int(input('Primeiro Bimestre: '))
if a > 10:
    a = int(input('Voce digitiou errado.\nPrimeiro Bimestre: '))
b = int(input('Segundo Bimestre: '))
if b > 10:
    b = int(input('Voce digitiou errado.\nSegundo Bimestre: '))
c = int(input('Terceiro Bimestre: '))
if c > 10:
    c = int(input('Voce digitiou errado.\nTerceiro Bimestre: '))
d = int(input('Quarto Bimestre: '))
if d > 10:
    d = int(input('Voce digitiou errado.\nQuarto Bimestre: '))
media = (a+b+c+d)/4
print('Media: {}'.format(media))
if media >= 7:
    print("O aluno passou de ano!!! ")
elif media > 4 and media < 7:
    print("O aluno esta de recuperação ")
else:
    print("O aluno foi reprovado!!! ")

# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('Media: {}'.format(media))
# else:
#     print('Foi informado alguma nota errada')

# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo  valor: '))
#
# resto1 = a % 2
# resto2 = b % 2
#
# if resto1 == 0 or not resto2 > 0 :
#      print('Foi digitado um numero par')
# else:
#     print('Nenhum numero par foi digitado')


#resto = a % 2
# if resto == 0:
#     print('o numero {} e par '.format(a) )
# else:
#     print('o numero {} e impar '.format(a))






# a = int(input('primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
#
# if a > b and a > c:
#     print('O maior número é {}'.format(a))
#
# elif b > a and b > c:
#     print('O maior numero é {}'.format(b))
# else:
#     print('O maior numero é {}'.format(c))
# print('Final do programa')