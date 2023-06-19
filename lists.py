import random
empty_list = []
users = ['foo','bar','baz']
# avec des listes mixte on peut écrire de cette manière
mix = [True, 
       3.14, 
       'lorem ipsum', 
       None, 
       [123,42]
       ]

# accès en lecture
# 0 est l'index du premier élément
print(users[0])

print(len(users))

# len -1 est l'index du dernier élément
i = len(users) - 1
print(users[i])

# l'index dépasse la taille de la liste
#print(users [100 + 42 - i])

# accès en écriture
users[0] = 'lorem'

# ajouter un nouvel élément à la fin
users.append('ipsum')

# ajouter un nouvel élément au début ou au milieu
users.insert(0, 'sit')
users.insert(2, 'dolores')
print(users)

# la fonction pop permet de faire le retrait du dernier élément
last_user =  users.pop()
print(last_user)
print(users)

# suppression par index
first_user = users.pop(0)
print(first_user)
print(users)

# suppression par valeur
users.remove('bar')
print(users)

fruits = ['ananas', 'banane', 'cerise']
legumes = ['artichaud', 'brocoli', 'carotte']
ingredient = fruits + legumes
print(ingredient)

# avec un opérateur composé
fruits += legumes
print(fruits)

# mettre une liste dans l'ordre croissant
numbers = ['g','d','a','c','b','e','f']
numbers = sorted(numbers)
print(numbers)

# liste en 2D
players = [
    [42000,46400,32103],
    [16700,44667,57287],
]

row = 0
col = 0
print(players[0][0])
