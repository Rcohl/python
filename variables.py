# à gauche c'est la variables et à droite c'est la ou les valeurs
# nombre entier/ integer en EN
number1 = 12
number1 = 42
print(number1)

# nombre à virgule flottante, float en EN
number2 = 3.14
number2 = 2.71
print(number2)

# chaine de caratères ou text
text1 = "foo bar baz"
print(text1)

text2 = "foo bar baz"
print(text2)

# booléen, boolean en EN c'est donc des données binaire, soit l'un ou l'autre commme vrai/faux oui/non etc...
python_is_cool = True
print(python_is_cool)

python_is_boring = False
print(python_is_boring)

# valeur nulle, null en EN
user_accepted_terms = None
print(user_accepted_terms)

# types de données
print(type(number1))
print(type(number2))
print(type(text1))
print(type(text2))
print(type(python_is_cool))
print(type(python_is_boring))
print(type(user_accepted_terms))

# vérification du type de données
print(type(number1) is int)
print(type(number2) is str)

# To do: interroger les types de variables
print(type(text1) is bool)
print(type(text2) is str)
print(type(python_is_cool) is bool)
print(type(python_is_boring) is str)
print(type(user_accepted_terms) is int)

# transtypage int--> str
print(type(str(number1)))
print(str(number1))

# transtypage int -->bool
print(type(bool(number1)))
print(bool(number1))

# converti en booléen, la valeur 0 donne false
number3 = 0
print(bool(number3))

# transtypage str--> int
# print(type(int(text1))) message d'erreur : ValueError: invalid literal for int() with base 10:

# il ne peut pas y avoir autre chose qu'un nombre dans la chaine de caractère si l'on veut la convertir en int()
text3 = "123456789"
print(type(int(text3)))

# les fonctions de transtypage
# -str() convertit vers chaine de caractère
# -int() convertit vers nombre entier
# -float() convertit vers un nombre à virgule
# -bool() convertit vers un booléen

# chaine de caratère, string
# Cette notation permet d'utiliser des sauts de ligne (souvent pour stocker du html car de chaine de caractère très longue)
#\n est équivalent à un saut de ligne
#\t est équivalent à une tabulation
text4 = """ <div>
        <h1> Titre de premier niveau <h1>
<div>"""
print(text4)

text5 = "<div>\n\t<h1>Titre de premier niveau</h1>\n\t<div>"
print(text5)

#la back slash seul est le caratère d'échappement
#\" est équivalent à uen guillemet"
#\\ est équivalent à un back slash \
text6 = "Foo \"Bar\" Baz"
print(text6)
text7 = "C:\\Program Files\\Foo"
print(text7)

#permutez les deux variables a et b en utilisant l'opérateur d'affectation et le nom des variables
a = 123
b = 42

#permutation des valeurs à l'aide d'une variable intermédiaire (plus simple)
c = b 
b = a
a = c

print(a)
print(b)

#permutation des valeurs à l'aide d'opérations arithmétiques (plus complexe)
#a = a + b
#b = a - b
#a = a - b

#print(a)
#print(b)