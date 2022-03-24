#conjunto
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

conjunto_uniao =  conjunto1.union(conjunto2)
print('União: {}'.format(conjunto_uniao))
conjunto_interseccao = conjunto1.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))
conjunto_diferenca1 = conjunto1.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto1)
print("Diferença entre 1 e 2: {}".format(conjunto_diferenca1))
print("Diferença entre 2 e 1: {}".format(conjunto_diferenca2))
conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1,2,3,4,5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é subconjunto de B: {}'.format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A: {}'.format(conjunto_superset))

lista = ['dog', 'dog', 'cat', 'cat', 'elefante']
print(lista)
conjunto_animais = set(lista) #comando SET faz a conversao da lista para conjunto
print(conjunto_animais)
lista_animais = list(conjunto_animais) #list converte conjunto para lista
print(lista_animais)

# conjuto = {1 ,2 ,3 ,4}
# conjuto.add(5)#add um conjunto
# conjuto.discard(2)#Remover um conjunto
# print(conjuto)