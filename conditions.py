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
