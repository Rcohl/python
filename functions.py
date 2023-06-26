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

#type hinting
def mult (a: int, b: int) -> int:
    """cette fonction
    a...
    b...
    retrun...
    """

    return a * b
resultat = mult('abc', 5)
print(resultat)

# le nom de la fonction + ses paramètres + son type de retour = signature de la fonction
# def mult(a: int, b: int) -> int:

# copie d'une fonction comme si c'était une variable
mult_copy = mult
mult_copy(2, 5)

# fonction de degré supérieur
# une fonction qui accepte une fonction en paramètre
# ou qui renvoie une fonction
def oprateur_binaire(a, b, fonction):
    return fonction(a, b)
# appel de la fonction de degré supérieur
resultat = oprateur_binaire(2, 5, mult)

# stockage de fonctions dans une liste
operations = []
operations.append(addition)
operations.append(mult)

a = 2
b = 5
resultat = None

for operation in operations:
    resultat = operation(a, b)
    print(resultat)

my_list = ['foo','ipsum']
text = 'toto'

print(len(my_list))
print(len(text))

def my_len(value):
    return 42

# sauvegarde de la fonction len() originale
len_backup = len
# surcharge de la fontion len() originale càd remplacement de la fonction originale par une autre
len= my_len

print(len(my_list))
print(len(text))

# restauration de la fonction len() originale
len = len_backup

# pass permet d'écrire du code python syntaxiquement valide même quand on n'a pas encore le corps 
# de la condition if ou de la boucle for

if True:
    pass
