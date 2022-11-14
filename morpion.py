from random import *
from os import *
from time import *


system("cls")

class morpion :

    def __init__(self): 
        self.tab = [['□' for i in range(3)]for j in range(3)] 
        self.joueurPlay2 = random.choices("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
        self.alreadyPlay = []
        self.firstPlayer = random.choices(0,1)

    def printTab(self):
        """ Affiche le plateau du morpion comme le vrai jeu"""
        for i in self.tab:
            print(i)
        print('')

    def emplacementJoueur (self, choix, coup_Joueur):
        print(choix)
        if choix == "1" :
            self.tab[0][0] = coup_Joueur
        elif choix == "2" :
            self.tab[0][1] = coup_Joueur
        elif choix == "3" :
            self.tab[0][2] = coup_Joueur
        elif choix == "4" :
            self.tab[1][0] = coup_Joueur
        elif choix == "5" :
            self.tab[1][1] = coup_Joueur
        elif choix == "6" :
            self.tab[1][2] = coup_Joueur
        elif choix == "7" :
            self.tab[2][0] = coup_Joueur
        elif choix == "8" :
            self.tab[2][1] = coup_Joueur
        elif choix == "9" :
            self.tab[2][2] = coup_Joueur
        return self.printTab()
        

    def game():
        robot = input("Voulez vous jouer avec un bot ? [True or False] ")
        choixRobot = ""
        if robot :
            while not choixRobot in self.alreadyPlay:
                choixRobot = str(randint(1, 9))
            self.alreadyPlay.append(choixRobot)
            morpion().emplacementJoueur(choixRobot, self.joueurPlay2)  
        else :
            if self.firstPlayer == 0 :
                while not joueurPlay1 in self.alreadyPlay:
                    joueurPlay1 = input("Joueur 1 Choississez votre choix pour jouer : ")
            joueurPlay2 = input("Joueur 2 Choississez votre choix pour jouer : ")


        



morpion().emplacementJoueur("X")          
