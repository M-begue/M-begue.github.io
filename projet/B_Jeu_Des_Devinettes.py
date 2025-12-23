from math import log2
from getpass import getpass
import random
import time
from B_Scores_jeuDesDevinettes import ajouter_score_devinettes


def determiner_gagnant(joueur_actuel : str, gagne : bool, joueur1 : str, joueur2: str) -> str:
#################################################################################################################################
#  Fonction permettant de déterminer lequel des deux joueur a gagné                                                             #
#                                                                                                                               #
#  Paramètres d'entrée : nom du joueur en train de jouer son tour, statut de la partie (en cours/finie), noms des deux joueurs  #
#  Paramètres de sortie : Le numéro du joueur ayant gagné                                                                       #
#################################################################################################################################
    gagnant : str

    if gagne and joueur_actuel == joueur1:
        gagnant = joueur1
    else:
        gagnant = joueur2

    return gagnant

def diff_bot() -> int:
    niveau_bot : int

    niveau_bot = -1
    print("Affrontez le bot en choisissant son niveau de difficulté :")
    print("   1 - Bot facile (joue au hasard)")
    print("   2 - Bot intermédiaire (stratégie simple)")
    print("   3 - Bot difficile (stratégie optimale)")

    while niveau_bot < 0 or niveau_bot > 3:
        niveau_bot = int(input("Entrez le numéro du niveau : "))

    return niveau_bot

def choisir_devineur(joueur1 : str, joueur2 : str) -> tuple[str, str]:
    reponse_Qui : int
    devineur : str
    decideur : str

    reponse_Qui = -1
    
    print(f"1. {joueur1}")
    print(f"2. {joueur2}")
    print()
    while reponse_Qui < 1 or reponse_Qui > 2:
        reponse_Qui = int(input("Qui devine ? "))
    if reponse_Qui == 1:
        devineur = joueur1
        decideur = joueur2
    else :
        devineur = joueur2
        decideur = joueur1
    return devineur, decideur

def jeu_des_devinettes(joueur1 : str, joueur2 : str, niveau_bot_2: int, scores : list[tuple[str, int]])-> None:
############################################################################################
#  Fonction principale qui s'occupe de faire jouer les deux joueurs au jeu des devinettes  #
#                                                                                          #
#  Paramètres d'entrée : Aucun                                                             #
#  Paramètres de sortie : Aucun                                                            #
############################################################################################
    limite_haute : int
    limite_basse : int
    essai : int
    gagne : bool
    reponse : int
    essai_max : int
    nombre_secret : int
    moyenne : int
    ecart : int
    joueur_actuel : str
    gagnant : str

    limite_haute = 0
    limite_basse = 1
    gagne = False
    nombre_secret = -1
    joueur_actuel = ""

    devineur, decideur = choisir_devineur(joueur1, joueur2)

    if niveau_bot_2 == 0:
        while (limite_haute <= 0):
            limite_haute = int(input(f"{devineur}, choisis une limite positive : "))
        essai_max = int(log2(limite_haute))
        while nombre_secret < limite_basse or nombre_secret > limite_haute:
            nombre_secret = int(getpass(f"{decideur}, entrez le nombre auquel vous pensez entre \x1b[38;5;81m{limite_basse}\033[0m et \x1b[38;5;81m{limite_haute} \033[0m : "))
        print()
        print(f"{devineur} vous avez {essai_max} essais pour deviner le nombre")
        print()
        
        while not gagne:
            if (essai_max == 0):
                print(f"{devineur}, vous n'avez plus d'éssais")
                print()
                print(f"\x1b[38;5;46mBien joué {decideur}  \033[0m")
                gagne=True
                joueur_actuel = decideur
                gagnant = determiner_gagnant(joueur_actuel, gagne, joueur1, joueur2)
                ajouter_score_devinettes(gagnant, scores)
                
            while (essai_max > 0):
                essai = -1
                while (essai > limite_haute) or (essai < limite_basse):
                    print(f"{devineur}, il vous reste {essai_max} essais pour deviner le nombre")
                    essai = int(input(f"Entrez un nombre entre \x1b[38;5;81m{limite_basse}\033[0m et \x1b[38;5;81m{limite_haute} \033[0m : "))
                    print()

                print(decideur,"aidez votre camarade à l'aide des proposition ci-dessous : ")
                print("   \x1b[38;5;250m1. C'est plus \033[0m")
                print("   \x1b[38;5;250m2. C'est moins \033[0m")
                print("   \x1b[38;5;250m3. C'est la bonne réponse \033[0m")
                print()
                reponse = int(input("Quel est votre choix ? "))
                
                while (reponse > 3) or (reponse < 1):
                    print("\x1b[38;5;196mErreur de saisie \033[0m")
                    reponse = int(input("Quel est votre choix ? "))


                if reponse==3:
                    gagne=True
                    print(f"\x1b[38;5;46mBien joué {devineur} \033[0m")
                    essai_max = 0
                    joueur_actuel = devineur
                    gagnant = determiner_gagnant(joueur_actuel, gagne, joueur1, joueur2)
                    ajouter_score_devinettes(gagnant, scores)

                elif reponse==2:
                    print("\x1b[38;5;201mC'est moins ! \033[0m")
                    limite_haute = essai
                    essai_max = essai_max - 1

                elif reponse==1:
                    print("\x1b[38;5;202mC'est plus ! \033[0m")
                    limite_basse = essai
                    essai_max = essai_max - 1

    elif niveau_bot_2 == 1:
        #Bot hasard
        if devineur == "BOT2":
            while (limite_haute <= 0):
                limite_haute = int(input(f"{decideur}, choisis une limite positive : "))
            essai_max = int(log2(limite_haute))
            while nombre_secret < limite_basse or nombre_secret > limite_haute:
                nombre_secret = int(getpass(f"{decideur}, entrez le nombre auquel vous pensez entre \x1b[38;5;81m{limite_basse}\033[0m et \x1b[38;5;81m{limite_haute} \033[0m : "))
            while not gagne:
                if (essai_max == 0):
                    print(f"{devineur} n'a plus d'éssais")
                    print()
                    print(f"\x1b[38;5;46mBien joué {decideur} \033[0m")
                    gagne=True
                    joueur_actuel = decideur
                    gagnant = determiner_gagnant(joueur_actuel, gagne, joueur1, joueur2)
                    ajouter_score_devinettes(gagnant, scores)
                    
                while (essai_max > 0):
                    essai = -1
                    print(f"Il reste {essai_max} essais au bot pour deviner le nombre")
                    essai = random.randint(limite_basse, limite_haute)
                    print(f"Le bot propose : \x1b[38;5;81m{essai}\033[0m")
                    print()

                    print(decideur,"Choissisez parmi les propositions suivantes : ")
                    print("   \x1b[38;5;250m1. C'est plus \033[0m")
                    print("   \x1b[38;5;250m2. C'est moins \033[0m")
                    print("   \x1b[38;5;250m3. C'est la bonne réponse \033[0m")
                    print()
                    reponse = int(input("Quel est votre choix ? "))
                    
                    while (reponse > 3) or (reponse < 1):
                        print("\x1b[38;5;196mErreur de saisie \033[0m")
                        reponse = int(input("Quel est votre choix ? "))

                    if reponse==3:
                        gagne=True
                        print("\x1b[38;5;46mLe BOT à gagné \033[0m")
                        essai_max = 0

                    elif reponse==2:
                        print("\x1b[38;5;201mC'est moins ! \033[0m")
                        limite_haute = essai
                        essai_max = essai_max - 1

                    elif reponse==1:
                        print("\x1b[38;5;202mC'est plus ! \033[0m")
                        limite_basse = essai
                        essai_max = essai_max - 1
        else:
            limite_haute = 100
            essai_max = int(log2(limite_haute))
            print("Le bot réfléchi à un nombre...")
            nombre_secret = random.randint(1, limite_haute)
            print(f"{devineur} vous avez {essai_max} essais pour deviner le nombre")
            print()
            while not gagne:
                if (essai_max == 0):
                    print(f"{devineur}, vous n'avez plus d'éssais")
                    print()
                    print(f"\x1b[38;5;46mLe Bot a gagné\033[0m")
                    print(f"Le nombre à deviné était \x1b[38;5;81m{nombre_secret}\033[0m")
                    gagne=True
                while (essai_max > 0):
                    essai = -1
                    while (essai > limite_haute) or (essai < limite_basse):
                        print(f"{devineur}, il vous reste {essai_max} essais pour deviner le nombre")
                        essai = int(input(f"Entrez un nombre entre \x1b[38;5;81m{limite_basse}\033[0m et \x1b[38;5;81m{limite_haute} \033[0m : "))
                        print()
                        if essai == nombre_secret:
                            gagne=True
                            print(f"\x1b[38;5;46mBien joué {devineur} \033[0m")
                            essai_max = 0
                            joueur_actuel = devineur
                            gagnant = determiner_gagnant(joueur_actuel, gagne, joueur1, joueur2)
                            ajouter_score_devinettes(gagnant, scores)
                        else:
                            print(f"Ce n'est pas \x1b[38;5;81m{essai}\033[0m, rééssayer")
                            essai_max = essai_max -1
                            if essai > nombre_secret:
                                limite_haute = essai
                            if essai < nombre_secret:
                                limite_basse = essai
    elif niveau_bot_2 == 2:
        #Bot intermédiare (nombre proche de la moyenne)
        if devineur == "BOT2":
            while (limite_haute <= 0):
                limite_haute = int(input(f"{decideur}, choisis une limite positive : "))
            essai_max = int(log2(limite_haute))
            while nombre_secret < limite_basse or nombre_secret > limite_haute:
                nombre_secret = int(getpass(f"{decideur}, entrez le nombre auquel vous pensez entre \x1b[38;5;81m{limite_basse}\033[0m et \x1b[38;5;81m{limite_haute} \033[0m : "))
            while not gagne:
                if (essai_max == 0):
                    print(f"{devineur} n'a plus d'éssais")
                    print()
                    print(f"\x1b[38;5;46mBien joué {decideur} \033[0m")
                    gagne=True
                    joueur_actuel = decideur
                    gagnant = determiner_gagnant(joueur_actuel, gagne, joueur1, joueur2)
                    ajouter_score_devinettes(gagnant, scores)
                    
                while (essai_max > 0):
                    essai = -1
                    print(f"Il reste {essai_max} essais au bot pour deviner le nombre")
                    moyenne = (limite_basse + limite_haute) // 2
                    ecart = random.randint(-10, 10)
                    essai = moyenne + ecart
                    print(f"Le bot propose : \x1b[38;5;81m{essai}\033[0m")
                    print()

                    print(decideur,"Choissisez parmi les propositions suivantes : ")
                    print("   \x1b[38;5;250m1. C'est plus \033[0m")
                    print("   \x1b[38;5;250m2. C'est moins \033[0m")
                    print("   \x1b[38;5;250m3. C'est la bonne réponse \033[0m")
                    print()
                    reponse = int(input("Quel est votre choix ? "))
                    
                    while (reponse > 3) or (reponse < 1):
                        print("\x1b[38;5;196mErreur de saisie \033[0m")
                        reponse = int(input("Quel est votre choix ? "))

                    if reponse==3:
                        gagne=True
                        print("\x1b[38;5;46mLe BOT à gagné \033[0m")
                        essai_max = 0

                    elif reponse==2:
                        print("\x1b[38;5;201mC'est moins ! \033[0m")
                        limite_haute = essai
                        essai_max = essai_max - 1

                    elif reponse==1:
                        print("\x1b[38;5;202mC'est plus ! \033[0m")
                        limite_basse = essai
                        essai_max = essai_max - 1
        else:
            limite_haute = 10000
            essai_max = int(log2(limite_haute))
            print("Le bot réfléchi à un nombre...")
            nombre_secret = random.randint(1, limite_haute)
            print(f"{devineur} vous avez {essai_max} essais pour deviner le nombre")
            print()
            while not gagne:
                if (essai_max == 0):
                    print(f"{devineur}, vous n'avez plus d'éssais")
                    print()
                    print(f"\x1b[38;5;46mLe Bot a gagné\033[0m")
                    print(f"Le nombre à deviné était \x1b[38;5;81m{nombre_secret}\033[0m")
                    gagne=True
                while (essai_max > 0):
                    essai = -1
                    while (essai > limite_haute) or (essai < limite_basse):
                        print(f"{devineur}, il vous reste {essai_max} essais pour deviner le nombre")
                        essai = int(input(f"Entrez un nombre entre \x1b[38;5;81m{limite_basse}\033[0m et \x1b[38;5;81m{limite_haute} \033[0m : "))
                        print()
                        if essai == nombre_secret:
                            gagne=True
                            print(f"\x1b[38;5;46mBien joué {devineur} \033[0m")
                            essai_max = 0
                            joueur_actuel = devineur
                            gagnant = determiner_gagnant(joueur_actuel, gagne, joueur1, joueur2)
                            ajouter_score_devinettes(gagnant, scores)
                        else:
                            print(f"Ce n'est pas \x1b[38;5;81m{essai}\033[0m, rééssayer")
                            essai_max = essai_max -1
                            if essai > nombre_secret:
                                limite_haute = essai
                            if essai < nombre_secret:
                                limite_basse = essai
    elif niveau_bot_2 == 3:
        #Bot difficile (nombre optimisé)
        if devineur == "BOT2":
            while (limite_haute <= 0):
                limite_haute = int(input(f"{decideur}, choisis une limite positive : "))
            essai_max = int(log2(limite_haute))
            while nombre_secret < limite_basse or nombre_secret > limite_haute:
                nombre_secret = int(getpass(f"{decideur}, entrez le nombre auquel vous pensez entre \x1b[38;5;81m{limite_basse}\033[0m et \x1b[38;5;81m{limite_haute} \033[0m : "))
            while not gagne:
                if (essai_max == 0):
                    print(f"{devineur} n'a plus d'éssais")
                    print()
                    print(f"\x1b[38;5;46mBien joué {decideur} \033[0m")
                    gagne=True
                    joueur_actuel = decideur
                    gagnant = determiner_gagnant(joueur_actuel, gagne, joueur1, joueur2)
                    ajouter_score_devinettes(gagnant, scores)
                    
                while (essai_max > 0):
                    essai = -1
                    print(f"Il reste {essai_max} essais au bot pour deviner le nombre")
                    essai = (limite_basse + limite_haute) // 2
                    print(f"Le bot propose : \x1b[38;5;81m{essai}\033[0m")
                    print()

                    print(decideur,"Choissisez parmi les propositions suivantes : ")
                    print("   \x1b[38;5;250m1. C'est plus \033[0m")
                    print("   \x1b[38;5;250m2. C'est moins \033[0m")
                    print("   \x1b[38;5;250m3. C'est la bonne réponse \033[0m")
                    print()
                    reponse = int(input("Quel est votre choix ? "))
                    
                    while (reponse > 3) or (reponse < 1):
                        print("\x1b[38;5;196mErreur de saisie \033[0m")
                        reponse = int(input("Quel est votre choix ? "))

                    if reponse==3:
                        gagne=True
                        print("\x1b[38;5;46mLe BOT à gagné \033[0m")
                        essai_max = 0

                    elif reponse==2:
                        print("\x1b[38;5;201mC'est moins ! \033[0m")
                        limite_haute = essai
                        essai_max = essai_max - 1

                    elif reponse==1:
                        print("\x1b[38;5;202mC'est plus ! \033[0m")
                        limite_basse = essai
                        essai_max = essai_max - 1
        else:
            limite_haute = 1000000
            essai_max = int(log2(limite_haute))
            print("Le bot réfléchi à un nombre...")
            nombre_secret = random.randint(1, limite_haute)
            print(f"{devineur} vous avez {essai_max} essais pour deviner le nombre")
            print()
            while not gagne:
                if (essai_max == 0):
                    print(f"{devineur}, vous n'avez plus d'éssais")
                    print()
                    print(f"\x1b[38;5;46mLe Bot a gagné\033[0m")
                    print(f"Le nombre à deviné était \x1b[38;5;81m{nombre_secret}\033[0m")
                    gagne=True
                while (essai_max > 0):
                    essai = -1
                    while (essai > limite_haute) or (essai < limite_basse):
                        print(f"{devineur}, il vous reste {essai_max} essais pour deviner le nombre")
                        essai = int(input(f"Entrez un nombre entre \x1b[38;5;81m{limite_basse}\033[0m et \x1b[38;5;81m{limite_haute} \033[0m : "))
                        print()
                        if essai == nombre_secret:
                            gagne=True
                            print(f"\x1b[38;5;46mBien joué {devineur} \033[0m")
                            essai_max = 0
                            joueur_actuel = devineur
                            gagnant = determiner_gagnant(joueur_actuel, gagne, joueur1, joueur2)
                            ajouter_score_devinettes(gagnant, scores)
                        else:
                            print(f"Ce n'est pas \x1b[38;5;81m{essai}\033[0m, rééssayer")
                            essai_max = essai_max -1
                            if essai > nombre_secret:
                                limite_haute = essai
                            if essai < nombre_secret:
                                limite_basse = essai

def jeu_robot_vs_robot(niveau_bot1: int, niveau_bot2: int) -> None:
    """
    Cas où deux bots s'affrontent, les bots choisissent des nombres et les stratégies sont déterminées par les niveaux.
    """
    devineur : str
    decideur : str
    limite_haute_bot1 : int
    limite_haute_bot2 : int
    nombre_secret : int
    nombre_secret : int

    limite_haute_bot1 = 0
    limite_haute_bot2 = 0
    joueur1 = "BOT1"
    joueur2 = "BOT2"
    limite_basse = 1
    essai_max = 1
    nombre_secret = 1

    # Choisir quel bot devine
    devineur, decideur = choisir_devineur(joueur1, joueur2)
    
    # Choisir la limite pour chaque bot
    if niveau_bot1 == 1 and decideur == joueur1:
        limite_haute_bot1 = 100
        nombre_secret = random.randint(limite_basse, limite_haute_bot1)
        essai_max = int(log2(limite_haute_bot1))
    elif niveau_bot1 == 2 and decideur == joueur1:
        limite_haute_bot1 = 10000
        nombre_secret = random.randint(limite_basse, limite_haute_bot1)
        essai_max = int(log2(limite_haute_bot1))
    elif niveau_bot1 == 3 and decideur == joueur1:
        limite_haute_bot1 = 1000000
        nombre_secret = random.randint(limite_basse, limite_haute_bot1)
        essai_max = int(log2(limite_haute_bot1))

    if niveau_bot2 == 1 and decideur == joueur2:
        limite_haute_bot2 = 100
        nombre_secret = random.randint(limite_basse, limite_haute_bot2)
        essai_max = int(log2(limite_haute_bot2))
    elif niveau_bot2 == 2 and decideur == joueur2:
        limite_haute_bot2 = 10000
        nombre_secret = random.randint(limite_basse, limite_haute_bot2)
        essai_max = int(log2(limite_haute_bot2))
    elif niveau_bot2 == 3 and decideur == joueur2:
        limite_haute_bot2 = 1000000
        nombre_secret = random.randint(limite_basse, limite_haute_bot2)
        essai_max = int(log2(limite_haute_bot2))

    gagne = False

    print(f"Les bots jouent ! {joueur1} vs {joueur2}")
    print(f"{devineur} vous avez {essai_max} essais pour deviner le nombre")
    

    while not gagne and essai_max > 0:
        essai = -1
        if devineur == "BOT1":  # BOT1
            if niveau_bot1 == 1:  # Bot facile (choisit un nombre aléatoire)
                essai = random.randint(limite_basse, limite_haute_bot2)
            elif niveau_bot1 == 2:  # Bot intermédiaire (choisit un nombre près de la moyenne)
                essai = (limite_basse + limite_haute_bot2) // 2
                essai += random.randint(-10, 10)
            elif niveau_bot1 == 3:  # Bot difficile (choisit un nombre de manière optimisée)
                essai = (limite_basse + limite_haute_bot2) // 2

        elif devineur == "BOT2":  # BOT2
            if niveau_bot2 == 1:  # Bot facile (choisit un nombre aléatoire)
                essai = random.randint(limite_basse, limite_haute_bot1)
            elif niveau_bot2 == 2:  # Bot intermédiaire (choisit un nombre près de la moyenne)
                essai = (limite_basse + limite_haute_bot1) // 2
                essai += random.randint(-10, 10)
            elif niveau_bot2 == 3:  # Bot difficile (choisit un nombre de manière optimisée)
                essai = (limite_basse + limite_haute_bot1) // 2
        
        print(f"{devineur} propose : {essai}")
        time.sleep(1.5)
        
        if essai == nombre_secret:
            gagne = True
            print(f"\x1b[38;5;46m{devineur} a gagné \033[0m")
        else:
            if essai > nombre_secret and devineur == joueur2:
                limite_haute_bot1 = essai
                essai_max = essai_max - 1
                print(f"Il reste {essai_max} essais au {devineur} pour deviner le nombre")
            elif essai < nombre_secret and devineur == joueur2:
                limite_basse = essai
                essai_max = essai_max - 1
                print(f"Il reste {essai_max} essais au {devineur} pour deviner le nombre")
            elif essai > nombre_secret and devineur == joueur1:
                limite_haute_bot2 = essai
                essai_max = essai_max - 1
                print(f"Il reste {essai_max} essais au {devineur} pour deviner le nombre")
            elif essai < nombre_secret and devineur == joueur1:
                limite_basse = essai
                essai_max = essai_max - 1
                print(f"Il reste {essai_max} essais au {devineur} pour deviner le nombre")

    if not gagne:
        print(f"\x1b[38;5;46mLe nombre à deviner était {nombre_secret}. \n{decideur} a gagné !\033[0m")
