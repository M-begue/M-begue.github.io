from B_Allumettes import *
from B_Morpion import *
from B_Jeu_Des_Devinettes import *
from B_Scores_allumettes import *
from B_Scores_jeuDesDevinettes import *
from B_Scores_Morpion import *

def affiche_Menu()-> None:
    print()
    print("Menu")
    print()
    print("   1. Devinette.")
    print("   2. Allumette.")
    print("   3. Morpion.")
    print("   4. Score.")
    print("   5. Quitter.")
    print()

def affiche_Menu_scores()-> None:
    print()
    print("Menu des scores")
    print()
    print("\t1. Devinette.")
    print("\t2. Allumette.")
    print("\t3. Morpion.")
    print()

def affiche_Menu_ModeDeJeux() -> int:
    choix_ModeDeJeux : int
    choix_ModeDeJeux = 0
    print()
    print("Modes de jeux")
    print()
    print("\t1. Humain VS Humain.")
    print("\t2. Humain VS Robot.")
    print("\t3. Robot VS Robot.")
    print()
    while (choix_ModeDeJeux < 1) or (choix_ModeDeJeux > 3):
        choix_ModeDeJeux = int(input("Quel est le mode de jeu auquel vous souhaitez jouer ? "))
    print()
    return choix_ModeDeJeux


def affiche_bot_difficulte(robot : str) -> int:
    choix_diff : int
    choix_diff = 0
    print(f"Choix de la difficulté du robot {robot} :")
    print("\t1. Hazardeux")
    print("\t2. Naïf")
    print("\t3. Complexe")
    print()
    while (choix_diff < 1) or (choix_diff > 3):
        choix_diff = int(input("Saisissez le chiffre correspondant à votre choix : "))
    print()
    return choix_diff


def choixMenu (choix:int) -> None:
    choix_score : int
    choixMDJ : int
    niveau_bot_1 : int
    niveau_bot_2 : int
    joueur1 : str
    joueur2 : str
    
    joueur1 = ""
    joueur2 = ""
    choix_score = 0


    if choix==1: #Devinettes
        choixMDJ = affiche_Menu_ModeDeJeux()
        if choixMDJ == 1:
            while (joueur1 == ""):
                joueur1 = input("Entrez le nom du joueur 1 : ")
                if (joueur1 == ""):
                    print("Vous devez saisir un nom !")
            while (joueur2 == "") or (joueur2 == joueur1):
                joueur2 = input("Entrez le nom du joueur 2 : ")
                if (joueur2 == ""):
                    print("Vous devez saisir un nom !")
                elif (joueur2 == joueur1):
                    print("Le nom du joueur 2 ne peut pas être le même que celui du joueur 1 !") 
            niveau_bot_2 = 0
            jeu_des_devinettes(joueur1, joueur2, niveau_bot_2, scores_devinettes)

        elif choixMDJ == 2:
            while (joueur1 == ""):
                joueur1 = input("Entrez le nom du joueur 1 : ")
                if (joueur1 == ""):
                    print("Vous devez saisir un nom !")
            joueur2 = "BOT2"
            niveau_bot_2 = affiche_bot_difficulte(joueur2)
            jeu_des_devinettes(joueur1, joueur2, niveau_bot_2, scores_devinettes)

        elif choixMDJ == 3:
            joueur1 = "BOT1"
            joueur2 = "BOT2"
            niveau_bot_1 = affiche_bot_difficulte(joueur1)
            niveau_bot_2 = affiche_bot_difficulte(joueur2)
            jeu_robot_vs_robot(niveau_bot_1, niveau_bot_2)

    elif choix==2: #Allumette
        choixMDJ = affiche_Menu_ModeDeJeux()
        if choixMDJ == 1:
            while (joueur1 == ""):
                joueur1 = input("Entrez le nom du joueur 1 : ")
                if (joueur1 == ""):
                    print("Vous devez saisir un nom !")
            while (joueur2 == "") or (joueur2 == joueur1):
                joueur2 = input("Entrez le nom du joueur 2 : ")
                if (joueur2 == ""):
                    print("Vous devez saisir un nom !")
                elif (joueur2 == joueur1):
                    print("Le nom du joueur 2 ne peut pas être le même que celui du joueur 1 !")
            niveau_bot_1 = 1
            niveau_bot_2 = affiche_bot_difficulte(joueur2)
            allumette(joueur1, joueur2, niveau_bot_1, niveau_bot_2, choixMDJ, scores_allumettes)
            
        elif choixMDJ == 2:
            while (joueur1 == ""):
                joueur1 = input("Entrez le nom du joueur 1 : ")
                if (joueur1 == ""):
                    print("Vous devez saisir un nom !")
            joueur2 = "BOT2"
            niveau_bot_1 = 1
            niveau_bot_2 = affiche_bot_difficulte(joueur2)
            allumette(joueur1, joueur2, niveau_bot_1, niveau_bot_2, choixMDJ, scores_allumettes)

        elif choixMDJ == 3:
            joueur1 = "BOT1"
            joueur2 = "BOT2"
            niveau_bot_1 = affiche_bot_difficulte(joueur1)
            niveau_bot_2 = affiche_bot_difficulte(joueur2)
            allumette(joueur1, joueur2, niveau_bot_1, niveau_bot_2, choixMDJ, scores_allumettes)

    elif choix==3: #Morpion
        choixMDJ = affiche_Menu_ModeDeJeux()
        if choixMDJ == 1:
            while (joueur1 == ""):
                joueur1 = input("Entrez le nom du joueur 1 : ")
                if (joueur1 == ""):
                    print("Vous devez saisir un nom !")
            while (joueur2 == "") or (joueur2 == joueur1):
                joueur2 = input("Entrez le nom du joueur 2 : ")
                if (joueur2 == ""):
                    print("Vous devez saisir un nom !")
                elif (joueur2 == joueur1):
                    print("Le nom du joueur 2 ne peut pas être le même que celui du joueur 1 !")
            niveau_bot_1 = 1
            niveau_bot_2 = 1
            morpion(joueur1, joueur2, niveau_bot_1, niveau_bot_2, scores_morpion)
            
        elif choixMDJ == 2:
            while (joueur1 == ""):
                joueur1 = input("Entrez le nom du joueur 1 : ")
                if (joueur1 == ""):
                    print("Vous devez saisir un nom !")
            joueur2 = "BOT2"
            niveau_bot_1 = 1
            niveau_bot_2 = affiche_bot_difficulte(joueur2)
            morpion(joueur1, joueur2, niveau_bot_1, niveau_bot_2, scores_morpion)

        elif choixMDJ == 3:
            joueur1 = "BOT1"
            joueur2 = "BOT2"
            niveau_bot_1 = affiche_bot_difficulte(joueur1)
            niveau_bot_2 = affiche_bot_difficulte(joueur2)
            morpion(joueur1, joueur2, niveau_bot_1, niveau_bot_2, scores_morpion)
    
    elif choix==4: #Scores

        affiche_Menu_scores()
        while choix_score == 0:
            choix_score = int(input("Quel jeu voulez-vous regarder le score ? "))
            choixMenu_Score(choix_score)

    elif choix==5:
        sauvegarder_scores_allumettes(scores_allumettes)
        sauvegarder_scores_devinettes(scores_devinettes)
        sauvegarder_scores_morpion(scores_morpion)
        print("Au revoir.")

    else:
        print("Erreur de saisie.")

def choixMenu_Score (choix_score : int) ->None:
    if  choix_score== 1:

        afficher_scores_devinettes()

    elif choix_score== 2:

        afficher_scores_allumettes()


    elif choix_score== 3:

        afficher_scores_morpion()

    else:
        print("Erreur de saisie")



if __name__ == "__main__":
    choix: int
    scores_allumettes : list[tuple[str, int]]
    scores_devinettes : list[tuple[str, int]]
    scores_morpion : list[tuple[str, int]]

    choix = 0

    scores_allumettes = charger_scores_allumettes()
    scores_devinettes = charger_scores_devinettes()
    scores_morpion = charger_scores_morpion()

    while (choix !=5):
        affiche_Menu()
        choix= int(input("Quel est votre choix ? "))
        choixMenu(choix)
