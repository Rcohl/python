#import du module random pour les nombres aléatoires
import random

#arithmétique
a = 123 + 42
a = 123 - 42
a = 123 * 42
a = 123 / 42

#division entière, integer division
a = 123 // 42
print(a)

#modulo ou reste de la division (euclidienne)
a = 53
#si il y a un reste, le nombre n'est pas divisible par 2, alors il n'est pas pair
print(a % 2)

a = 74
#si il n'y a pas de reste, le nombre est divisible par 2, alors il est pair
print(a % 2)

#puissance, exponentiation
#deux puissance trois
a = 2 ** 3
print(a)

#les opérateurs de comparaison
#opérateur d'égalité (fontionne aussi avec des chaines de caractères)
result = 123 == 42
print(result)

password = "abc"
user_input = "def"
print(password == user_input)

#different de (fontionne aussi avec des chaines de caratères)
print(123 != 42)

#opérateur strictement plus grand que ">"
print(123 > 42)

#opérateur plus grand ou égal ">="
print(42 >= 42)

#opérateur strictement plus petit que "<"
print(42 < 123)

#opérateur plus petit ou égal "<="
print(42 <= 42)

#opérateurs composés
b = 0

#incrémentation
#b = b + 1
b += 1
b += 1
print(b)

#décrémentation
#b = b - 1
b -= 1
b -= 1
print(b)

#multiplication
c = 3
# c= c * 2
c *= 2
print(c)

#division
d = 10
# d = d / 3
d /= 3
print(d)

#division entière
d = 10
# d = d // 3
d //= 3
print(d)

#opérateur in (d'inclusion)
text1 = "Lorem ipsum"

print("e" in text1)
print("lorem" in text1)

list1 = ["lorem","ipsum"]
print("e" in list1)
print("ipsum" in list1)

#comparaison avec des nombres aléatoires
e = random.randint(0, 100)
f = random.randint(0, 100)

print(f'{e = }')
print(f'{f = }')

result = e == f
print(result)

result = e < f
print(result)

#expression
# 1 + 1 -> 2
# (100 + 2) * 3 = -> 102 * 3 -> 306
# 1 + 1 > (100 + 2) * 3
# ce qui donne
# 2 > 306 -> false
#random.randint(0 , 100)

#print(100) -> ce n'est pas une expression

