import random
from rich.console import Console

console = Console()


def jeu_multiplication():
    points = 0

    while points < 100:
        num1 = random.randint(2, 20)
        num2 = random.randint(2, 20)

        produit = num1 * num2

        try:
            reponse = int(input(f"Combien font {num1} x {num2} ? "))

            if reponse == produit:
                points += 1
                console.print(
                    f"Bonne réponse ! Votre score est maintenant de {points}/100", style="bold green")
            else:
                console.print(
                    f"Mauvaise réponse, la réponse correcte était {produit}", style="bold red")

        except ValueError:
            console.print("Veuillez entrer un nombre valide.",
                          style="bold yellow")

    console.print("Félicitations ! Vous avez atteint 100 points.",
                  style="bold purple")


# Démarrer le jeu
jeu_multiplication()

