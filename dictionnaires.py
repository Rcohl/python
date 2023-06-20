# syntaxe pour déclarer un dictionnaire
fruits = {
    'a': 'ananas',
    'b': 'banane',
    'c': 'cerise',
}

print(fruits)

# accès en lecture
print(fruits['a'])
fruit = fruits['a']

# accès en écriture
fruits['a'] = 'abricot'

print(fruits)

# boucle foreach pour obtenir les clés
for key in fruits:
    print(f"{key = }")
    # fruits[key] contient la valeur associée à la clé
    print(f"fruit = {fruits[key]}")

# boucle foreach pour obtenir les clés et les valeurs en même temps
for key, value in fruits.items():
    print(f"{key = }")
    print(f"{value = }")

# boucle foreach pour obtenir les valeurs seulement
for value in fruits.values():
    print(f"{value = }")

# dictionnaire avec clés de tout type
my_dict = {
    100: 'foo',
    # si une même clé réapparaît elle écrase la première
    100: 'bar',
    # pas de soucis pour avoir plusieurs fois la même valeur
    101: 'bar',
    3.14: True,
    True: 'abc',
    None: 123,
}

print(my_dict)

# pour ajouter une nouvelle entrée
my_dict['baz'] = 1
print(my_dict)

# pour supprimer une entrée existance en gardant une copie
#a = my_dict.pop[101]
#print(my_dict)

# pour supprimer une entrée existance sans garder une copie
del my_dict['baz']
print(my_dict)

