# exo 6.7
# Inversez la position des valeurs `bar` et `lorem` puis affichez le résultat
#
# ATTENTION : Dans l'énoncé, quand il est écrit Xème position, cela correspond à l'index X-1

my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.7

indice1 = 1
indice2 = 3

temp = my_list[indice1]
my_list[indice1] = my_list[indice2]
my_list[indice2] = temp
print(my_list)


