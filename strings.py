text1 = "lorem"
text2 = "ipsum"

# concaténation
text3 = text1 + text2
print(text3)
#solution
text3 = text1 + " " + text2
print(text3)

#interpolation avec une f-string
text3 = f"{text1} {text2}"
print(text3)

#Attention : la concaténation ne fonctionne qu'avec des mails
#solution : convertir les autres types en str
mails = 52
text4 = "vous avez " + str(mails) + " mails non lus"
print(text4)

#répétition de texte
text5 = "foo" * 3
print(text5)

#affichage de valeur arrondies mais sans arrondir la variable
number1 = 10 / 3
text6 = f"10 / 3 est à peu près égal {number1:.2f}"
print(text6)

#les fonctions associés aux strings
text7 = "foo bar baz foo"
print(len(text7)) #lenght = longueur de la chaine de caractère

print(text7.count('foo')) #count = compte le nombre de fois où le caractère apprait dans la chaine de caractère

#retrouver l'emplacement d'un mot/caractère
text7 = "foo bar baz foo"
position = text7.find('foo')
print(position)

#pour trouver l'occurence suivante, il faut chercher une position plus loin
print(text7.find('foo', position + 1))

#si le mot/caractère n'existe pas il renvoie -1, position qui n'existe pas non plus
position = text7.find('lorem')
print(position)

#remplacement de mots
text7 = text7.replace('foo' , 'lorem') #remplace le mot dans la variable
print(text7.replace('foo' , 'lorem')) #ne remplace pas le mot dans la variable

#split & join
list1 = text7.split(' ')
print(list1)

text8 = "+".join(list1)
print(text8)

#documenter une fonction, on le fait avec 3 "

def ouiNon(value):
    if value == True:
        return "oui"
    elif value == False:
        return "non"
    """cette fonction renvoie: 
    -oui si le paramètre passé est True
    -non si le paramètre passé est False
    -"" dans les autres cas

    value bool valeur qui sera transformée en "oui" ou "non"
    return str"""
    
    return "" 
help(ouiNon)
