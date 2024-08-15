import json
import random
from rich.console import Console
from time import sleep
import subprocess


console = Console()

# Charger les conjugaisons à partir du fichier JSON
with open('conjugaison.json', 'r',encoding='utf-8') as f:
    conjugaisons = json.load(f)

verbes = list(conjugaisons.keys())

# Fonction pour choisir un verbe et un temps au hasard
utilise = set()
dernier_verbe = []
dernier_temps = []


def choisir_exercice():
    global utilise, dernier_verbe, dernier_temps

    combinaisons_possibles = [(verbe, temps)
                              for verbe in verbes for temps in conjugaisons[verbe]]

    if len(utilise) == len(combinaisons_possibles):
        utilise = set()
        dernier_verbe = []
        dernier_temps = []

    while True:
        verbe = random.choice(verbes)

        temps = random.choice(list(conjugaisons[verbe].keys()))
        if len(dernier_verbe) == len(list(conjugaisons.keys())):
            dernier_verbe = []

        if len(dernier_temps) == len(list(conjugaisons[verbe].keys())):
            dernier_temps = []

        if (verbe, temps) not in utilise and temps not in dernier_temps and verbe not in dernier_verbe:
            utilise.add((verbe, temps))
            dernier_verbe.append(verbe)
            dernier_temps.append(temps)
            return verbe, temps


def exercice():
    points = 0
    verbe, temps = choisir_exercice()
    console.print(
        f"Conjugue le verbe '{verbe}' au temps '{temps}':", style="bold cyan")

    # Afficher la réponse correcte pour chaque personne
    for i, personne in enumerate(['je', 'tu', 'il', 'nous', 'vous', 'ils']):
        reponse = input(f"{personne} : ")
        verification = conjugaisons[verbe][temps][i].split()

        if len(verification) == 2:
            if reponse.strip().lower() == verification[1].lower():
                console.print("Correct!", style="bold green")
                sleep(1)
                subprocess.run(["powershell", "-Command", "Clear-Host"])
                points += 1
            else:

                console.print(
                    f"Incorrect. La bonne réponse est: {verification[1]}", style="bold red")
                sleep(1)
                subprocess.run(["powershell", "-Command", "Clear-Host"])
        elif len(verification) > 2:
            if temps.split()[0] != 'subjonctif':
                if reponse.strip().lower() == f'{verification[1].lower()} {verification[2].lower()}':
                    console.print("Correct!", style="bold green")
                    sleep(1)
                    subprocess.run(["powershell", "-Command", "Clear-Host"])
                    points += 1
                else:

                    console.print(
                        f"Incorrect. La bonne réponse est: {verification[1].lower()} {verification[2].lower()}", style="bold red")
                    sleep(1)
                    subprocess.run(["powershell", "-Command", "Clear-Host"])
            else:
                global subjonctif_input
                if verification[0].lower() == 'que':
                    subjonctif_input = f'{verification[0].lower()} {verification[1].lower()} {verification[2].lower()}'
                else:
                    subjonctif_input = f'{verification[0].lower()}{verification[1].lower()} {verification[2].lower()}'

                if reponse.strip().lower() == subjonctif_input:
                    console.print("Correct!", style="bold green")
                    sleep(1)
                    subprocess.run(["powershell", "-Command", "Clear-Host"])
                    points += 1
                else:
                    if verification[0].lower() == 'que':
                        console.print(
                            f"Incorrect. La bonne réponse est: {verification[0].lower()} {verification[1].lower()} {verification[2].lower()}", style="bold red")
                        sleep(1)
                        subprocess.run(
                            ["powershell", "-Command", "Clear-Host"])
                    else:
                        console.print(
                            f"Incorrect. La bonne réponse est: {verification[0].lower()}{verification[1].lower()} {verification[2].lower()}", style="bold red")
                        sleep(1)
                        subprocess.run(
                            ["powershell", "-Command", "Clear-Host"])

    return points


def main():
    try:
        goal = int(input(
            'Veuillez entrer le nombre de bonnes réponses requises pour terminer la session: '))
    except ValueError:
        console.print("Veuillez entrer un nombre valide", style="bold red")
        return
    total_points = 0
    while total_points < goal:
        points = exercice()
        total_points += points
        console.print(
            f"Votre score actuel est : {total_points} points.", style="bold purple")
        if total_points >= goal:
            console.print(
                f"Félicitations, vous avez atteint {goal} points!", style="bold green")
            break


if __name__ == "__main__":
    main()
