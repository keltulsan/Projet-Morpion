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
            # la valeur de tab d'indices i et j vaut le str de cpt
            # incrémenter cpt de 1
    # renvoyer tab

# definir la fonction position 
    # initialiser tab qui est le retour de la fonction tailleGrille de paramètre taille
    # initialiser cpt à 1
    # pour i dans le retour de l'éxécution range de paramètre taille
        # alors
        # pour j dans le retour de l'éxécution range de paramètre taille
            # alors
            # incrémentre à tab de position i et j la str de cpt
            # incrémenter cpt de 1
    # renvoyer tab 

# initialiser tab avec le retour de l'éxécution de la fonction tailleGrille de paramètre taille
# initialiser de tabFictif un tableau de tableau rempli avec le charactère '□' par compréhension de longueur taille ##[['□' for i in range(taille)]for j in range(taille)] 
# initialiser de tabReussite un tableau rempli avec les emplacements jouables ## ["1", "2", "3", "4", "5", "6", "7", "8", "9", "123456789"]

# initialiser password qui vaut la str "Ichiban tsuyoi"
# initialiser easterEgg qui vaut la str "Hard"

# initialiser longueurTab la longueur du tableau tab multiplier par la longueur du tableau tab
# initialiser joueurPlay1 qui est le retour de l'éxécution de la fonction input de paramètre la figure choisie

# tant que joueurPlay1 est dans la liste des entiers de 1 à 9 rentré comme des str  ##[str(i) for i in range(1, 10)]
    # on assigne a joueurPlay1 le retour de l'éxécution de la fonction input de paramètre la figure choisie de nouveau

# initialiser joueurPlay2 qui est le retour de l'éxécution de la fonction choice de paramètre un tableau composé de l'alphabet en majuscule
# si joueurPlay2 vaut joueurPlay1 :
    # alors
    # asigner joueurPlay2 qui est le retour de l'éxécution de la fonction choice de paramètre un tableau composé de l'alphabet en majuscule

# initialiser alreadyPlay comme étant un tableau vide
# initialiser firstPlayer qui est le retour de l'éxécution de la fonction choice de paramètre un tableau composé de 1 et 2
# afficher le joueur jouant en premier 

# definir la fonction afficher
    # initialiser grille qui vaut la str d'un saut de ligne ##"\n"
    # pour i dans le retour de l'éxécution de la fonction range de paramètre taille
        # alors
        # pour j dans le retour de l'éxécution de la fonction range de paramètre taille
            # alors
            # incrémenter grille du str "| " puis concatainer la valeur de tab d'indices i et j puis container la str  " "
        # incrémenter grille du str "|"
        # incrémenter grille de la str " \n- - - - - - -\n"
    # afficher grille


# definir emplacementJoueur de paramètres choix et coup_Joueur
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
    # si sinon choix vaut la str vaut "123456789"
        # alors
        # pour i qui est le retour de l'éxécution de la fonction range de paramètres 3
            # alors
            # pour i qui est le retour de l'éxécution de la fonction range de paramètres 3
                # alors
                # assigner à la valeur de tab de coordonnées tab[i][j] la valeur de coup_Joueur
                # assigner à la valeur de tabFictif de coordonnées tab[i][j] la valeur de coup_Joueur
    # renvoyer l'affichage du retour de l'éxécution de la fonction afficher


# définir la fonction victoire 
    # initialiser la variable winTotale comme étant un tableau de longueur 8 rempli de 0 
    ## [[789], [456], [123], [741], [852], [963], [753], [951]] #combinaison de win possible
    ## [  0,     0,     0,     0,     0,     0,     0,     0  ]

    # """Regarde les victoires en lignes horizontales. """
    # pour i prennant les valeurs 0,1,2
        # si joueurPlay1 dans tabFictif d'indice i et joueurPlay2 dans tabFictif d'indice i
            # alors
            # incrémenter winTotale à l'indice i la valeur -1
        # si sinon le caractère '□' est dans tabFictif d'indice i
            # alors
            # pass
        # sinon
            # alors
            # incrémenter winTotale à l'indice i la valeur de tab d'indices i et 0

    # """Regarde les victoires en lignes verticales."""
    # pour i prennant les valeurs 0,1,2
        # si joueurPlay1 dans un nouveau tableau de valeur tabFictif d'indices j et i, pour j dans les valeurs 0,1,2 et joueurPlay2 dans un nouveau tableau de valeur tabFictif d'indices
        # j et i, pour j dans les valeurs 0,1,2
            # alors
            # incrémenter winTotale à l'indice i + 3 la valeur -1
        # si sinon le caractère '□' est dans un nouveau tableau de valeur tabFictif d'indices j et i, pour j dans les valeurs 0,1,2
            # alors
            # pass
        # sinon
            # alors
            # incrémenter winTotale à l'indice i + 3 la valeur de tab d'indices 0 et i
    
    # """Regarde les victoires en lignes en diagonales."""
    # pour i prennant les valeurs 0,1
        # si joueurPlay1 dans un nouveau tableau de valeur tabFictif d'indices j et [(2 - j) * i - j * (i - 1)],  pour j dans les valeurs 0,1,2 
        # et joueurPlay2 dans un nouveau tableau de valeur tabFictif d'indices j et [(2 - j) * i - j * (i - 1)],  pour j dans les valeurs 0,1,2 
            # alors
            # incrémenter winTotale à l'indice i + 6 la valeur -1
        # si sinon le caractère '□' est dans un nouveau tableau de valeur tabFictif d'indices j et [(2 - j) * i - j * (i - 1)],  pour j dans les valeurs 0,1,2 
            # alors
            # pass
        # sinon
            # alors
            # incrémenter winTotale à l'indice i + 6 la valeur de tab d'indices 0 et i * 2
    
    # renvoyer winTotale
     

# definir la fonction whoWin
    # pour i dans Victoire 
        # si i vaut la valeur de joueurPlay1
            # alors
            # renvoyer l'affichage "Victoire du joueur 1"
        # si sinon i vaut la valeur de joueurPlay2
            # alors
            # renvoyer l'affichage "Victoire du joueur 2"

#définir la fonction IA de paramètre dificultie
    #assigner à cptJ1 la valeur 0
    #assigner à cptJ2 la valeur 0
    #initialiser choixIA en lui attribuant une valeur vide
    #initialiser mot qui vaut un mot vide

'''regarder dans les lignes si l'un des deux joueur a 2 fois sont symboles'''
    #pour i dans le retour de l'éxécution de la fonction range de paramètre 3
        #attribuer à cptJ2 le retour de l'execution de la fonction count de parametre joueurPlay2 à partir d'un nouveau tableau rempli des valeurs de tabFictif d'indice i et j
        #pour j dans le retour de l'execution de la fonction range de parametre 3
        #si cptJ2 est égal à 2
            #alors
            #pour x dans le retour de l'éxécution de la fonction range de paramètre 3
                #si la valeur de tabFictif d'indices i et x vaut "□"
                    #alors
                    # si dificultie vaut la str "Hard" 
                        # alors 
                        # assigner à mot le retour de l'éxécution de la fonction input de paramètre le mot de passe
                        # si mot est égale à password
                            # alors
                            # renvoyer    
                    #attribuer à choixIA la valeur de tableauPosition d'indices i et x
                    #retourner la chaine de caractere de choixIA
                
    #pour i dans le retour de l'éxécution de la fonction range de paramètre 3
        #attribuer à cptJ1 le retour de l'execution de la fonction count de parametre joueurPlay1 à partir d'un nouveau tableau rempli des valeurs de tabFictif d'indice i et j
        #pour j dans le retour de l'execution de la fonction range de parametre 3
        #si cptJ1 est égal à 2
            #alors
            #pour x dans le retour de l'éxécution de la fonction range de paramètre 3
                #si la valeur de tabFictif d'indices i et x vaut "□"
                    #alors
                    #attribuer à choixIA la valeur de tableauPosition d'indices i et x
                    #retourner la chaine de caractere de choixIA

'''regarder dans les colonnes si l'un des deux joueur a 2 fois sont symboles'''
    #pour i dans le retour de l'éxécution de la fonction range de paramètre 3
        #attribuer à cptJ2 le retour de l'execution de la fonction count de parametre joueurPlay2 à partir d'un nouveau tableau rempli des valeurs de tabFictif d'indice j et i
        #pour j dans le retour de l'execution de la fonction range de parametre 3
        #si cptJ2 est égal à 2
            #alors
            #pour x dans le retour de l'éxécution de la fonction range de paramètre 3
                #si la valeur de tabFictif d'indices x et i vaut "□"
                    #alors
                    # si dificultie vaut la str "Hard" 
                        # alors 
                        # assigner à mot le retour de l'éxécution de la fonction input de paramètre le mot de passe
                        # si mot est égale à password
                            # alors
                            # renvoyer    
                    #attribuer à choixIA la valeur de tableauPosition d'indices x et i
                    #retourner la chaine de caractere de choixIA

    #pour i dans le retour de l'éxécution de la fonction range de paramètre 3
        #attribuer à cptJ1 le retour de l'execution de la fonction count de parametre joueurPlay1 à partir d'un nouveau tableau rempli des valeurs de tabFictif d'indice j et i
        #pour j dans le retour de l'execution de la fonction range de parametre 3
        #si cptJ1 est égal à 2
            #alors
            #pour x dans le retour de l'éxécution de la fonction range de paramètre 3
                #si la valeur de tabFictif d'indices x et i vaut "□"
                    #alors
                    #attribuer à choixIA la valeur de tableauPosition d'indices x et i
                    #retourner la chaine de caractere de choixIA

'''regarder dans les diagonales si l'un des deux joueur a 2 fois sont symboles'''
    #pour i dans le retour de l'éxécution de la fonction range de paramètre 2
        #attribuer à cptJ2 le retour de l'execution de la fonction count de parametre joueurPlay2 à partir d'un nouveau tableau rempli des valeurs de tabFictif d'indice j et (2 - j) * i - j * (i - 1)
        #pour j dans le retour de l'execution de la fonction range de parametre 3
        #si cptJ2 est égal à 2
            #alors
            #pour x dans le retour de l'éxécution de la fonction range de paramètre 3
                #si la valeur de tabFictif d'indices x et (2 - x) * i - x * (i - 1) vaut "□"
                    #alors
                    # si dificultie vaut la str "Hard" 
                        # alors 
                        # assigner à mot le retour de l'éxécution de la fonction input de paramètre le mot de passe
                        # si mot est égale à password
                            # alors
                            # renvoyer    
                    #attribuer à choixIA la valeur de tableauPosition d'indices x et (2 - x) * i - x * (i - 1)
                    #retourner la chaine de caractere de choixIA

     #pour i dans le retour de l'éxécution de la fonction range de paramètre 2
        #attribuer à cptJ1 le retour de l'execution de la fonction count de parametre joueurPlay1 à partir d'un nouveau tableau rempli des valeurs de tabFictif d'indice j et (2 - j) * i - j * (i - 1)
        #pour j dans le retour de l'execution de la fonction range de parametre 3
        #si cptJ1 est égal à 2
            #alors
            #pour x dans le retour de l'éxécution de la fonction range de paramètre 3
                #si la valeur de tabFictif d'indices x et (2 - x) * i - x * (i - 1) vaut "□"
                    #alors
                    #attribuer à choixIA la valeur de tableauPosition d'indices x et (2 - x) * i - x * (i - 1)
                    #retourner la chaine de caractere de choixIA

'''regarder dans les colonnes si l'IA à son symbole présent une seule fois et le joueur n'a aucun symbole sur la ligne'''
    #pour i dans le retour de l'éxécution de la fonction range de paramètre 2
        #attribuer à cptJ1 le retour de l'execution de la fonction count de parametre joueurPlay1 à partir d'un nouveau tableau rempli des valeurs de tabFictif d'indice j et (2 - j) * i - j * (i - 1)
        #pour j dans le retour de l'execution de la fonction range de parametre 3
        #attribuer à cptJ2 le retour de l'execution de la fonction count de parametre joueurPlay2 à partir d'un nouveau tableau rempli des valeurs de tabFictif d'indice j et (2 - j) * i - j * (i - 1)
        #pour j dans le retour de l'execution de la fonction range de parametre 3
        #si cptJ2 est égal à 1 et cptJ1 est égal à 0
            #alors
            #pour x dans le retour de l'éxécution de la fonction range de paramètre 3
                #si la valeur de tabFictif d'indices x et (2 - x) * i - x * (i - 1) vaut "□"
                    #alors
                    #attribuer à choixIA la valeur de tableauPosition d'indices x et (2 - x) * i - x * (i - 1)
                    #retourner la chaine de caractere de choixIA

'''regarder dans les lignes si l'IA à son symbole présent une seule fois et le joueur n'a aucun symbole sur la ligne alors l'IA se mettra à coté de son symbole déjà présent'''
    #pour i dans le retour de l'éxécution de la fonction range de paramètre 3
        #attribuer à cptJ1 le retour de l'execution de la fonction count de parametre joueurPlay1 à partir d'un nouveau tableau rempli des valeurs de tabFictif d'indice i et j
        #pour j dans le retour de l'execution de la fonction range de parametre 3
        #attribuer à cptJ2 le retour de l'execution de la fonction count de parametre joueurPlay2 à partir d'un nouveau tableau rempli des valeurs de tabFictif d'indice i et j
        #pour j dans le retour de l'execution de la fonction range de parametre 3
        #si cptJ2 est égal à 1 et cptJ1 est égal à 0
            #alors
            #pour x dans le retour de l'éxécution de la fonction range de paramètre 3
                #si la valeur de tabFictif d'indices i et x vaut "□"
                    #alors
                    #attribuer à choixIA la valeur de tableauPosition d'indices i et x
                    #retourner la chaine de caractere de choixIA

'''regarder dans les colonnes si l'IA à son symbole présent une seule fois et le joueur n'a aucun symbole sur la ligne'''
    #pour i dans le retour de l'éxécution de la fonction range de paramètre 3
        #attribuer à cptJ1 le retour de l'execution de la fonction count de parametre joueurPlay1 à partir d'un nouveau tableau rempli des valeurs de tabFictif d'indice j et i
        #pour j dans le retour de l'execution de la fonction range de parametre 3
        #attribuer à cptJ2 le retour de l'execution de la fonction count de parametre joueurPlay2 à partir d'un nouveau tableau rempli des valeurs de tabFictif d'indice j et i
        #pour j dans le retour de l'execution de la fonction range de parametre 3
        #si cptJ2 est égal à 1 et cptJ1 est égal à 0
            #alors
            #pour x dans le retour de l'éxécution de la fonction range de paramètre 3
                #si la valeur de tabFictif d'indices x et i vaut "□"
                    #alors
                    #attribuer à choixIA la valeur de tableauPosition d'indices x et i
                    #retourner la chaine de caractere de choixIA

'''regarder si le centre est libre sinon si les coins sont libres'''
    #si la valeur de tabFictif d'indices 1 et 1 vaut "□"
        #alors
        #attribuer à choixIA la valeur de tableauPosition d'inidices 1 et 1
        #retourner la chaine de caractere de choixIA
    #sinon
        #alors
        #si la valeur de tabFictif d'indices 0 et 0 vaut "□"
            #alors
            #attribuer à choixIA la valeur de tableauPosition d'inidices 0 et 0
            #retourner la chaine de caractere de choixIA
        #sinon si la valeur de tabFictif d'indices 0 et 2 vaut "□"
            #alors
            #attribuer à choixIA la valeur de tableauPosition d'inidices 0 et 2
            #retourner la chaine de caractere de choixIA
        #sinon si la valeur de tabFictif d'indices 2 et 0 vaut "□"
            #alors
            #attribuer à choixIA la valeur de tableauPosition d'inidices 2 et 0
            #retourner la chaine de caractere de choixIA
        #sinon si la valeur de tabFictif d'indices 2 et 2 vaut "□"
            #alors
            #attribuer à choixIA la valeur de tableauPosition d'inidices 2 et 2
            #retourner la chaine de caractere de choixIA

    # assigner à choixIA la valeur du retour de l'éxécution de la fonction choice de paramètre tableauReussite sans la dernière valeur de ce tableau
    # tant que choixIA dans alreadyPlay 
        # alors
        # assigner à choixIA la valeur du retour de l'éxécution de la fonction choice de paramètre tableauReussite sans la dernière valeur de ce tableau  
    # renvoyer choixIA    

# definir la fonction game
    # appelle de global avec les variables firstPlayer et joueurPlay2
    # initialisation de robot qui est le retour de l'éxécution de la fonction input "voulez vous joueur avec un bot ? [True or FAlse]"
    # initialisation de coupJoueur comme étant un mot vide
    # initialisation de choixRobot qui est le retour de l'éxécution de la fonction randint de paramètre 1, 9 etant un str

    # si robot vaut la str "False" 
        # alors 
        # afficher "Vous avez choisi le mode multijoueur"
        # modifie joueurPlay2 qui est le retour de l'éxécution de la fonction input de paramètre la figure choisie*
        # tant que joueurPlay1 vaut joueurPlay2 ou si joueurPlay2 et dans est dans la liste des entiers de 1 à 9 rentré comme des str
            # alors
            # modifie joueurPlay2 qui est le retour de l'éxécution de la fonction input de paramètre la figure rechoisie*
    # sinon
        # alors 
        # afficher "Vous avez choisi le mode contre L'IA"

    # appelle de la fonction afficher

    # tant que la longueur de alreadyPlay est inférieur à longueurTab
        # alors
        # si robot vaut la str "False"
            # alors
            # si "1" dans alreadyPlay and "3" dans alreadyPlay and "7" dans alreadyPlay and "8" dans alreadyPlay and "9" dans alreadyPlay and not  "2" dans alreadyPlay and not  "4" dans alreadyPlay and not  "5" dans alreadyPlay" and not  "6" dans alreadyPlay
                # alors
                # renvoyer l'affichage de la str ":-)"
            # utiliser la méthode .sleep de paramètre 0.3
            # si firstPlayer vaut 1
                # alors
                # assigner à caseJoueurPlay1 le retour de l'éxécution de la fonction input de paramètre choisir l'endroit où l'on veut joueur
                # tant que caseJoueurPlay1 dans alreadyPlay ou si caseJoueurPlay1 n'est pas dans tableauReussite 
                    # alors  
                    # assigner à caseJoueurPlay1 le retour de l'éxécution de la fonction input de paramètre rechoisir l'endroit où l'on veut joueur
                # incrémenter alreadyPlay avec le retour de l'éxécution la méthode append de paramètre caseJoueurPlay1
                # utiliser la fonction amplacementJoueur de paramètre caseJoueurPlay1 et joueurPlay1
                # incrémenter de 1 firstPlayer
                # assigner à coupJouer la variable caseJoueurPlay1

            # si sinon firstPlayer vaut 2
                # alors
                # assigner à caseJoueurPlay2 le retour de l'éxécution de la fonction input de paramètre choisir l'endroit où l'on veut joueur
                # tant que caseJoueurPlay2 dans alreadyPlay ou si caseJoueurPlay2 n'est pas dans tableauReussite 
                    # alors  
                    # assigner à caseJoueurPlay le retour de l'éxécution de la fonction input de paramètre rechoisir l'endroit où l'on veut joueur
                # incrémenter alreadyPlay avec le retour de l'éxécution la méthode append de paramètre caseJoueurPlay2
                # utiliser la fonction amplacementJoueur de paramètre caseJoueurPlay2 et joueurPlay2
                # incrémenter de -1 firstPlayer
                # assigner à coupJouer la variable caseJoueurPlay2

        # sinon 
            # alors
            # utiliser la méthode .sleep de paramètre 0.5
            # si firstPlayer vaut 1
                # alors
                # assigner à caseJoueurPlay1 le retour de l'éxécution de la fonction input de paramètre choisir l'endroit où l'on veut joueur
                # tant que caseJoueurPlay1 dans alreadyPlay ou si caseJoueurPlay1 n'est pas dans tableauReussite 
                    # alors  
                    # assigner à caseJoueurPlay1 le retour de l'éxécution de la fonction input de paramètre rechoisir l'endroit où l'on veut joueur
                # incrémenter alreadyPlay avec le retour de l'éxécution la méthode append de paramètre caseJoueurPlay1
                # utiliser la fonction amplacementJoueur de paramètre caseJoueurPlay1 et joueurPlay1
                # incrémenter de 1 firstPlayer
                # assigner à coupJouer la variable caseJoueurPlay1
            
            # si sinon firstPlayer vaut la valeur 2
                # alors
                # assigner à choixRobot le retour de l'éxécution de la fontion IA de paramètre un mot vide ## ou easterEgg selon le cas
                # incrémenter alreadyPlay avec le retour de l'éxécution la méthode append de paramètre choixRobot
                # utiliser la fonction amplacementJoueur de paramètre choixRobot et joueurPlay2
                # incrémenter de -1 firstPlayer
                # assigner à coupJouer la variable choixRobot

        # afficher la position que le joueur a séléctionné grâce à la variable coupJouer
        # utiliser la méthode .sleep de paramètre 0.5

        # si joueurPlay1 dans le retour de l'éxécution de la fonction Victoire() ou si joueurPlay2 dans le retour de l'éxécution de la fonction Victoire()
            # alors
            # renvoyer le retour de l'éxécution de la fonction whoWin
    
    # afficher "égalité"
    # renvoyer

# utilisation de la fonction game

# FIN
