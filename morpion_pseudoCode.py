#debut 


# importer le module random
# importer le module time
# importer le module os

#assigner à command la str "cls"
#utiliser la fonction du system du module os de paramètre command  ## os.system(command)

#assigner à taille la valeur 3

#definir la fonction tailleGrille de paramètre taille 
    #incrémenter à tab un tableau de tableau rempli avec le charactère '□' par compréhension de longueur taille
    ## tab = [['□' for i in range(taille)]for j in range(taille)] 
    # renvoyer tab

# initialiser tab avec le retour de l'éxécution de la fonction tailleGrille de paramètre taille
# initialiser longueurTab la longueur du tableau tab multiplier par la longueur du tableau tab
# initialiser joueurPlay1 qui est le retour de l'éxécution de la fonction input de paramètre la figure choisie
# initialiser joueurPlay2 qui est le retour de léxécution de la fonction choice de paramètre un tableau composé de l'alphabet en majuscule
# initialiser alreadyPlay comme étant un tableau vide
# initialiser firstPlayer qui est le retour de l"éxécution de la fonction choice de paramètre un tableau composé de 0 et 1
# afficher le joueur jouant en premier 

# definir la fonction printTab
    # pour i dans tab 
        # alors 
        # afficher la valeur de i
    # afficher un mot vide 

# definir emplacementJoueur de paramètre choix et coup_Joueur
    # if choix vaut la str "1" :
        # alors
        #  assigner à la valeur de tab de coordonnées tab[0][0] la valeur de  coup_Joueur
    # si sinon choix vaut la str "2" :
        #alors
        #  assigner à la valeur de tab de coordonnées tab[0][1] la valeur de  coup_Joueur
    # si sinon choix  vaut la str "3" :
        #alors
        # assigner à la valeur de tab de coordonnées tab[0][2] la valeur de  coup_Joueur
    # si sinonchoix  vaut la str "4" :
        #alors
        # assigner à la valeur de tab de coordonnées tab[1][0] la valeur de  coup_Joueur
    # si sinon choix  vaut la str "5" :
        #alors
        # assigner à la valeur de tab de coordonnées tab[1][1] la valeur de  coup_Joueur
    # si sinon choix  vaut la str "6" :
        #alors
        # assigner à la valeur de tab de coordonnées tab[1][2] la valeur de  coup_Joueur
    # si sinon choix  vaut la str "7" :
        #alors
        # assigner à la valeur de tab de coordonnées tab[2][0] la valeur de  coup_Joueur
    # si sinon choix  vaut la str "8" :
        #alors
        # assigner à la valeur de tab de coordonnées tab[2][1] la valeur de  coup_Joueur
    # si sinon choix  vaut la str "9" :
        #alors
        # assigner à la valeur de tab de coordonnées tab[2][2] la valeur de  coup_Joueur
    # renvoyer l'affichage du retour de l'éxécution de la fonction printTab
