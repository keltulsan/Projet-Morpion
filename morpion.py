from random import *
from os import *
from time import *


system("cls")


taille = int(input("Choissisez la taille de la grille : "))

def tailleGrille(taille):
    """créer tableau de tableau de longueur rentré par l'utilisateur"""
    tab = [['□' for i in range(taille)]for j in range(taille)] 
    return tab



tab = tailleGrille(taille) 
longueurTab = len(tab)*len(tab)
joueurPlay1 = input("Joueur 1 choississez la figure que vous voulez jouer : ")
joueurPlay2 = choice(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]) # choix alea figure
alreadyPlay = [] 
firstPlayer = choice([0,1]) # choix du joueur qui commence
print(firstPlayer)


def printTab():
    """ Affiche le plateau du morpion comme le vrai jeu"""
    for i in tab:
        print(i)
    print('')

def emplacementJoueur (choix, coup_Joueur):
    """ Modifie l'emplacement dans le cadriallage du morpion par la figure du joueur choisi qui prend en paramètre l'emplacement choisi et la figure choisie par le joueur"""
    print(choix)
    if choix == "1" :
        tab[0][0] = coup_Joueur
    elif choix == "2" :
        tab[0][1] = coup_Joueur
    elif choix == "3" :
        tab[0][2] = coup_Joueur
    elif choix == "4" :
        tab[1][0] = coup_Joueur
    elif choix == "5" :
        tab[1][1] = coup_Joueur
    elif choix == "6" :
        tab[1][2] = coup_Joueur
    elif choix == "7" :
        tab[2][0] = coup_Joueur
    elif choix == "8" :
        tab[2][1] = coup_Joueur
    elif choix == "9" :
        tab[2][2] = coup_Joueur
    return printTab()
    

def Victoire():
    winTotale = [0 for i in range(8)] # [[789], [456], [123], [741], [852], [963], [753], [951]] #combinaison de win possible
                                      # [  0,     0,     0,     0,     0,     0,     0,     0  ]

     # regarde les victoires en lignes horizontales. 
    for i in range(3) :
        if joueurPlay1 in tab[i][0] and joueurPlay2 in tab[i][0] :
            winTotale[i] = -1
        elif '□' in tab[i][0] :
            pass
        else :
            winTotale[i] = tab[i][0]

    # regarde les victoires en lignes vertical. 
    for i in range(3) : 
        if joueurPlay1 in tab[0][i] and joueurPlay2 in tab[0][i] :
            winTotale[i] = -1
        elif '□' in tab[0][i] :
            pass
        else :
            winTotale[i + 3] = tab[0][i]

    # regarde les victoires en lignes diagonnales. 
    for i in range(0,3,2) : # debute a 0, jusquà 2, de 2 en 2 soit i vaudra 0 puis 2
        cpt = 0
        if i == 0 :
            for j in range(3):
                if joueurPlay1 in tab[i+cpt][j] and joueurPlay2 in tab[i+cpt][j] :
                    winTotale[i] = -1
                elif '□' in tab :
                    pass
                else :
                    winTotale[i + 6] = tab[0][i]
                cpt += 1
        elif i == 2:
                if joueurPlay1 in tab[i-cpt][j] and joueurPlay2 in tab[i-cpt][j] :
                    winTotale[i] = -1
                elif '□' in tab :
                    pass
                else :
                    winTotale[i-1 + 6] = tab[0][i]
    return winTotale
        
def whoWin():
    for i in Victoire() :
        if i == joueurPlay1 : 
            return print("Joueur 1 win")
        elif i == joueurPlay2:
            return print("Joueur 2 win")
        else :
            pass
    if "0" not in Victoire():
        return print("Egalité")

def game():
    global firstPlayer, joueurPlay2
    robot = input("Voulez vous jouer avec un bot ? [True or False] ")
    choixRobot = str(randint(1, 9))
    if robot == "False": joueurPlay2 = input("Joueur 2 choississez la figure que vous voulez jouer : ") #si pas robot alors le joueur 2 choisi la figure qu'il veut
    print(firstPlayer)
    while len(alreadyPlay) < longueurTab:

        if robot == "True" :

            if firstPlayer == 0 :
                caseJoueurPlay1 = input("Joueur 1 faite votre choix pour jouer : ") 
                while caseJoueurPlay1 in alreadyPlay:
                    caseJoueurPlay1 = input("Joueur 2 refaite votre choix pour jouer : ")
                alreadyPlay.append(caseJoueurPlay1)
                emplacementJoueur(caseJoueurPlay1, joueurPlay1) 
                firstPlayer +=1 #modifie le joueur qui va commencer 

            elif firstPlayer == 1 :   
                while choixRobot in alreadyPlay:
                    choixRobot = str(randint(1, 9)) 
                alreadyPlay.append(choixRobot)   
                emplacementJoueur(choixRobot, joueurPlay2) 
                firstPlayer -= 1 #modifie le joueur qui va commencer 
            
        elif robot == "False":
            
            if firstPlayer == 0 :
                caseJoueurPlay1 = input("Joueur 1 faite votre choix pour jouer : ") 
                while caseJoueurPlay1 in alreadyPlay:
                    caseJoueurPlay1 = input("Joueur 2 refaite votre choix pour jouer : ")
                alreadyPlay.append(caseJoueurPlay1)
                emplacementJoueur(caseJoueurPlay1, joueurPlay1 ) 
                firstPlayer +=1 #modifie le joueur qui va commencer 
                

            elif firstPlayer == 1 :
                caseJoueurPlay2 =  input("Joueur 2 faite votre choix pour jouer : ")
                while caseJoueurPlay2 in alreadyPlay:
                    caseJoueurPlay2 = input("Joueur 2 refaite votre choix pour jouer : ")
                alreadyPlay.append(caseJoueurPlay2)
                emplacementJoueur(caseJoueurPlay2, joueurPlay2) 
                firstPlayer -=1 #modifie le joueur qui va commencer 

            
        if joueurPlay1 in Victoire() or joueurPlay2 in Victoire(): # si un joueur a gagné renvoie le victorieux
            return whoWin()
            
        
        
        print(alreadyPlay)


game()          
