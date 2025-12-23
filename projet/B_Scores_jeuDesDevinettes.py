import json
try:
    from js import localStorage
except ImportError:
    localStorage = None

def charger_scores_devinettes() -> list[tuple[str, int]]:
    scores = []
    if localStorage:
        data = localStorage.getItem('scores_devinettes')
        if data:
            # Conversion JSON (listes) vers Python (tuples)
            temp_list = json.loads(data)
            scores = [tuple(item) for item in temp_list]
    return scores

def sauvegarder_scores_devinettes(scores: list[tuple[str, int]]) -> None:
    if localStorage:
        data_json = json.dumps(scores)
        localStorage.setItem('scores_devinettes', data_json)

def ajouter_score_devinettes(gagnant: str, scores: list[tuple[str, int]]) -> None:
    joueur_trouve = False
    for i in range(len(scores)):
        if scores[i][0] == gagnant:
            joueur_trouve = True
            nouveau_score = scores[i][1] + 1
            scores[i] = (scores[i][0], nouveau_score)
            
            position = i
            while position > 0 and scores[position][1] > scores[position - 1][1]:
                scores[position], scores[position - 1] = scores[position - 1], scores[position]
                position -= 1
            break

    if not joueur_trouve:
        scores.append((gagnant, 1))
        position = len(scores) - 1
        while position > 0 and scores[position][1] > scores[position - 1][1]:
            scores[position], scores[position - 1] = scores[position - 1], scores[position]
            position -= 1
    
    sauvegarder_scores_devinettes(scores)

def afficher_scores_devinettes() -> None:
    scores = charger_scores_devinettes()
    if not scores:
        print("\nAucun score disponible.")
    else:
        print("\n--- Classement des scores Devinettes ---")
        for i, (nom, pts) in enumerate(scores, start=1):
            print(f"{i}. {nom} : {pts} points")
        print("--------------------------------------")