from pyscript import display

from B_Morpion import morpion
from B_Allumettes import allumette
from B_Jeu_Des_Devinettes import jeu_robot_vs_robot

from B_Scores_Morpion import charger_scores_morpion
from B_Scores_allumettes import charger_scores_allumettes
from B_Scores_jeuDesDevinettes import charger_scores_devinettes


# Chargement des scores
scores_morpion = charger_scores_morpion()
scores_allumettes = charger_scores_allumettes()
scores_devinettes = charger_scores_devinettes()


def demo_morpion():
    display("🎮 Morpion — BOT vs BOT", target="output", append=False)
    morpion(
        "BOT1",
        "BOT2",
        2,  # niveau BOT1
        3,  # niveau BOT2
        scores_morpion
    )


def demo_allumettes():
    display("🔥 Allumettes — BOT vs BOT", target="output", append=False)
    allumette(
        "BOT1",
        "BOT2",
        2,
        3,
        3,
        scores_allumettes
    )


def demo_devinette():
    display("🔢 Devinette — BOT vs BOT", target="output", append=False)
    jeu_robot_vs_robot(2, 3)
