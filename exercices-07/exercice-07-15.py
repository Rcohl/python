# exo 7.15
# en utilisant une boucle for, affichez tous les nombres divisibles par 3, de 2 à 99 inclus

# réponse 7.15

import random

for i in range(2 , 100):
    r = random.randint(1, 10)
    if r % 3 == 0:
        print(r)