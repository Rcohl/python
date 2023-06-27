# scope = portée des variables

my_var1 = 123

def my_func1():
    print(my_var1)
    print(my_var2)

my_var2 = 42

# la fonction voit les variables définies à l'extérieur au préalable ou à postériorie
my_func1()

def my_func2():
    my_var3 = 3.14

my_func2()

# il n'est pas possible d'accéder à une variable définie à l'intérieur d'une fonction
# que celle-ci ait été exécutée ou non
# principe d'un verre teinté.
# NameError: name 'my_var3' is not defined.
# print(my_var3)

my_var4 = 'foo'

def my_func3(my_var4):
    # le paramètre my_var4 masque la variable définie à l'extérieur de la fonction
    print(my_var4)

# cet appel affiche 'bar'
my_func3('bar')

my_var4 = 'foo'

def my_func4():
    # la varible my_var4 fait de l'ombre (shadowing) à la variable définie à l'extérieur de la fonction
    my_var4 = 'baz'
    print(my_var4)

my_func4()
# la variable définie à l'extérieur de la fonction reste inchangée
print(my_var4)
