from random import *
import os
import time
import turtle as t

t.setup(800,700,600,100)  #Largeur : 800px, Hauteur : 700px, position écran x : 700px, pos y : 100px
t.title("Morpion by Ewen et Naëlle")  #Change le titre
t.up()
t.setpos(-300, 300) #position au départ
t.speed(0)
r = 70

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
    """ Affiche le plateau du morpion comme le vrai jeu"""
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
emplacementWin = ""
numEmplacement = ""

longueurTab = len(tab)*len(tab)
joueurPlay1 = (input("Joueur 1 choississez la figure que vous voulez jouer : "))
joueurPlay1 = joueurPlay1.upper()

while not joueurPlay1 in ["O", "X"]:
    joueurPlay1 = input("Joueur 1 rechoississez la figure que vous voulez jouer. Vous pouveza choisir O et X : ")
    joueurPlay1 = joueurPlay1.upper()

if joueurPlay1 == "X":
    joueurPlay2 = "O"
else:
    joueurPlay2 = "X"

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
    cpt = 1
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
            t.clear()
            t.setpos(-300, 300)
            t.right(90)
            grille_turtle()
            for i in range(3):
                for j in range(3):
                    tab[i][j] = coup_Joueur
                    tabFictif[i][j] = coup_Joueur
                    position_letter(str(cpt),coup_Joueur)
                    cpt+=1
    return afficher()


def Victoire():
    """Cette fonction regarde toutes les possibilités de gagner une partie. Les lignes, les colonnes, les diagonales
    Renvoie un tableau de valeurs qui peut être composé de 0, -1 et le symbole du joueur qui as réussi à gagner"""
    global emplacementWin, numEmplacement
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
            emplacementWin = "ligne" 
            numEmplacement = str(i+1)

    # regarde les victoires en lignes verticales. 
    for i in range(3):
        if joueurPlay1 in [tabFictif[j][i] for j in range(3)] and joueurPlay2 in [tabFictif[j][i] for j in range(3)]:
            winTotale[i + 3] = -1
        elif '□' in [tabFictif[j][i] for j in range(3)]:
            pass
        else:
            winTotale[i + 3] = tab[0][i]
            emplacementWin = "colonne" 
            numEmplacement = str(i+1)

    # regarde les victoires en lignes en diagonales. 
    for i in range(2):
        if joueurPlay1 in [tabFictif[j][(2 - j) * i - j * (i - 1)] for j in range(3)] and joueurPlay2 in [tabFictif[j][(2 - j) * i - j * (i - 1)] for j in range(3)]:
            winTotale[i + 6] = -1
        elif '□' in [tabFictif[j][(2 - j) * i - j * (i - 1)] for j in range(3)]:
            pass
        else:
            winTotale[i + 6] = tab[0][i * 2]
            emplacementWin = "diagonale" 
            numEmplacement = str(i+1)

    return winTotale
        

def whoWin():
    """Cette fonction va vérifier si l'un des deux joueurs a gagner et le renverra"""
    for i in Victoire() :
        if i == joueurPlay1 : 
            return print("Victoire du Joueur 1")
        elif i == joueurPlay2:
            return print("Victoire du Joueur 2")



def grille_turtle():
    """ Créer la grille de morpion de 3x3"""
    length=600
    t.pensize(10)
    t.color("black")
    for i in range(2):
        t.right(90)
        t.forward(length//3)
        t.left(90)
        t.down()
        t.forward(length)
        t.backward(length)
        t.up()

    t.forward(length//3)
    t.right(90)
    t.forward(length//3)
    t.right(180)
        
    t.down()
    t.forward(length)
    t.backward(length)
    t.up()
    t.right(90)
    t.forward(length//3)
    t.left(90)
    t.down()
    t.forward(length)
    t.backward(length)
    t.up()

def letterX(lengthX,x,y):
    t.setpos(x,y)
    t.pensize(10)
    t.color("purple")
    t.down()
    t.right(45)
    t.forward(lengthX/2)
    t.right(180)
    t.forward(lengthX)
    t.right(180)
    t.forward(lengthX/2)
    t.left(90)
    t.forward(lengthX/2)
    t.right(180)
    t.forward(lengthX)
    t.right(180)
    t.forward(lengthX/2)
    t.right(45)
    t.up()

def letterO (x,y):
    t.setpos(x,y)
    t.color("pink")
    t.down()
    t.circle(r)
    t.up()


def position_letter (coup_joueur,letter) :
    if coup_joueur == "1" :
        if letter == "O" :
            letterO(-130,200)
        elif letter == "X" :
            letterX(200,-200,200)
    elif coup_joueur == "2" :
        if letter == "O" :
            letterO(70,200)
        elif letter == "X" :
            letterX(200,0,200)
    elif coup_joueur == "3" :
        if letter == "O" :
            letterO(270,200)
        elif letter == "X" :
            letterX(200,200,200)
    elif coup_joueur == "4" :
        if letter == "O" :
            letterO(-130,0)
        elif letter == "X" :
            letterX(200,-200,0)
    elif coup_joueur == "5" :
        if letter == "O" :
            letterO(70,0)
        elif letter == "X" :
            letterX(200,0,0)
    elif coup_joueur == "6" :
        if letter == "O" :
            letterO(270,0)
        elif letter == "X" :
            letterX(200,200,0)
    elif coup_joueur == "7" :
        if letter == "O" :
            letterO(-130,-200)
        elif letter == "X" :
            letterX(200,-200,-200)
    elif coup_joueur == "8" :
        if letter == "O" :
            letterO(70,-200)
        elif letter == "X" :
            letterX(200,0,-200)
    elif coup_joueur == "9" :
        if letter == "O" :
            letterO(270,-200)
        elif letter == "X" :
            letterX(200,200,-200)

def ligne() :
    t.down()
    t.right(90)
    t.forward(400)
    t.left(90)

def colonne():
    t.down()
    t.right(180)
    t.forward(400)
    t.left(180)
    
def diagonale():
    t.down()
    t.right(135)
    t.forward(565)
    t.left(135)

def victoire_turtle(numEmplacement,emplacementWin):
    t.color("orange")
    if numEmplacement == "1" :
        t.setpos(-200, 200)
        if emplacementWin == "ligne" :
            ligne()
        elif emplacementWin == "colonne" :
            colonne()
        elif emplacementWin == "diagonale" :
            diagonale()
    elif numEmplacement == "2" :
        if emplacementWin == "ligne" :
            t.setpos(-200, 0)
            ligne()
        elif emplacementWin == "colonne" :
            t.setpos(0, 200)
            colonne()
        elif emplacementWin == "diagonale" :
            t.setpos(200, 200)
            t.right(90)
            diagonale()
    elif numEmplacement == "3" :
        if emplacementWin == "ligne" :
            t.setpos(-200, -200)
            ligne()
        elif emplacementWin == "colonne" :
            t.setpos(200, 200)
            colonne()
    t.up()


def IA () :
    """Création d'une IA qui va vérifier tous les cas où l'un des deux joueurs peut gagner et remplir cette case, priorise la vicoire à l'égalité.
    Si il n'y a qu'une seule figure dans une ligne, colonne, diagonale , elle va placer sa figure pour former un couple de 2, priorise les diagonales.
    Rempli automatiquement le centre ou l'un des quatres coins au début """
    cptJ1 = 0 # compteur de figures présentes du joueur
    cptJ2 = 0 # compteur de figures présentes de l'IA
    choixIA = ""

    # regarde dans les lignes si l'un des deux joueur a 2 fois sont symboles
    for i in range(3):     
        cptJ2 = [tabFictif[i][j]for j in range(3)].count(joueurPlay2)
        if cptJ2 == 2:
            for x in range(3):
                if tabFictif[i][x] == '□' :
                    choixIA = tableauPosition[i][x]
                    return str(choixIA)
    for i in range(3): 
        cptJ1 = [tabFictif[i][j]for j in range(3)].count(joueurPlay1)         
        if cptJ1 == 2 :
            for x in range(3):
                if tabFictif[i][x] == '□' :
                    choixIA = tableauPosition[i][x]
                    return str(choixIA)
        
    # regarde dans les colonnes si l'un des deux joueur a 2 fois sont symboles
    for i in range(3):
        cptJ2 = [tabFictif[j][i]for j in range(3)].count(joueurPlay2)
        if cptJ2 == 2:
            for x in range(3):
                if tabFictif[x][i] == '□' :
                    choixIA = tableauPosition[x][i]
                    return str(choixIA)
    for i in range(3):
        cptJ1 = [tabFictif[j][i]for j in range(3)].count(joueurPlay1)
        if cptJ1 == 2: 
            for x in range(3):
                if tabFictif[x][i] == '□' :
                    choixIA = tableauPosition[x][i]
                    return str(choixIA)
     
    # regarde dans les diagonales si l'un des deux joueur a 2 fois sont symboles
    for i in range(2):
        cptJ2 = [tabFictif[j][(2 - j) * i - j * (i - 1)] for j in range(3)].count(joueurPlay2)
        if cptJ2 == 2:
            for x in range(3):
                if tabFictif[x][(2 - x) * i - x * (i - 1)] == '□' : #regarde quel caractère est '□'
                    choixIA = tableauPosition[x][(2 - x) * i - x * (i - 1)] # donne la position du caratère '□' dans le tableau
                    return str(choixIA)
    for i in range(2):
        cptJ1 = [tabFictif[j][(2 - j) * i - j * (i - 1)] for j in range(3)].count(joueurPlay1)
        if cptJ1 == 2 :
            for x in range(3):
                if tabFictif[x][(2 - x) * i - x * (i - 1)] == '□' : #regarde quel caractère est '□'
                    choixIA = tableauPosition[x][(2 - x) * i - x * (i - 1)] # donne la position du caratère '□' dans le tableau
                    return str(choixIA)
                
    if tabFictif[0][0] == joueurPlay1 and tabFictif[2][2] == joueurPlay1 or tabFictif[0][2] == joueurPlay1 and tabFictif[2][0] == joueurPlay1:
        if tabFictif[1][0] == '□':
            choixIA = tableauPosition[1][0]
        elif tabFictif[0][1] == '□':
            choixIA = tableauPosition[0][1]
        elif tabFictif[1][2] == '□':
            choixIA = tableauPosition[1][2]
        elif tabFictif[2][1] == '□':
            choixIA = tableauPosition[2][1]
        return str(choixIA)
    
    # regarde dans les diagonales si l'IA a son symbole présent une seule fois et que le joueur n'est aucun symbole sur la ligne 
    # alors l'IA se mettra à coté de son symbole déjà présent
    for i in range(2):
        cptJ1 = [tabFictif[j][(2 - j) * i - j * (i - 1)] for j in range(3)].count(joueurPlay1)
        cptJ2 = [tabFictif[j][(2 - j) * i - j * (i - 1)] for j in range(3)].count(joueurPlay2)
        if cptJ2 == 1 and cptJ1 == 0:
            for x in range(3):
                if tabFictif[x][(2 - x) * i - x * (i - 1)] == '□' : #regarde quel caractère est '□'
                    choixIA = tableauPosition[x][(2 - x) * i - x * (i - 1)] # donne la position du caratère '□' dans le tableau
                    return str(choixIA)

    # regarde dans les lignes si l'IA a son symbole présent une seule fois et que le joueur n'est aucun symbole sur la ligne 
    # alors l'IA se mettra à coté de son symbole déjà présent
    for i in range(3):     
        cptJ2 = [tabFictif[i][j]for j in range(3)].count(joueurPlay2)
        cptJ1 = [tabFictif[i][j]for j in range(3)].count(joueurPlay1)
        if cptJ2 == 1 and cptJ1 == 0:
            for x in range(3):
                if tabFictif[i][x] == '□' :
                    choixIA = tableauPosition[i][x]
                    return str(choixIA)

    # regarde dans les colonnes si l'IA a son symbole présent une seule fois et que le joueur n'est aucun symbole sur la ligne 
    # alors l'IA se mettra à coté de son symbole déjà présent
    for i in range(3):     
        cptJ2 = [tabFictif[j][i]for j in range(3)].count(joueurPlay2)
        cptJ1 = [tabFictif[j][i]for j in range(3)].count(joueurPlay1)
        if cptJ2 == 1 and cptJ1 == 0:
            for x in range(3):
                if tabFictif[x][i] == '□' :
                    choixIA = tableauPosition[x][i]
                    return str(choixIA)


    # si le centre est libre l'IA se met au centre
    if tabFictif[1][1] == '□' : 
        choixIA = tableauPosition[1][1] 
        return str(choixIA)
    else :
        # sinon elle se met dans l'un des coins
        if tabFictif[0][0] == '□':
            choixIA = tableauPosition[0][0] 
            return str(choixIA)
        elif tabFictif[0][2] == '□':
            choixIA = tableauPosition[0][2] 
            return str(choixIA)
        elif tabFictif[2][0] == '□':
            choixIA = tableauPosition[2][0] 
            return str(choixIA)
        elif tabFictif[2][2] == '□':
            choixIA = tableauPosition[2][2] 
            return str(choixIA)

    choixIA = choice(tableauReussite[:-1])
    while choixIA in alreadyPlay :
        choixIA = choice(tableauReussite[:-1])
        
    return(choixIA)

def game():
    """Création d'une partie de morpion qui peut se joueur à 2 ou seul avec une IA"""
    global firstPlayer, joueurPlay2, numEmplacement, emplacementWin
    grille_turtle()
    robot = input("Voulez vous jouer avec un bot ? [True or False] ")
    coupJouer = ""

    if robot == "False": 
        print("Vous avez choisi le mode multijoueur \n \n")
        joueurPlay2 = input("Joueur 2 choississez la figure que vous voulez jouer : ") #si pas robot alors le joueur 2 choisi la figure qu'il veut
        joueurPlay2 = joueurPlay2.upper()
        print("\n")
        if joueurPlay1 == "O" :
            while joueurPlay2 != "X" :
                joueurPlay2 = input("Joueur 2 rechoississez la figure que vous voulez jouer, 'X' : ")
                joueurPlay2 = joueurPlay2.upper()
        else :
            while joueurPlay2 != "O" :
                joueurPlay2 = input("Joueur 2 rechoississez la figure que vous voulez jouer, 'O' : ")
                joueurPlay2 = joueurPlay2.upper()
                
        print("\n")
    
    else : 
         print("Vous avez choisi le mode contre L'IA \n \n")
    afficher()

    while len(alreadyPlay) < longueurTab:
        if robot == "False":
            time.sleep(0.3)
            if firstPlayer == 1 :
                caseJoueurPlay1 = input("Joueur 1 faite votre choix pour jouer : ") 
                print("\n")
                while caseJoueurPlay1 in alreadyPlay or not caseJoueurPlay1 in tableauReussite :
                    caseJoueurPlay1 = input("Joueur 1 refaite votre choix pour jouer : ")
                    print("\n")
                alreadyPlay.append(caseJoueurPlay1)
                emplacementJoueur(caseJoueurPlay1, joueurPlay1)
                position_letter(caseJoueurPlay1, joueurPlay1) 
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
                position_letter(caseJoueurPlay2, joueurPlay2)  
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
                position_letter(caseJoueurPlay1, joueurPlay1) 
                firstPlayer +=1 #modifie le joueur qui va commencer 
                coupJouer = caseJoueurPlay1

            elif firstPlayer == 2 :  
                choixRobot = IA() 
                alreadyPlay.append(choixRobot)
                emplacementJoueur(choixRobot, joueurPlay2)
                position_letter(choixRobot, joueurPlay2) 
                firstPlayer -= 1 #modifie le joueur qui va commencer 
                coupJouer = choixRobot
        print("La position " + str(coupJouer) + " a été selectionnée \n")
        time.sleep(0.5) 

        if joueurPlay1 in Victoire() or joueurPlay2 in Victoire() : # si un joueur a gagné renvoie le victorieux ou si toutes les cases ont étaient prises renvoie égalité
            if coupJouer == "123456789" :
                for i in range (3) :
                    numEmplacement = str(i+1)
                    emplacementWin = "ligne"
                    victoire_turtle(numEmplacement,emplacementWin)
                    emplacementWin = "colonne"
                    victoire_turtle(numEmplacement,emplacementWin)
                for i in range(2):
                    numEmplacement = str(i+1)
                    emplacementWin = "diagonale"
                    victoire_turtle(numEmplacement,emplacementWin)
            else :
                victoire_turtle(numEmplacement,emplacementWin)

            return whoWin()


    print("Egalité")
    return 
            
game() 
t.done()
