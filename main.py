# Application Python de gestion des tâches
# Partie 1 - Projet Git / GitHub

tasks = []


def add_task():
    """Demande un titre et ajoute une tâche si la saisie n'est pas vide."""
    title = input("Titre de la tâche : ").strip()
    if not title:
        print("Erreur : le titre ne peut pas être vide.")
        return
    tasks.append(title)
    print("Tâche ajoutée avec succès.")


def show_tasks():
    """Affiche toutes les tâches avec leur numéro."""
    if not tasks:
        print("Aucune tâche enregistrée.")
        return
    print("\n--- LISTE DES TÂCHES ---")
    for number, title in enumerate(tasks, start=1):
        print(f"{number}. {title}")


def search_task():
    """Recherche les tâches dont le titre contient le mot-clé."""
    keyword = input("Mot-clé à rechercher : ").strip()
    if not keyword:
        print("Erreur : le mot-clé ne peut pas être vide.")
        return
    results = [
        (number, title)
        for number, title in enumerate(tasks, start=1)
        if keyword.casefold() in title.casefold()
    ]
    if not results:
        print("Aucune tâche correspondante.")
        return
    print("\n--- RÉSULTATS DE LA RECHERCHE ---")
    for number, title in results:
        print(f"{number}. {title}")


def main():
    """Affiche le menu et traite les choix de l'utilisateur."""
    while True:
        print("\n=== GESTION DES TÂCHES ===")
        print("1. Ajouter une tâche")
        print("2. Afficher les tâches")
        print("3. Rechercher une tâche")
        print("0. Quitter")
        choice = input("Votre choix : ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            search_task()
        elif choice == "0":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez choisir 1, 2, 3 ou 0.")
        if __name__ == "__main__":
            main()
