# exo 2.1
#
# Ajoutez les 10 premiers nombres de la suite de Fibonacci, que vous
# aurez calculé « à la main », dans une liste nommée
# `fibonacci_numbers`. Puis affichez cette liste en utilisant une
# boucle de type « for each ».
#
# ATTENTION : la suite doit démarre à 0.

# réponse 2.1

fibonacci_numbers = [] 

a, b = 0, 1  
fibonacci_numbers.append(a) 

for i in range(9): 
    a, b = b, a + b  
    fibonacci_numbers.append(a) 
for number in fibonacci_numbers:
    print(fibonacci_numbers)

