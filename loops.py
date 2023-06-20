import random

# les différentes boucles:
# for = valeur connue
# for each = liste finie
# while = attente de condition (comme le "if")

# while: c'est comme un "if" mais il est répété
# while False:
    # print("ce message ne s'affiche pas")

# Ctrl+c pour arrêter le programme
# continue permet de reprendre au début de la boucle suivante
# break permet d'afficher le message qu'une seule fois

# while True:
#     #continue
#     print("ce message est affiché en boucle")
#     break

# premier tirage
dice = random.randint(1, 6)

while dice != 6:
    print(f"je n'ai pas tiré un 6, mais un {dice}")
    print("je recommence un nouveau tirage")
    dice = random.randint(1, 6)

print("j'ai tiré un 6")

# recréation de la for classique avec une boucle while
i = 0
while i < 10:
    print(f'{i = }')
    i += 1

# boucle for classique en python
# 0 est inclus mais 10 est exclu
for i in range(0, 10):
    print(f'{i = }')

# boucle à rebour
for i in range(10, 0, -1):
    print(f'{i = }')

users = ['foo','bar','baz']

for user in users:
    print(user)

# enumerate permet de récupérer l'index de chaque éléments
for i, user in enumerate(users):
    print(f"{i = }, {user = }")

# boucle for
for i in range(0, len(users)):
    user = users[i]
    print(f"{i = }, {user = }")

# accumulateur
accumulateur = 0
for i in range(1, 11):
    accumulateur = accumulateur + i # accumulateur += i
    print(f"{i = }")
    print(f"{accumulateur = }")

# liste en 2D
# players = [
#     [42000,46400,32103],
#     [16700,44667,57287],
# ]

# row = 0
# col = 0
#print(players[0][0])

players = [
        [42000,46400,32103],
        [16700,44667,57287],
]
for line_index in range(0, len(players)):
    line = players[line_index]

    for col_index in range(0, len(line)):
        score = line[col_index]
        
        print(score)
        