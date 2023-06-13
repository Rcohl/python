import random

if True :
    print("ce message s'affichera toujours")

if False :
    print("ce message ne s'affichera jamais")
    
number1 = random.randint(0 , 10)
number2 = random.randint(0 , 10)

print(f'{number1 = }')
print(f'{number2 = }')

#Block if1
if number1 < number2 :
    print("number1 est plus petit que number2")
else : 
    print("La première condition n'est pas vérifiée")

#Block if2
if number1 < number2 :
    print("number1 est plus petit que number2")
else : # number1 >= number2
    print("La variable number1 est supérieur ou égale à number2")

#Block if3
# avec les elif
if number1 < number2 :
    print("number1 est plus petit que number2")

elif number1 > number2 :
    print("La variable number1 est plus grande que number2")

else : #elif == else if 
    print("La variable number1 est égale à number2")

#Réécriture du block if3 avec des if imbriqués

if number1 < number2 :
    print("number1 est plus petit que number2")
else : 
    if number1 > number2:
        print("La variable number1 est plus grande que number2")

    else :
        print("Les deux variables sont égales")

#opérateurs booléens

#négation
print(not True)
print(not False)

#Table de vérité de l'opérateur de négation
# A     not A
# True  False
# False True

#OU logique
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#Table de vérité de l'opérateur OU logique
# A      B      A or B
# True   True   True
# True   False  True
# False  True   True
# False  False  False

# pour retrouver la table, remplacez :
#A = j'ai du cash
#B = j'ai ma cb
#A or B = puis-je aller faire mes courses ?

#ET logique
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#Table de vérité de l'opérateur ET logique
# A      B      A and B
# True   True   True
# True   False  False
# False  True   False
# False  False  False

#Table de vérité de l'opérateur NAND (not and) logique
# A      B      A and B   not (A and B)
# True   True   True      False
# True   False  False     True
# False  True   False     True
# False  False  False     True

#syntaxe alternative spécifique à Python équivalent de : age >= 12 and age <=25
#print(12 <= age <= 25)

#OU exclusif (xor)
print(True ^ True)
print(True ^ False)
print(False ^ True)
print(False ^ False)

#table de vérité de l'opérateur xor
# A      B      A xor B
# True   True   False
# True   False  True
# False  True   True
# False  False  False

#exo courses (opérateur OU logique)
#affichez "je peux aller faire les courses" si j'ai au moins un moyen de paiement
#affichez "je ne peux pas aller faire les courses" si je n'ai pas de moyen de paiement

has_cash = bool(random.randint(0 , 1))
has_cb = bool(random.randint(0 , 1))

print(f'{has_cash}')
print(f'{has_cb}')

if has_cash or has_cb:
    print("je peux aller faire les courses")
else:
    print("je ne peux pas aller faire les courses")

#exo courses (opérateur ET logique)
#affichez "je peux aller faire les courses" si j'ai au moins un moyen de paiement
#affichez "je ne peux pas aller faire les courses" si je n'ai pas de moyen de paiement

print(f'{has_cash}')
print(f'{has_cb}')

if not has_cash and not has_cb:
    print("je ne peux pas aller faire les courses")
else:
    print("je peux aller faire les courses")

#combinaison d'opérateur AND et OR
user_level = 2
user_score = 143
user_credit = 0

if user_level >=3 and user_score >=100 or user_credit >= 10:
    print("le joueur peut acheter du matériel")
else:
    print("le joueur ne peut pas acheter du matériel")

#exercice carte de réduction
#déterminez la carte de réduction auquelle le voyageur a droit
#-entre 0 et 11 ans inclus, le voyageur a droit à la gratuité
#-entre 12 et 25 ans inclus, le voyageur a droit à une réduction de 50%
#-entre 26 et 64 ans inclus, le voyageur a droit à une réduction de 10%
#-au dela de 65 ans inclus, le voyageur a droit à une réduction de 50%

age = random.randint(0 , 99)
print(age)

if (0 <= age <= 11):
    print("le voyageur a droit à la gratuité")

elif (12<= age <= 25):
    print("le voyageur a droit à une réduction de 50%")

elif (26 <= age <= 64):
    print("le voyageur a droit à une réduction de 10%")

elif (65 <= age <=99):
    print("le voyageur a droit à une réduction de 50%")

