# exo 7.13
# en utilisant une boucle for, affichez tous les nombre pairs, de 1 à 99 inclus

# réponse 7.13

import random

count = 0

for i in range(100):
    r = random.randint(1, 10)
    if r % 2:
        count += 1

print("Nombre de fois où r est pair:", count)