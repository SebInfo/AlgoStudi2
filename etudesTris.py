import random
def tri_insertion(tableau):
    comp=0
    perm=0
    for i in range(1,len(tableau)):
        en_cours = tableau[i]
        j = i
        # décalage des éléments du tableau 
        comp=comp+1
        while j>0 and tableau[j-1]>en_cours:
            tableau[j]=tableau[j-1]
            j = j-1
        # on insère l'élément à sa place
        tableau[j]=en_cours
        perm=perm+1

    affiche_complexite(tableau,comp,perm)
    
    return tableau

def tri_bulle(tableau):
    comp=0
    perm=0
    permutation = True
    passage = 0
    while permutation == True:
        permutation = False
        passage = passage + 1
        for en_cours in range(0, len(tableau) - passage):
            comp=comp+1
            if tableau[en_cours] > tableau[en_cours + 1]:
                permutation = True
                perm=perm+1
                # On echange les deux elements
                tableau[en_cours], tableau[en_cours + 1] = tableau[en_cours + 1],tableau[en_cours]

    affiche_complexite(tableau,comp,perm)
    return tableau


def tri_selection(tableau):
    comp=0
    perm=0
    nb = len(tableau)
    for en_cours in range(0,nb-1):    
        plus_petit = en_cours
        for j in range(en_cours+1,nb) :
            comp = comp + 1
            if tableau[j] < tableau[plus_petit] :
                plus_petit = j
        if plus_petit is not en_cours :
            perm = perm + 1
            temp = tableau[en_cours]
            tableau[en_cours] = tableau[plus_petit]
            tableau[plus_petit] = temp
    affiche_complexite(tableau,comp,perm)
    return tableau

def affiche_complexite(tableau,comp,perm):
    print("Taille du tableau :", len(tableau))
    print("n2 :", pow(len(tableau),2) )
    print ("Comparaisons :", comp)
    print ("Permutations :", perm)
    print ("Opérations ", perm+comp)



print("Tri à bulles")
print("Tableau avant:")
tab = [1,4,98,123,300,400,800]
print(tab)
tri_bulle(tab)
print("Tableau après le tri:")
print(tab)
print("#################################")

print("Tri par sélection")
print("Tableau avant:")
tab = [1,4,98,123,300,400,800]
print(tab)
tri_selection(tab)
print("Tableau après le tri:")
print(tab)
print("#################################")

print("Tri insertions")
print("Tableau avant:")
tab = [1,4,98,123,300,400,800]
print(tab)
tri_insertion(tab)
print("Tableau après le tri:")
print(tab)
print("#################################")

