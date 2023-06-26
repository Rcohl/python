# exo 7.14
# en utilisant une boucle for, affichez tous les nombre pairs, de 1 à 100 inclus

# réponse 7.14

import random

for i in range(1, 101):
    r = random.randint(1, 10)
    if r % 2 == 0:
        print(r)