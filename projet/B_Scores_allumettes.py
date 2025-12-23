import json
# On tente d'importer le module 'js' qui n'existe que dans l'environnement PyScript (le navigateur)
try:
    from js import localStorage
except ImportError:
    localStorage = None

def charger_scores_allumettes() -> list[tuple[str, int]]:
    """Charge les scores depuis le localStorage du navigateur."""
    scores = []

    if localStorage:
        data = localStorage.getItem('scores_allumettes')
        if data:
            try:
                # Le format JSON ne connaît pas les tuples, il transforme tout en listes [nom, score]
                temp_list = json.loads(data)
                # On convertit les listes internes en tuples pour rester fidèle à votre typage
                scores = [tuple(item) for item in temp_list]
                print("Scores chargés avec succès !")
            except Exception:
                print("Erreur lors de la lecture des scores.")
                scores = []
        else:
            print("Aucun score enregistré dans le navigateur.")
    else:
        print("Environnement hors-ligne : stockage indisponible.")

    return scores

def sauvegarder_scores_allumettes(scores: list[tuple[str, int]]) -> None:
    """Sauvegarde la liste des scores dans le localStorage au format JSON."""
    if localStorage:
        # On convertit la liste de tuples en format JSON (texte)
        data_json = json.dumps(scores)
        localStorage.setItem('scores_allumettes', data_json)
        print("Sauvegarde effectuée dans le navigateur.")
    else:
        print("Sauvegarde impossible : localStorage introuvable.")

def ajouter_score_allumettes(gagnant: str, scores : list[tuple[str, int]]) -> None:
    """Ajoute un point et trie la liste (votre logique originale)."""
    joueur_trouve = False
    
    # Recherche du joueur et mise à jour
    for i in range(len(scores)):
        if scores[i][0] == gagnant:
            joueur_trouve = True
            nouveau_score = scores[i][1] + 1
            scores[i] = (scores[i][0], nouveau_score)

            # Tri manuel vers le haut
            position = i
            while position > 0 and scores[position][1] > scores[position - 1][1]:
                scores[position], scores[position - 1] = scores[position - 1], scores[position]
                position -= 1
            break

    # Si nouveau joueur
    if not joueur_trouve:
        scores.append((gagnant, 1))
        position = len(scores) - 1
        while position > 0 and scores[position][1] > scores[position - 1][1]:
            scores[position], scores[position - 1] = scores[position - 1], scores[position]
            position -= 1

    # APPEL DE LA SAUVEGARDE WEB
    sauvegarder_scores_allumettes(scores)

def afficher_scores_allumettes() -> None:
    """Affiche les scores dans la console PyScript."""
    scores = charger_scores_allumettes()
    
    if not scores:
        print("\nAucun score disponible.")
    else:
        print("\n--- CLASSEMENT DES SCORES ALLUMETTES ---")
        for i, (nom, pts) in enumerate(scores, start=1):
            print(f"{i}. {nom} : {pts} points")
        print("----------------------------------------")