# exo 7.14
# en utilisant une boucle for, affichez tous les nombre pairs, de 1 à 100 inclus

# réponse 7.14

import random

count = 0

for i in range(101):
    r = random.randint(1, 10)
    if r % 2:
        count += 1

print("Nombre de fois où r est pair:", count)