import library

# les fonctions Python ressembles beaucoup aux fonctions de JS
# définition
def hello():
    print('Hello Python!')

# appel ou exécution
hello()

def hello2(name):
    print(f"Hello {name}!")

hello2('foo')

# paramètres + retour de valeur
def addition(a,b):
    return a + b

resultat = addition(42,123)
print(resultat)

# appel d'une fonction stocker dans un autre module
resultat = library.oui_non(False)
print(resultat)
print(library.oui_non(True))

# reverse lookup
my_list = [42, 123, 3.14]

def reverse_lookup(my_list, value):
    """cette fonction prend en paramètre une liste et une valeur à rechercher.
    Elle renvoie l'index de la valeur si elle est trouvée, ou none si la valeur n'est pas trouvée
    
    my_list est de type liste dans il faut chercher
    value any la valeur à rechercher
    return int si la valeur est trouvée ou None si la valeur n'est pas trouvée. 
    """

    for i in range(len(my_list)):
        if my_list[i] == value:
            print(f'{i = }')

reverse_lookup(my_list, 3.14)