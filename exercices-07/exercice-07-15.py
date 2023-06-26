# exo 7.15
# en utilisant une boucle for, affichez tous les nombres divisibles par 3, de 2 à 99 inclus

# réponse 7.15

import random

count = 0

for i in range(2 , 100):
    r = random.randint(1, 10)
    if r % 3:
        count += 1

print("Nombre de fois où r est divisible par 3:", count)