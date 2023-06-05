# à gauche c'est la variables et à droite c'est la ou les valeurs
# nombre entier/ integer en EN
number1 =12
number1 =42
print(number1)

#nombre à virgule flottante, float en EN
number2 =3.14
number2 =2.71
print(number2)

#chaine de caratères ou text
text1 ='foo bar baz'
print(text1)

text2 ="foo bar baz"
print(text2)

#booléen, boolean en EN c'est donc des données binaire, soit l'un ou l'autre commme vrai/faux oui/non etc...
python_is_cool = True
print (python_is_cool)

python_is_boring = False
print(python_is_boring)

#valeur nulle, null en EN
user_accepted_terms = None
print(user_accepted_terms)

#types de données
print(type(number1))
print(type(number2))
print(type(text1))
print(type(text2))
print(type(python_is_cool))
print(type(python_is_boring))
print(type(user_accepted_terms))

#vérification du type de données
print(type(number1) is int)
print(type(number2) is str)

# To do: interroger les types de variables
print(type(text1) is bool)
print(type(text2) is str)
print(type(python_is_cool) is bool)
print(type(python_is_boring) is str)
print(type(user_accepted_terms) is int)

#transtypage int--> str
print(type(str(number1)))
print(str(number1))

#transtypage int -->bool
print(type(bool(number1)))
print(bool(number1))

#converti en booléen, la valeur 0 donne false
number3 =0
print(bool(number3))

#transtypage str--> int
#print(type(int(text1))) message d'erreur : ValueError: invalid literal for int() with base 10:

#il ne peut pas y avoir autre chose qu'un nombre dans la chaine de caractère si l'on veut la convertir en int()
text3 ='123456789'
print(type(int(text3)))

#les fonctions de transtypage
#-str() convertit vers chaine de caractère
#-int() convertit vers nombre entier
#-float() convertit vers un nombre à virgule
#-bool() convertit vers un booléen


