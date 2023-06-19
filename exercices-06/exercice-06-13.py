# exo 6.13
# Multipliez chacun des nombres dans la liste par 100, réaffactez le résultat à la place de la valeur originelle puis affichez le résultat
#
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`
import random
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.13

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