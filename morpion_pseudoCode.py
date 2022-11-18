#debut 

# importer le module random
# importer le module time
# importer le module os

# assigner à command la str "cls"
# utiliser la fonction du system du module os de paramètre command  ## os.system(command)

# assigner à taille la valeur 3

# definir la fonction tailleGrille de paramètre taille 
    # initialiser cpt valant 1
    # incrémenter à tab un tableau de tableau rempli avec le charactère '□' par compréhension de longueur taille
    ## tab = [['□' for i in range(taille)]for j in range(taille)] 
    # pour i dans le retour de l'éxécution de la fonction range de paramètre taille
        # alors
        # pour j dans le retour de l'éxécution de la fonction range de paramètre taille
            # alors
            # la valeur de tab d'indice i et j vaut le str de cpt
            # incrémenter cpt de 1
    # renvoyer tab

# initialiser tab avec le retour de l'éxécution de la fonction tailleGrille de paramètre taille
# initialiser à tabFictif un tableau de tableau rempli avec le charactère '□' par compréhension de longueur taille

# initialiser longueurTab la longueur du tableau tab multiplier par la longueur du tableau tab
# initialiser joueurPlay1 qui est le retour de l'éxécution de la fonction input de paramètre la figure choisie

# tant que joueurPlay1 est dans la liste des entiers de 1 à 10 rentré comme des str
    # on assigne a joueurPlay1 le retour de l'éxécution de la fonction input de paramètre la figure choisie de nouveau

# initialiser joueurPlay2 qui est le retour de l'éxécution de la fonction choice de paramètre un tableau composé de l'alphabet en majuscule
# initialiser alreadyPlay comme étant un tableau vide
# initialiser firstPlayer qui est le retour de l'éxécution de la fonction choice de paramètre un tableau composé de 0 et 1
# afficher le joueur jouant en premier 

# definir la fonction afficher
    # initialiser grille qui vaut la str d'un saut de ligne ##"\n"
    # pour i dans le retour de l'éxécution de la fonction range de paramètre taille
        # alors
        # pour j dans le retour de l'éxécution de la fonction range de paramètre taille
            # alors
            # incrémenter grille du str "| " puis concatainer la valeur de tab d'indice i et j puis container la str  " "
        # incrémenter grille du str "|"
        # incrémenter grille de la str " \n- - - - - - -\n"
    # afficher grille


# definir emplacementJoueur de paramètre choix et coup_Joueur
    # if choix vaut la str "1" :
        # alors
        # assigner à la valeur de tab de coordonnées tab[0][0] la valeur de coup_Joueur
        # assigner à la valeur de tabFictif de coordonnées tab[0][0] la valeur de coup_Joueur
    # si sinon choix vaut la str "2" :
        #alors
        # assigner à la valeur de tab de coordonnées tab[0][1] la valeur de coup_Joueur
        # assigner à la valeur de tabFictif de coordonnées tab[0][1] la valeur de coup_Joueur
    # si sinon choix  vaut la str "3" :
        #alors
        # assigner à la valeur de tab de coordonnées tab[0][2] la valeur de coup_Joueur
        # assigner à la valeur de tabFictif de coordonnées tab[0][2] la valeur de coup_Joueur
    # si sinon choix  vaut la str "4" :
        #alors
        # assigner à la valeur de tab de coordonnées tab[1][0] la valeur de coup_Joueur
        # assigner à la valeur de tabFictif de coordonnées tab[1][0] la valeur de coup_Joueur
    # si sinon choix  vaut la str "5" :
        #alors
        # assigner à la valeur de tab de coordonnées tab[1][1] la valeur de coup_Joueur
        # assigner à la valeur de tabFictif de coordonnées tab[1][1] la valeur de coup_Joueur
    # si sinon choix  vaut la str "6" :
        #alors
        # assigner à la valeur de tab de coordonnées tab[1][2] la valeur de coup_Joueur
        # assigner à la valeur de tabFictif de coordonnées tab[1][2] la valeur de coup_Joueur
    # si sinon choix  vaut la str "7" :
        #alors
        # assigner à la valeur de tab de coordonnées tab[2][0] la valeur de coup_Joueur
        # assigner à la valeur de tabFictif de coordonnées tab[2][0] la valeur de coup_Joueur
    # si sinon choix  vaut la str "8" :
        #alors
        # assigner à la valeur de tab de coordonnées tab[2][1] la valeur de coup_Joueur
        # assigner à la valeur de tabFictif de coordonnées tab[2][1] la valeur de coup_Joueur
    # si sinon choix  vaut la str "9" :
        #alors
        # assigner à la valeur de tab de coordonnées tab[2][2] la valeur de coup_Joueur
        # assigner à la valeur de tabFictif de coordonnées tab[2][2] la valeur de coup_Joueur
    # renvoyer l'affichage du retour de l'éxécution de la fonction afficher


# définir la fonvtion victoire 
    # initialiser la variable winTotale comme étant un tableau de longueur 8 rempli de 0 
    ## [[789], [456], [123], [741], [852], [963], [753], [951]] #combinaison de win possible
    ## [  0,     0,     0,     0,     0,     0,     0,     0  ]

    # pour i prennant les valeurs 0,1,2
        # si joueurPlay1 dans tabFictif d'indice i et joueurPlay2 dans tabFictif d'indice i
            # alors
            # incrémenter winTotale à l'indice i la valeur -1
        # si sinon le caractère '□' est dans tabFictif d'indice i
            # alors
            # pass
        # sinon
            # alors
            # incrémenter winTotale à l'indice i la valeur de tab d'indice i et 0

    # pour i prennant les valeurs 0,1,2
        # si joueurPlay1 dans un nouveau tableau de valeur tabFictif d'indice j et i pour j dans les valeurs 0,1,2 et joueurPlay2 dans un nouveau tableau de valeur tabFictif d'indice j et i pour j dans les valeurs 0,1,2
            # alors
            # incrémenter winTotale à l'indice i + 3 la valeur -1
        # si sinon le caractère '□' est dans un nouveau tableau de valeur tabFictif d'indice j et i pour j dans les valeurs 0,1,2
            # alors
            # pass
        # sinon
            # alors
            # incrémenter winTotale à l'indice i + 3 la valeur de tab d'indice 0 et i
    
    # pour i prennant les valeurs 0,1
        # si joueurPlay1 dans un nouveau tableau de valeur tabFictif d'indice j et [(2 - j) * i - j * (i - 1)]  pour j dans les valeurs 0,1,2 et joueurPlay2 dans un nouveau tableau de valeur tabFictif d'indice j et [(2 - j) * i - j * (i - 1)]  pour j dans les valeurs 0,1,2 
            # alors
            # incrémenter winTotale à l'indice i + 6 la valeur -1
        # si sinon le caractère '□' est dans un nouveau tableau de valeur tabFictif d'indice j et [(2 - j) * i - j * (i - 1)]  pour j dans les valeurs 0,1,2 
            # alors
            # pass
        # sinon
            # alors
            # incrémenter winTotale à l'indice i + 6 la valeur de tab d'indice 0 et i * 2
    
    # renvoyer winTotale
     

# definir la fonction whoWin
    # pour i dans Victoire 
        # si i vaut la valeur de joueurPlay1
            # alors
            # renvoyer l'affichage "Victoire du joueur 1"
        # si sinon i vaut la valeur de joueurPlay2
            # alors
            # renvoyer l'affichage "Victoire du joueur 2"
        # sinon 
            # alors
            # pass

# definir la fonction game
    # appelle de global avec les variables firstPlayer et joueurPlay2
    # initialisation de robot qui est le retour de l'éxécution de la fonction input "voulez vous joueur avec un bot ? [True or FAlse]"
    # initialisation de coupJoueur comme étant un mot vide
    # initialisation de choixRobot qui est le retour de l'éxécution de la fonction randint de paramètre 1, 9 etant un str

    # si robot vaut la str "False" 
        # alors 
        # afficher "Vous avez choisi le mode multijoueur"
        # modifie joueurPlay2 qui est le retour de l'éxécution de la fonction input de paramètre la figure choisie*
        # tant que joueurPlay1 vaut joueurPlay2 ou si joueurPlay2 et dans est dans la liste des entiers de 1 à 10 rentré comme des str
            # alors
            # modifie joueurPlay2 qui est le retour de l'éxécution de la fonction input de paramètre la figure rechoisie*
    # sinon
        # alors 
        # afficher "Vous avez choisi le mode contre L'IA"

    # afficher le retour de l'éxécution de la fonction afficher

    # tant que la longueur de alreadyPlay est inférieur à longueurTab
        # alors
        # si robot vaut la str "False"
            # alors
            # utiliser la méthode .sleep de paramètre 0.3
            # si firstPlayer vaut 0
                # alors
                # assigner à caseJoueurPlay1 le retour de l'éxécution de la fonction input de paramètre choisir l'endroit où l'on veut joueur
                # tant que caseJoueurPlay1 dans alreadyPlay
                    # alors  
                    # assigner à caseJoueurPlay1 le retour de l'éxécution de la fonction input de paramètre rechoisir l'endroit où l'on veut joueur
                # incrémenter alreadyPlay grâce grace au retour de l'éxécution la méthode append de paramètre caseJoueurPlay1
                # utiliser la fonction amplacementJoueur de paramètre caseJoueurPlay1 et joueurPlay1
                # incrémenter de 1 firstPlayer
                # assigner à coupJouer la variable caseJoueurPlay1

            # si sinon firstPlayer vaut 1
                # alors
                # assigner à caseJoueurPlay2 le retour de l'éxécution de la fonction input de paramètre choisir l'endroit où l'on veut joueur
                # tant que caseJoueurPlay2 dans alreadyPlay
                    # alors  
                    # assigner à caseJoueurPlay le retour de l'éxécution de la fonction input de paramètre rechoisir l'endroit où l'on veut joueur
                # incrémenter alreadyPlay grâce grace au retour de l'éxécution la méthode append de paramètre caseJoueurPlay2
                # utiliser la fonction amplacementJoueur de paramètre caseJoueurPlay2 et joueurPlay2
                # incrémenter de -1 firstPlayer
                # assigner à coupJouer la variable caseJoueurPlay2

        # sinon 
            # alors
            # utiliser la méthode .sleep de paramètre 0.5
            # si firstPlayer vaut 0
                # alors
                # assigner à caseJoueurPlay1 le retour de l'éxécution de la fonction input de paramètre choisir l'endroit où l'on veut joueur
                # tant que caseJoueurPlay1 dans alreadyPlay
                    # alors  
                    # assigner à caseJoueurPlay1 le retour de l'éxécution de la fonction input de paramètre rechoisir l'endroit où l'on veut joueur
                # incrémenter alreadyPlay grâce grace au retour de l'éxécution la méthode append de paramètre caseJoueurPlay1
                # utiliser la fonction amplacementJoueur de paramètre caseJoueurPlay1 et joueurPlay1
                # incrémenter de 1 firstPlayer
                # assigner à coupJouer la variable caseJoueurPlay1
            
            # si sinon firstPlayer vaut la valeur 1
                # alors
                # tant que choixRobot dans alreadyPlay
                    # alors
                    # assigner à choixRobot le retour de l'éxécution de la fonction randint de paramètre 1, 9 etant un str
                # incrémenter alreadyPlay grâce grace au retour de l'éxécution la méthode append de paramètre choixRobot
                # utiliser la fonction amplacementJoueur de paramètre choixRobot et joueurPlay2
                # incrémenter de -1 firstPlayer
                # assigner à coupJouer la variable choixRobot

        # afficher la position que le joueur a séléctionné grâce à la variable coupJouer
        # utiliser la méthode .sleep de paramètre 0.5

        # si joueurPlay1 dans le retour de l'éxécution de la fonction Victoire() ou si joueurPlay2 dans le retour de l'éxécution de la fonction Victoire()
            # alors
            # renvoyer le retour de léxécution de la fonction whoWin
    
    # afficher "égalité"
    # renvoyer

# utilisation de la fonction game

# FIN