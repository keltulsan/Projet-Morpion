from random import *
import os
import time



command = 'cls' #for windows
os.system(command)


taille = 3

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
print("Vous joueurez en " + str(firstPlayer) + " - - - - - [0 : Vous commencez et 1 : Vous jouerez en second]")


def printTab():
    """ Affiche le plateau du morpion comme le vrai jeu"""
    for i in tab:
        print(i)
    print('')

def emplacementJoueur (choix, coup_Joueur):
    """ Modifie l'emplacement dans le cadriallage du morpion par la figure du joueur choisi qui prend en paramètre l'emplacement choisi et la figure choisie par le joueur"""
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
    for i in range(3):
        if joueurPlay1 in tab[i] and joueurPlay2 in tab[i]:
            winTotale[i] = -1
        elif '□' in tab[i]:
            pass
        else:
            winTotale[i] = tab[i][0]

    # regarde les victoires en lignes verticales. 
    for i in range(3):
        if joueurPlay1 in [tab[j][i] for j in range(3)] and joueurPlay2 in [tab[j][i] for j in range(3)]:
            winTotale[i + 3] = -1
        elif '□' in [tab[j][i] for j in range(3)]:
            pass
        else:
            winTotale[i + 3] = tab[0][i]

    # regarde les victoires en lignes en diagonales. 
    for i in range(2):
        if joueurPlay1 in [tab[j][(2 - j) * i - j * (i - 1)] for j in range(3)] and joueurPlay2 in [tab[j][(2 - j) * i - j * (i - 1)] for j in range(3)]:
            winTotale[i + 6] = -1
        elif '□' in [tab[j][(2 - j) * i - j * (i - 1)] for j in range(3)]:
            pass
        else:
            winTotale[i + 6] = tab[0][i * 2]

    return winTotale
        
def whoWin():
    for i in Victoire() :
        if i == joueurPlay1 : 
            return print("Victoire du Joueur 1")
        elif i == joueurPlay2:
            return print("Victoire du  Joueur 2")
        else : 
            pass

def game():
    global firstPlayer, joueurPlay2
    robot = input("Voulez vous jouer avec un bot ? [True or False] ")
    coupJouer = ""
    choixRobot = str(randint(1, 9))

    if robot == "False": 
        print("Vous avez choisi le mode multijoueur \n \n")
        joueurPlay2 = input("Joueur 2 choississez la figure que vous voulez jouer : \n") #si pas robot alors le joueur 2 choisi la figure qu'il veut
        while joueurPlay1 == joueurPlay2 :
            joueurPlay2 = input("Joueur 2 rechoississez la figure que vous voulez jouer : ")
            print("\n")
    
    else : 
         print("Vous avez choisi le mode contre L'IA \n \n")

    printTab()
    while len(alreadyPlay) < longueurTab:

        if robot == "False":
            time.sleep(0.3)
            if firstPlayer == 0 :
                caseJoueurPlay1 = input("Joueur 1 faite votre choix pour jouer : ") 
                print("\n")
                while caseJoueurPlay1 in alreadyPlay:
                    caseJoueurPlay1 = input("Joueur 1 refaite votre choix pour jouer : ")
                    print("\n")
                alreadyPlay.append(caseJoueurPlay1)
                emplacementJoueur(caseJoueurPlay1, joueurPlay1 ) 
                firstPlayer +=1 #modifie le joueur qui va commencer 
                coupJouer = caseJoueurPlay1
                
            elif firstPlayer == 1 :
                caseJoueurPlay2 =  input("Joueur 2 faite votre choix pour jouer : ")
                print("\n")
                while caseJoueurPlay2 in alreadyPlay:
                    caseJoueurPlay2 = input("Joueur 2 refaite votre choix pour jouer : ")
                    print("\n")
                alreadyPlay.append(caseJoueurPlay2)
                emplacementJoueur(caseJoueurPlay2, joueurPlay2) 
                firstPlayer -=1 #modifie le joueur qui va commencer 
                coupJouer = caseJoueurPlay2

        else :
            time.sleep(0.5)
            if firstPlayer == 0 :
                caseJoueurPlay1 = input("Joueur 1 faite votre choix pour jouer : ") 
                print("\n")
                while caseJoueurPlay1 in alreadyPlay:
                    caseJoueurPlay1 = input("Joueur 2 refaite votre choix pour jouer : ")
                    print("\n")
                alreadyPlay.append(caseJoueurPlay1)
                emplacementJoueur(caseJoueurPlay1, joueurPlay1) 
                firstPlayer +=1 #modifie le joueur qui va commencer 
                coupJouer = caseJoueurPlay1

            elif firstPlayer == 1 :   
                while choixRobot in alreadyPlay:
                    choixRobot = str(randint(1, 9)) 
                alreadyPlay.append(choixRobot)   
                emplacementJoueur(choixRobot, joueurPlay2) 
                firstPlayer -= 1 #modifie le joueur qui va commencer 
                coupJouer = choixRobot

        print("La position " + str(coupJouer) + " a été selectionnée \n")
        time.sleep(0.5) 
        
        

            
        if joueurPlay1 in Victoire() or joueurPlay2 in Victoire() : # si un joueur a gagné renvoie le victorieux ou si toutes les cases ont étaient prises renvoie égalité
            return whoWin()


    print("Egalité")
    return 
            
        
        
    


game()          
