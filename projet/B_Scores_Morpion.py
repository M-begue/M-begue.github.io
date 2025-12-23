import json
try:
    from js import localStorage
except ImportError:
    localStorage = None

def charger_scores_morpion() -> list[tuple[str, int]]:
    scores = []
    if localStorage:
        data = localStorage.getItem('scores_morpion')
        if data:
            temp_list = json.loads(data)
            scores = [tuple(item) for item in temp_list]
    return scores

def sauvegarder_scores_morpion(scores: list[tuple[str, int]]) -> None:
    if localStorage:
        data_json = json.dumps(scores)
        localStorage.setItem('scores_morpion', data_json)

def ajouter_score_morpion(gagnant: str, scores: list[tuple[str, int]]) -> None:
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
            
    sauvegarder_scores_morpion(scores)

def afficher_scores_morpion() -> None:
    scores = charger_scores_morpion()
    if not scores:
        print("\nAucun score disponible.")
    else:
        print("\n--- Classement des scores Morpion ---")
        for i, (nom, pts) in enumerate(scores, start=1):
            print(f"{i}. {nom} : {pts} points")
        print("--------------------------------------")