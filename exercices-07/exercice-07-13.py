# exo 7.13
# en utilisant une boucle for, affichez tous les nombre pairs, de 1 à 99 inclus

# réponse 7.13

import random

for i in range(1, 100):
    r = random.randint(1, 10)
    if r % 2 == 0:
        print(r)