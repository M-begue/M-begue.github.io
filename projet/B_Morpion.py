import random
import time
from B_Scores_Morpion import ajouter_score_morpion

def afficher_aide_ligne()->None:
######################################################################
#
#
#
#
#######################################################################
    compteur : int
    print(f"[1]→   |   |   ")
    for compteur in range (1, 3):
        print("    ---+---+---")
        print(f"[{compteur + 1}]→   |   |   ")


def afficher_aide_colonne()->None:
######################################################################
#
#
#
#
#######################################################################
    compteur : int
    compteur = 1
    print("    [1] [2] [3]")
    print("     ↓   ↓   ↓ ")
    print("       |   |   ")
    for compteur in range (compteur, 3):
        print("    ---+---+---")
        print("       |   |   ")


def determiner_gagnant(joueur_actuel : str, fin_jeu : bool, joueur1 : str, joueur2: str) -> str:
    gagnant : str

    if fin_jeu and joueur_actuel == joueur1:
        gagnant = joueur1
    else:
        gagnant = joueur2

    return gagnant

def bot_facile(grille: list[list[str]]) -> tuple[int, int]:
    cases_vides = [(i, j) for i in range(3) for j in range(3) if grille[i][j] == " "]
    return random.choice(cases_vides)

def bot_intermediaire(grille: list[list[str]], tour: str, adversaire: str) -> tuple[int, int]:
    if tour == "\x1b[38;5;27m0\033[0m":
        adversaire = "\x1b[38;5;196mX\033[0m"
    else:
        adversaire = "\x1b[38;5;27m0\033[0m"
    # Vérifie si le bot peut gagner
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                grille[i][j] = tour
                if victoire(grille, tour):
                    return i, j
                grille[i][j] = " "
        # Vérifie si l'adversaire peut gagner
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                grille[i][j] = adversaire
                if victoire(grille, adversaire):
                    grille[i][j] = " "
                    return i, j
                grille[i][j] = " "

    # Sinon joue au hasard
    return bot_facile(grille)

def bot_difficile(grille: list[list[str]], tour: str, adversaire: str) -> tuple[int, int]:
    coins : list[tuple[int, int]]
    if tour == "\x1b[38;5;27m0\033[0m":
        adversaire = "\x1b[38;5;196mX\033[0m"
    else:
        adversaire = "\x1b[38;5;27m0\033[0m"
    # Vérifie si le bot peut gagner
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                grille[i][j] = tour
                if victoire(grille, tour):
                    return i, j
                grille[i][j] = " "

    # Bloque l'adversaire s'il peut gagner
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                grille[i][j] = adversaire
                if victoire(grille, adversaire):
                    grille[i][j] = " "
                    return i, j
                grille[i][j] = " "

    # Prendre les coins si disponibles
    coins = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for i, j in coins:
        if grille[i][j] == " ":
            return i, j

    # Prendre le centre si disponible
    if grille[1][1] == " ":
        return 1, 1

    # Sinon joue au hasard
    return bot_facile(grille)


def affiche_Grille (grille:list[list[str]])-> None:
###############################################################################################################################
#  Procédure permettant l'affichage de la grille                                                                              #
#                                                                                                                             #
#  Paramètres d'entrée : Modèle de la grille ainsi que les valeurs des cases si elles sont remplies par une croix ou un rond  #
#  Paramètres de sortie : Aucun                                                                                               #
###############################################################################################################################
    i:int
    
    for i in range (3):
        print (f" {grille [i][0]} | {grille [i][1]} | {grille[i][2]} ")
        if i<2:
            print("---+---+---")


def victoire(grille:list[list[str]], tour:str)-> bool:
######################################################################################################
#  Fonction permettant d'analyser si un des deux joueurs a gagné                                     #
#                                                                                                    #
#  Paramètres d'entrée : grille contenant les valeurs de chaque case, symbole du tour actuel         #
#  Paramètres de sortie : Retourne un booléen qui indique si le joueur a gagné à la fin de son tour  #
######################################################################################################
    i : int

    # Victoire sur une ligne
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] == tour:
            return True

    # Victoire sur une colonne
    for i in range(3):
        if grille[0][i] == grille[1][i] == grille[2][i] == tour:
            return True

    # Victoire sur une diagonale
    if (grille[0][0] == grille[1][1] == grille[2][2] == tour):
        return True
    if (grille[0][2] == grille[1][1] == grille[2][0] == tour):
        return True
    
    return False


#Fonction pour vérifier si il y a un match nul
def match_nul(grille:list[list[str]])-> bool:
    i:int
    j:int

    for i in range(3):
        for j in range(3):
            if (grille[i][j] == " "):
                return False
    return True


#procédure pour le jeu
def morpion(joueur1 : str, joueur2 : str, niveau_bot1 : int, niveau_bot2 : int, scores : list[tuple[str, int]])->None:
    grille:list[list[str]]
    fin_jeu: bool
    tour: str
    ligne:int
    colonne:int
    joueur_actuel: str
    gagnant : str

    grille=[[" " for _ in range (3)] for _ in range(3)]
    joueur_actuel = random.choice([joueur1, joueur2])
    if joueur_actuel == joueur1:
        tour ="\x1b[38;5;196mX\033[0m"
    else:
        tour = "\x1b[38;5;27m0\033[0m"
    fin_jeu=False
    ligne = -1
    colonne = -1

    
    print("Bienvenue au jeu du morpion !")
    print("Règles : Chaque joueur place un symbole à tour de rôle")
    print("Celui qui réussi a remplir une ligne/colonne/diagonale a gagner.")
    print()
    print(f"Le joueur {joueur_actuel} commence !")
    print()

    while not fin_jeu:
        affiche_Grille(grille)
        print()
        # Tour des bots ou des joueurs
        if (joueur_actuel == "BOT1" and niveau_bot1) or (joueur_actuel == "BOT2" and niveau_bot2):
            print(f"{joueur_actuel} réfléchit...")
            time.sleep(1.5)
            if joueur_actuel == "BOT1" and niveau_bot1 == 1:
                ligne, colonne = bot_facile(grille)
            elif joueur_actuel == "BOT1" and niveau_bot1 == 2:
                ligne, colonne = bot_intermediaire(grille, tour, "\x1b[38;5;27m0\033[0m")
            elif joueur_actuel == "BOT1" and niveau_bot1 == 3:
                ligne, colonne = bot_difficile(grille, tour, "\x1b[38;5;27m0\033[0m")
            elif joueur_actuel == "BOT2" and niveau_bot2 == 1:
                ligne, colonne = bot_facile(grille)
            elif joueur_actuel == "BOT2" and niveau_bot2 == 2:
                ligne, colonne = bot_intermediaire(grille, tour, "\x1b[38;5;27m0\033[0m")
            elif joueur_actuel == "BOT2" and niveau_bot2 == 3:
                ligne, colonne = bot_difficile(grille, tour, "\x1b[38;5;196mX\033[0m")
        else:
            print(joueur_actuel,tour,"tapez la ligne et la colonne")
            afficher_aide_ligne()
            ligne= int(input("Ligne : "))-1
            while (ligne<0) or (ligne>2):
                print("\x1b[38;5;196mChoisissez un nombre entre 1 et 3\033[0m")
                ligne= int(input("Ligne : "))-1
            
            afficher_aide_colonne()
            colonne= int(input("Colonne : "))-1
            while (colonne<0) or (colonne>2):
                print("\x1b[38;5;196mChoisissez un nombre entre 1 et 3\033[0m")

                colonne= int(input("Colonne : "))-1

            while grille [ligne][colonne]!=" ":
                print("\x1b[38;5;196mEmplacement indisponible !\033[0m")
                ligne= int(input("Ligne : "))-1

                while (ligne<0) or (ligne>2):
                    print("\x1b[38;5;196mChoisissez un nombre entre 1 et 3\033[0m")
                    afficher_aide_ligne()
                    ligne= int(input("Ligne : "))-1
                
                colonne= int(input("Colonne : "))-1
                while (colonne<0) or (colonne>2):
                    print("\x1b[38;5;196mChoisissez un nombre entre 1 et 3\033[0m")
                    afficher_aide_colonne()
                    colonne= int(input("Colonne : "))-1

        grille[ligne][colonne]=tour

        #vérifier la victoire
        if victoire(grille,tour):
            affiche_Grille(grille)
            print(f"\x1b[38;5;46m{joueur_actuel} a gagné\033[0m")
            fin_jeu = True
            gagnant = determiner_gagnant(joueur_actuel, fin_jeu, joueur1, joueur2)
            if gagnant == "BOT1" or gagnant == "BOT2":
                print()
            else:
                ajouter_score_morpion(gagnant, scores)

        elif match_nul(grille):
            affiche_Grille(grille)
            print("\x1b[38;5;81mMatch nul ! La grille est pleine.\033[0m")
            fin_jeu = True

        else:
            if (joueur_actuel == joueur1):
                joueur_actuel = joueur2
                tour = "\x1b[38;5;27m0\033[0m"
            else:
                joueur_actuel = joueur1
                tour = "\x1b[38;5;196mX\033[0m"