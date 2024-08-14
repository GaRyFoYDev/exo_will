from rich.prompt import Prompt
from rich.console import Console
from random import shuffle



# Instancier la console rich
console = Console()


import json
from random import shuffle
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def charger_vocabulaire(fichier_json):
    with open(fichier_json, 'r', encoding='utf-8') as f:
        return json.load(f)

def quiz(vocabulaire):
    # Demander le score à atteindre à l'élève
    while True:
        try:
            score_a_atteindre = int(Prompt.ask(
                "Choisissez un score à atteindre pour réussir le quiz (entier positif)"))
            if 0 < score_a_atteindre <= len(vocabulaire):
                break
            else:
                console.print(
                    f"[bold red]Veuillez entrer un nombre entre 1 et {len(vocabulaire)}.[/bold red]")
        except ValueError:
            console.print(
                "[bold red]Veuillez entrer un nombre entier valide.[/bold red]")

    # Mélanger les mots pour le quiz
    mots = list(vocabulaire.keys())
    shuffle(mots)

    score = 0
    total_questions = len(mots)

    console.print(f"\nBienvenue au quiz de vocabulaire !\n")
    console.print(
        f"Objectif : Atteindre un score de [bold green]{score_a_atteindre}[/bold green].\n")

    for mot in mots:
        definition = vocabulaire[mot]
        console.print(f"\nDéfinition : [bold green]{definition}[/bold green]")
        reponse = Prompt.ask("Quel est le mot ?").lower()

        if reponse == mot:
            score += 1
            console.print("[bold blue]Bonne réponse ![/bold blue]")
        else:
            console.print(
                f"[bold red]Mauvaise réponse ! Le bon mot était : {mot}[/bold red]")

        console.print(
            f"Score actuel : [bold yellow]{score}/{score_a_atteindre}[/bold yellow]\n")
        if score >= score_a_atteindre:
            break

    if score >= score_a_atteindre:
        console.print(
            f"\n[bold green]Félicitations ! Vous avez atteint votre objectif avec un score de {score}/{score_a_atteindre}.[/bold green]")
    else:
        console.print(
            f"\n[bold red]Vous n'avez pas atteint l'objectif. Score final : {score}/{score_a_atteindre}.[/bold red]")


# Charger le vocabulaire à partir du fichier JSON
vocabulaire_cm2 = charger_vocabulaire('vocabulaire.json')

# Lancer le quiz
quiz(vocabulaire_cm2)



