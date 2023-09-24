#Liste des fonctions utiles au programme principal du TP1 du module CS-DEV
# Reste à faire:
#     - compte des déplacements pour la résolution du jeu des tours de Hanoï 
#     ( pour s'assurer qu'il s'agit bien de 2**n -1 pour n disques comme dans la manière optimale )

#     - Travail sur les nombres tricolores (vérification du caractère tricolore d'un nombre à l'aide de la transformation en string puis de l'étude de l'appartenance des caractères dans ['1','4','9'])
#                                          (programme donnant tous les nombres tricolores de 1 à N, N un entier)     
#     - Travail sur les nombres amicaux    (programme vérifiant les bons sentiments éprouvés entre deux entiers naturels)
#     - interface graphique pour la résolution du produit matriciel





#Fonctions utiles au calendrier

def test_bissextile(n): #détermine si une année est bissextile (int -> bool)
    return (n%100==0 and n%4 != 0) or n%400
    
    

def nombre_jours(mois,annee): #donne le nombre de jours d'un mois sur une année précise (int*int -> int)
    if mois > 12 or mois==0: raise ValueError("mois invalide")
    if mois != 2:              # mois autre que février
        if (mois%2) == 1 or mois==8: return 31 
        else: return 30
    if test_bissextile(annee): return 29 #mois de février
    else: return 28

# format dd/mm/aaaa
def date_valide(jour,mois,annee): #Détermine la validité d'une date (int*int*int -> bool)
    if not jour > 31 or jour == 0 or mois == 0 or mois > 12: #Enlève les impossibilités de nombre de jours et de mois
        return jour <= nombre_jours(mois,annee)
    else: return False    

 
        
def validite_texte(jour,mois,annee): #version texte de datevalide (int*int*int -> str)
    if date_valide(jour, mois, annee): return "date valide"
    else: return "date non valide"

def transformation_string_to_int_list(date): #permet l'implémentation des input de date au format jj/mm/aaaa (str sous la forme */*/*) -> int*int*int
    l = []
    date_list = date.split('/')
    for i in range(len(date_list)):
        p = 0
        l.append(int(date_list[i][p:]))
    return l[0],l[1],l[2]





#Ai-je respecté les bonnes pratiques ? J'espère !







#Fonction utile au calcul des impôts en 2022

def mes_Impots(n): #donne le montant des impôts sur le revenu en fonction desdits revenus (int->int). Les impôts sont arrondis par défaut
    echelon_2 = ((26070-10225)*11)/100
    echelon_3 = ((64545-26070)*30)/100
    echelon_4 = ((160336-74545)*41)/100 #valeur maximale des impôts pour les échelons 2 à 4, à rajouter pour les échelons supérieurs
    if n <= 10225: return 0
    if n <= 26070: return (((n-10225)*11)/100)//1  
    if n <= 74545: return (((n-26070)*30)/100 +echelon_2)//1
    if n <= 160336: return (((n-74545)*41)/100 +echelon_3 +echelon_2)//1
    return (((n-160336)*45)/100 +echelon_4 +echelon_3 +echelon_2)//1








#Fonction utile à la multiplication de matrices de M_n,p(R)*M_p,m(R). 

def mult_matrices(m1,m2): # multiplications de matrices rectangulaires (float list list* float list list -> float list list )
    nombre_colonnes_m1 = len(m1[0])
    nombre_lignes_m1 = len(m1)
    nombre_lignes_m2 = len(m2)
    nombre_colonnes_m2 = len(m2[0])
    if nombre_colonnes_m1 != nombre_lignes_m2: raise ValueError("matrices incohérentes") 
    res = [[0 for i in range(nombre_colonnes_m2)] for i in range(nombre_lignes_m1)]
    for i in range(nombre_lignes_m1):
        for j in range(nombre_colonnes_m2): #Parcours de la matrice res
            for k in range(nombre_colonnes_m1):
                res[i][j] += m1[i][k] * m2[k][j] #coefficient en (i,j) de res
    return res


# trois fonctions adaptées du code 1 de https://www.geeksforgeeks.org/take-matrix-input-from-user-in-python/
def init_matrice(n,p):                                  #Création de matrice de taille n*p int*int -> int list list
    matrice = [[0 for i in range(p)] for i in range(n)]
    return matrice
def remplissage_matrice(n,p):                           #fonction de remplissage par l'utilisateur d'une matricede taille n*p (int*int -> int list list avec entrées par l'utilisateur)
    matrice = init_matrice(n,p)
    
    for i in range(n):          
        for j in range(p):      
             matrice[i][j] = (int(input(f"Coefficients en {i},{j} "))) #Entrée ligne par lignes des coefficients par l'utilisateur
    return matrice

def affichage_matrice(matrice):                         #fonction d'affichage de matrice quelconque
    n = len(matrice)
    p = len(matrice[0])
    for i in range(n):
        for j in range(p):
            print(matrice[i][j], end = " ")
        print()


def multiplication_matrices_entree_utilisateur(n,p,m):          #réunion des trois fonctions permettant de donner le résultat du produit des matrices implémentées en entrée ( int*int*int -> int list list )
    affichage_matrice(mult_matrices(remplissage_matrice(n,p),remplissage_matrice(p, m))) #trois entiers sont en entrée au lieu de quatre -> empêche les matrices incohérentes car p est commun aux deux matrices








#Fonctions utiles à la résolution du jeu des tours de Hanoï

def resolution_Hanoi(n):  #Donne les déplacements à effectuer pour amener une tour de n disques du plot 1 au plot 3 (int -> string)
                          #Cette fonction équivaut donc à deplacement_plot1_plot3
                          #Utilisation de récurrences imbriquées entre chaque type de déplacement. Chaque fonction a un cas d'arrêt en n = 1, et chaque appel diminue le n. Ainsi la fonction se termine.
                          #Formule de récurrence pour chaque type de déplacement: Déplacement_plotDedépart_plotDepassage(n-1) + "Déplacement_plotDeDépart_plotD'arrivée" + Déplacement_plotDepassage_plotD'arrivée(n-1)
    if n == 0:
        return("Vous jouez au tours de Hanoï ou au lancer de fer à cheval ?")
    if n == 1:              
        print("PLot 1 vers Plot 3")
        print()
        
        
        
        
    else:
        def deplacement_plot1_plot2(n,k):
            if n == 1:
                print("PLot 1 vers Plot 2")
                print()
            else:
                resolution_Hanoi(n-1)
                print("PLot 1 vers Plot 2")
                print()
                deplacement_plot3_plot2(n-1)
        def deplacement_plot2_plot3(n):
            if n == 1:
                print("PLot 2 vers Plot 3")
                print()
            else:
                deplacement_plot2_plot1(n-1)
                print("PLot 2 vers Plot 3")
                print()
                resolution_Hanoi(n-1)
        def deplacement_plot3_plot2(n):
            if n == 1:
                print("PLot 3 vers Plot 2")
                print()
            else:
                deplacement_plot3_plot1(n-1)
                print("PLot 3 vers Plot 2")
                print()
                deplacement_plot1_plot2(n-1)
        def deplacement_plot2_plot1(n):
            if n == 1:
                print("PLot 2 vers Plot 1")
                print()
            else:
                deplacement_plot2_plot3(n-1)
                print("PLot 2 vers Plot 1")
                print()
                deplacement_plot3_plot1(n-1)
        def deplacement_plot3_plot1(n):
            if n == 1:
                print("PLot 3 vers Plot 1")
                print()
            else:
                deplacement_plot3_plot2(n-1)
                print("PLot 3 vers Plot 1")
                print()
                deplacement_plot2_plot1(n-1)
        
        deplacement_plot1_plot2(n-1)
        print("PLot 1 vers Plot 3")
        print()        
        deplacement_plot2_plot3(n-1)
        
    
        
    








#Fonctions utiles à l'application de la conjecture de Syracuse

def syracuse(n):
    alt=n
    i=0
    terme=n
    print(terme)
    while terme != 1:
        if terme%2==0: terme/2
        else: terme= terme*3 +1
        print(terme)
        if terme > alt: alt = terme
        i+=1
    return alt,i

def maximsyr(a,b):
    maximvol=a
    maximalt=a
    
    for i in range(a,b+1):
        if syracuse(i)[0]>maximalt: maximalt=i
        if syracuse(i)[1]>maximvol: maximvol=i
    return maximvol,maximalt
        





        
        
    

      
    
    
        
        
        
        
        
    
        
        


    
    

    

        
    

    