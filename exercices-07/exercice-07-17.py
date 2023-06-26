# exo 7.17
# en utilisant une boucle for, affichez la puissance 3 des nombres de 1 à 100 inclus

# réponse 7.17

import random

for i in range(1,101):
    r = random.randint(1, 10)
    print(r ** 3)