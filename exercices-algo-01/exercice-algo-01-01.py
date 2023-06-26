# exo 1.1
# Triez la liste suivante en ordre croissant en utilisant l'algorithme du tri bulle puis affichez la liste.
#
# ATTENTION : ne pas utiliser les fonctions sorted() et list.sort()

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 1.1

def tri_bulle(my_list):
    n = len(my_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if my_list[j] > my_list[j+1] :
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

tri_bulle(my_list)

for i in range(len(my_list)):
    print (my_list[i])
