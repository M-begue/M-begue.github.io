from random import randint
from B_Scores_allumettes import ajouter_score_allumettes

def affiche_allu(n:int)->None:
    print(f"Le nombres d'allumettes est de \x1b[38;5;81m{n}\033[0m")

def determiner_gagnant(joueur_actuel : str, fin_jeu : bool, joueur1 : str, joueur2: str) ->str:
    gagnant : str

    if fin_jeu and joueur_actuel == joueur1:
        gagnant = joueur2
    else:
        gagnant = joueur1

    return gagnant


def robot_complexe(nb_allu : int) -> int:
#################################################################################################################################################
#  Fonction qui retourne le nombre d'allumettes que retire le robot avec la difficulté complexe, en fonction du nombre d'allumettes restantes.  #
#                                                                                                                                               #
#  Paramètres d'entrée : nombre d'allumettes restantes.                                                                                         #
#  Paramètres de sortie : nombre d'allumettes retirées.                                                                                         #
#################################################################################################################################################
    prendre : int
    
    if (nb_allu > 1) and (nb_allu < 5):
        prendre = nb_allu - 1
    elif (nb_allu > 5) and (nb_allu < 9):
        prendre = nb_allu - 5
    elif (nb_allu > 9) and (nb_allu < 13):
        prendre = nb_allu - 9
    elif (nb_allu > 13) and (nb_allu < 17):
        prendre = nb_allu - 13
    else:
        prendre = 1

    return prendre


def robot_naif(nb_allu : int, prendre : int) -> int:
#######################
#
#
#
#
#######################
    if (nb_allu == 1) or (prendre == 1):
        prendre = 1
    else:
        prendre = prendre - 1
    return prendre


def robot_hasardeux() -> int:
######################################################################################################################
#  Procédure qui retourne le nombre d'allumettes que retire le robot avec la difficulté complexe, en fonction du nombre d'allumettes restantes.  #
#
#  Paramètres d'entrée : Aucun.
#  Paramètres de sortie : nombre d'allumettes retirées.
#######################################################################################################################################
    prendre = randint(1, 3) # Retourne un entier aléatoire entre 1 et 3
    return prendre


def tour_robot(joueur_actuel : str, diff_robot : int, prendre : int, nb_allu : int) -> int:
#####################################################################################################
#  Fonction qui gère le nombre d'allumettes prises à chaque fois qu'un robot est en train           #
#  de jouer, pour éviter les répétitions.                                                           #
#                                                                                                   #
#  Paramètres d'entrée : nom du joueur, difficulté du robot en train de jouer, nombre d'allumettes  #
#  prises au tour précédent, nombre d'allumettes restantes.                                         #
#  Paramètres de sortie : nombre d'allumettes prises par le robot.                                  #
#####################################################################################################
    if (diff_robot == 1):
        prendre = robot_hasardeux()
    elif (diff_robot == 2):
        prendre = robot_naif(nb_allu, prendre)
    elif (diff_robot == 3):
        prendre = robot_complexe(nb_allu)
        
    if (prendre == 1):
        print(f"Le robot a retiré \x1b[38;5;81m1\033[0m allumette.")
    else:
        print(f"Le robot a retiré \x1b[38;5;81m{prendre}\033[0m allumettes.")
    return prendre


def tour_humain(joueur_actuel : str, nb_allu : int) -> int:
    prendre : int
    prendre = -1
    prendre= int(input(f"{joueur_actuel}, retirez 1, 2 ou 3 allumettes : "))
    while (prendre<1) or (prendre>3) or (prendre>nb_allu):
        print("\x1b[38;5;196mErreur de saisie\033[0m")
        prendre= int(input(f"{joueur_actuel}, retirez 1,2 ou 3 allumettes : "))
    
    return prendre


def allumette(joueur1 : str, joueur2 : str, niveau_bot_1 : int, niveau_bot_2 : int, choixMDJ : int, scores : list[tuple[str, int]])->None:
#
#  Fonction principale qui est responsable de la gestion du jeu des allumettes.
#
#  Paramètres d'entrée : 
#  Paramètres de sortie : 
#
   #glossair
    nb_allu: int
    joueur_actuel: str
    fin_jeu:bool
    prendre:int
    gagnant : str

    prendre = 1
    nb_allu=20
    joueur_actuel = joueur1
    fin_jeu=False #sera vrai uniquement lorsque le jeu sera fini

    print("Bienvenue au jeu des allumettes !")
    print("Règles : Chaque joueur peut retirer 1, 2 ou 3 allumettes par tour.")
    print("Le joueur qui prend la dernière allumette a perdu.")
    
    while not fin_jeu:
        affiche_allu(nb_allu)
        if (choixMDJ == 1): # Mode de jeu HUMAIN VS HUMAIN
            prendre = tour_humain(joueur_actuel, nb_allu)
            nb_allu=nb_allu-prendre
        
        elif(choixMDJ == 2): # Mode de jeu HUMAIN VS ROBOT
            if (joueur_actuel == joueur1):
                prendre = tour_humain(joueur_actuel, nb_allu)
            elif (joueur_actuel == joueur2):
                prendre = tour_robot(joueur_actuel, niveau_bot_2, prendre, nb_allu)
            nb_allu=nb_allu-prendre
        
        elif (choixMDJ == 3): # Mode de jeu ROBOT VS ROBOT
            if (joueur_actuel == joueur1):
                prendre = tour_robot(joueur_actuel, niveau_bot_1, prendre, nb_allu)
                nb_allu = nb_allu -prendre
            elif (joueur_actuel == joueur2):
                nb_allu = nb_allu - prendre
                prendre = tour_robot(joueur_actuel, niveau_bot_2, prendre, nb_allu)

        if nb_allu==0:
            affiche_allu(nb_allu)
            print("\x1b[38;5;196m",joueur_actuel,"a perdu\033[0m")
            fin_jeu=True
            gagnant = determiner_gagnant(joueur_actuel, fin_jeu, joueur1, joueur2)
            if gagnant == "BOT1" or gagnant == "BOT2":
                print()
            else:
                ajouter_score_allumettes(gagnant, scores)

        else:
            if(joueur_actuel==joueur1):
                joueur_actuel=joueur2
            else:
                joueur_actuel= joueur1

