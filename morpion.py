from random import *
import os
import time

taille = 3


def tailleGrille(taille):
    """créer tableau de tableau de longueur rentré par l'utilisateur"""
    cpt = 1
    tab = [['□' for i in range(taille)] for j in range(taille)]
    for i in range(taille):
        for j in range(taille):
            tab[i][j] = str(cpt)
            cpt += 1
    return tab


def position() :
    """Renvoie un tableau de tableau composé de la position des choix, comme 1 qui est la position en haut à droite"""
    tab = tailleGrille(taille)
    cpt = 1
    for i in range(3): 
        for j in range(3):
            tab[i][j] = str(cpt)
            cpt += 1
    return tab

tab = tailleGrille(taille) 
tabFictif = [['□' for i in range(taille)]for j in range(taille)]
tableauReussite = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "123456789"]
tableauPosition = position()

longueurTab = len(tab)*len(tab)
joueurPlay1 = input("Joueur 1 choississez la figure que vous voulez jouer : ")

while joueurPlay1 in [str(i) for i in range(1, 10)]:
    joueurPlay1 = input("Joueur 1 rechoississez la figure que vous voulez jouer : ")

joueurPlay2 = choice(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]) # choix alea figure
if joueurPlay2 == joueurPlay1 :
    joueurPlay2 = choice(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])

alreadyPlay = [] 
firstPlayer = choice([1,2]) # choix du joueur qui commence
print("Vous joueurez en " + str(firstPlayer) + " - - - - - [1 : Vous commencez et 2 : Vous jouerez en second]")


def afficher():
    """ Affiche le plateau du morpion comme le vrai jeu"""
    grille = "\n"
    for i in range(taille):
        for j in range(taille):
            grille += "| " + tab[i][j] + " "
        grille += "|"
        grille += " \n- - - - - - -\n"
    print(grille)
            

def emplacementJoueur (choix, coup_Joueur):
    """ Modifie l'emplacement dans le cadriallage du morpion par la figure du joueur choisi qui prend en paramètre l'emplacement choisi et la figure choisie par le joueur"""
    if choix == "1" :
        tab[0][0] = coup_Joueur
        tabFictif[0][0] = coup_Joueur
    elif choix == "2" :
        tab[0][1] = coup_Joueur
        tabFictif[0][1] = coup_Joueur
    elif choix == "3" :
        tab[0][2] = coup_Joueur
        tabFictif[0][2] = coup_Joueur
    elif choix == "4" :
        tab[1][0] = coup_Joueur
        tabFictif[1][0] = coup_Joueur
    elif choix == "5" :
        tab[1][1] = coup_Joueur
        tabFictif[1][1] = coup_Joueur
    elif choix == "6" :
        tab[1][2] = coup_Joueur
        tabFictif[1][2] = coup_Joueur
    elif choix == "7" :
        tab[2][0] = coup_Joueur
        tabFictif[2][0] = coup_Joueur
    elif choix == "8" :
        tab[2][1] = coup_Joueur
        tabFictif[2][1] = coup_Joueur
    elif choix == "9" :
        tab[2][2] = coup_Joueur
        tabFictif[2][2] = coup_Joueur
    elif choix == "123456789" :
        for i in range(3):
            for j in range(3):
                tab[i][j] = coup_Joueur
                tabFictif[i][j] = coup_Joueur
    return afficher()


def Victoire():
    """Cette fonction regarde toutes les possibilités de gagner une partie. Les lignes, les colonnes, les diagonales
    Renvoie un tableau de valeurs qui peut être composé de 0, -1 et le symbole du joueur qui as réussi à gagner"""
    winTotale = [0 for i in range(8)] # [[789], [456], [123], [741], [852], [963], [753], [951]] #combinaison de win possible
                                      # [  0,     0,     0,     0,     0,     0,     0,     0  ]
     # regarde les victoires en lignes horizontales. 
    for i in range(3):
        if joueurPlay1 in tabFictif[i] and joueurPlay2 in tabFictif[i]:
            winTotale[i] = -1
        elif '□' in tabFictif[i] :
            pass
        else:
            winTotale[i] = tab[i][0]

    # regarde les victoires en lignes verticales. 
    for i in range(3):
        if joueurPlay1 in [tabFictif[j][i] for j in range(3)] and joueurPlay2 in [tabFictif[j][i] for j in range(3)]:
            winTotale[i + 3] = -1
        elif '□' in [tabFictif[j][i] for j in range(3)]:
            pass
        else:
            winTotale[i + 3] = tab[0][i]

    # regarde les victoires en lignes en diagonales. 
    for i in range(2):
        if joueurPlay1 in [tabFictif[j][(2 - j) * i - j * (i - 1)] for j in range(3)] and joueurPlay2 in [tabFictif[j][(2 - j) * i - j * (i - 1)] for j in range(3)]:
            winTotale[i + 6] = -1
        elif '□' in [tabFictif[j][(2 - j) * i - j * (i - 1)] for j in range(3)]:
            pass
        else:
            winTotale[i + 6] = tab[0][i * 2]
    return winTotale
        

def whoWin():
    """Cette fonction va vérifier si l'un des deux joueurs a gagner et le renverra"""
    for i in Victoire() :
        if i == joueurPlay1 : 
            return print("Victoire du Joueur 1")
        elif i == joueurPlay2:
            return print("Victoire du Joueur 2")


def game():
    """Création d'une partie de morpion qui peut se joueur à 2 ou seul avec une IA"""
    global firstPlayer, joueurPlay2
    robot = input("Voulez vous jouer avec un bot ? [True or False] ")
    coupJouer = ""
    choixRobot = str(randint(1,9))

    if robot == "False": 
        print("Vous avez choisi le mode multijoueur \n \n")
        joueurPlay2 = input("Joueur 2 choississez la figure que vous voulez jouer : ") #si pas robot alors le joueur 2 choisi la figure qu'il veut
        print("\n")
        while joueurPlay1 == joueurPlay2 or joueurPlay2 in [str(i) for i in range(1, 10)]:
            joueurPlay2 = input("Joueur 2 rechoississez la figure que vous voulez jouer : ")
            print("\n")
    
    else : 
         print("Vous avez choisi le mode contre L'IA \n \n")
    afficher()

    while len(alreadyPlay) < longueurTab:
        if robot == "False":
            if "1" in alreadyPlay and "3" in alreadyPlay and "7" in alreadyPlay and "8" in alreadyPlay and "9" in alreadyPlay and not "2" in alreadyPlay and not "4" in alreadyPlay and not "5" in alreadyPlay and not "6" in alreadyPlay :
                smile =  " :-) "      
                return print(smile)
            time.sleep(0.3)
            if firstPlayer == 1 :
                caseJoueurPlay1 = input("Joueur 1 faite votre choix pour jouer : ") 
                print("\n")
                while caseJoueurPlay1 in alreadyPlay or not caseJoueurPlay1 in tableauReussite :
                    caseJoueurPlay1 = input("Joueur 1 refaite votre choix pour jouer : ")
                    print("\n")
                alreadyPlay.append(caseJoueurPlay1)
                emplacementJoueur(caseJoueurPlay1, joueurPlay1 ) 
                firstPlayer +=1 #modifie le joueur qui va commencer 
                coupJouer = caseJoueurPlay1
                
            elif firstPlayer == 2 :
                caseJoueurPlay2 =  input("Joueur 2 faite votre choix pour jouer : ")
                print("\n")
                while caseJoueurPlay2 in alreadyPlay or not caseJoueurPlay2 in tableauReussite :
                    caseJoueurPlay2 = input("Joueur 2 refaite votre choix pour jouer : ")
                    print("\n")
                alreadyPlay.append(caseJoueurPlay2)
                emplacementJoueur(caseJoueurPlay2, joueurPlay2) 
                firstPlayer -=1 #modifie le joueur qui va commencer 
                coupJouer = caseJoueurPlay2

        else :
            time.sleep(0.5)
            if firstPlayer == 1 :
                caseJoueurPlay1 = input("Joueur 1 faite votre choix pour jouer : ") 
                print("\n")
                while caseJoueurPlay1 in alreadyPlay or not caseJoueurPlay1 in tableauReussite :
                    caseJoueurPlay1 = input("Joueur 1 refaite votre choix pour jouer : ")
                    print("\n")
                alreadyPlay.append(caseJoueurPlay1)
                emplacementJoueur(caseJoueurPlay1, joueurPlay1) 
                print(tabFictif)
                firstPlayer +=1 #modifie le joueur qui va commencer 
                coupJouer = caseJoueurPlay1

            elif firstPlayer == 2 :  
                while choixRobot in alreadyPlay :
                    choixRobot = str(randint(1,9))
                alreadyPlay.append(choixRobot)
                emplacementJoueur(choixRobot, joueurPlay2) 
                print(tabFictif)
                firstPlayer -= 1 #modifie le joueur qui va commencer 
                coupJouer = choixRobot

        print("La position " + str(coupJouer) + " a été selectionnée \n")
        time.sleep(0.5) 
        
        if joueurPlay1 in Victoire() or joueurPlay2 in Victoire() : # si un joueur a gagné renvoie le victorieux ou si toutes les cases ont étaient prises renvoie égalité
            return whoWin()

    print("Egalité")
    return 
            
game() 
