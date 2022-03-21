#listas e tuplas
lista = [12, 10, 5, 7]
lista_animal = ['Cachorro', 'Gato', 'Elefante', 'Lobo', 'Arara']

# lista_animal[0] = 'Macaco'
# print(lista_animal)

tupla = (1, 10, 12, 14)
print(len(tupla))
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print((type(tupla_animal)))
print(tupla_animal)
lista_numerica = list(tupla)
print((type(lista_numerica)))
print(lista_numerica)

# lista.sort()
# lista_animal.sort()
# print(lista,'\n',lista_animal)
# lista.reverse()
# lista_animal.reverse()
# print(lista, '\n', lista_animal)





# nova_lista = lista_animal * 3
# print(nova_lista)
# print(lista)
# print(lista_animal,'\n')
# print(max(lista_animal))
# print(min(lista_animal))

# if 'Lobo' in lista_animal:
#     print("Existe um lobo na lista\n")
# else:
#     print(('Não existe um lobo na lista. Será incluindo\n'))
#     lista_animal.append('Lobo') ## append adiciona um item a lista se não houver
#     print(lista_animal)
#
# # lista_animal.pop(1)#pop retira a ultima coisa que add a lista ou retirar um item da lista escolhendo a posição
# # print(lista_animal)
#
# lista_animal.remove('Elefante')
# print(lista_animal)

# print(sum(lista))
# print(max(lista))
# print(min(lista))
