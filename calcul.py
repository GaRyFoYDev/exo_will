import random
import operator
from rich.console import Console
from rich.table import Table

console = Console()


def generer_operation():
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    nombres = []

    while len(nombres) < 3:
        nombre = random.randint(2, 20)
        if nombre % 10 != 0 and nombre not in nombres:
            nombres.append(nombre)

    # Choisir deux opérations aléatoires
    op1 = random.choice(list(operations.keys()))
    op2 = random.choice(list(operations.keys()))

    # Créer une expression en respectant les règles de priorité
    if op2 == '*' or (op1 != '*' and random.choice([True, False])):
        expression = f"{nombres[0]} {op1} {nombres[1]} {op2} {nombres[2]}"
    else:
        expression = f"{nombres[0]} {op1} ({nombres[1]} {op2} {nombres[2]})"

    # Évaluer l'expression
    resultat = eval(expression)

    return expression, resultat


def exercice_calcul_mental():
    # Demander le nombre de tours réussis
    console.print("Bienvenue dans l'exercice de calcul mental !",
                  style="bold underline blue")

    while True:
        try:
            tours_voulus = int(console.input(
                "[bold green]Combien de tours réussis souhaitez-vous obtenir pour terminer ? [/bold green]"))
            break
        except ValueError:
            console.print(
                '[bold red]Veuillez entrer un chiffre valide.[/bold red]')

    tours_effectues = 0

    while tours_effectues < tours_voulus:
        expression, resultat = generer_operation()
        console.print(f"\n[bold cyan]Calculez : {expression}[/bold cyan]")

        try:
            reponse = int(console.input("Votre réponse : "))
        except ValueError:
            console.print(
                '[bold red]Veuillez entrer un chiffre valide.[/bold red]')
            continue

        if reponse == resultat:
            console.print("[bold green]Bravo, c'est correct![/bold green]")
            tours_effectues += 1
        else:
            console.print(
                f"[bold red]Dommage, la bonne réponse était {resultat}.[/bold red]")

        # Affichage du tableau des scores
        table = Table(title="Progression")
        table.add_column("Tours réussis", justify="center")
        table.add_row(f"{tours_effectues}/{tours_voulus}")
        console.print(table)

    console.print(
        f"[bold magenta]Félicitations ! Vous avez atteint {tours_voulus} tours réussis.[/bold magenta]")
    console.print(
        f"[bold yellow]Vous avez terminé avec {tours_effectues} tours réussis. Bien joué![/bold yellow]")


# Lancer l'exercice de calcul mental
exercice_calcul_mental()
