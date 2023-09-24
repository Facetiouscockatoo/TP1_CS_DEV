#TP1 du module CS-DEV de JEUNET Florian
#Programme principal

import fonctions
from fonctions import validite_texte
from fonctions import transformation_string_to_int_list

from fonctions import mes_Impots

from fonctions import init_matrice
from fonctions import remplissage_matrice
from fonctions import mult_matrices
from fonctions import affichage_matrice
from fonctions import multiplication_matrices_entree_utilisateur

from fonctions import resolution_Hanoi 

from fonctions import syracuse
from fonctions import maximsyr
montant = input("Montant ")     #Affiche les impôts dur le revenu
print(mes_Impots(float(montant)))


date=transformation_string_to_int_list(input("Date(jj/mm/aaaa) "))  #Détermine si une date est valide
print(validite_texte(date[0],date[1],date[2]))



n = int(input("Nombre de lignes pour première matrice: "))          #Affiche le produit matriciel de deux matrices entrées par l'utilisateur
p = int(input("Nombre de colonnes pour première matrice: "))
m = int(input("Nombre de colonnes pour seconde matrice: "))

multiplication_matrices_entree_utilisateur(n,p,m)


n=int(input("Nombre de disques "))      #Donne les instructions du début jusqu'à la fin pour ceux qui sont las de jouer ( int -> des phrases )
resolution_Hanoi(n)



depart=int(input("Terme de départ de la suite ")) #Donne les termes de la suite de Syracuse à partir de n_0 = n, l'altitude maximale atteinte ainsi que le temps de vol.
syracuse(n)

print(maximsyr(1,1001)) #nombres atteignant respectivement le temps de vol et l'altitude maximaux entre 1 et 1001



