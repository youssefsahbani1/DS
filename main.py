"""Application console de gestion des tâches (Partie 1)."""

taches = []  # liste de titres ; le numéro d'une tâche = sa position + 1


def afficher_menu():
    print("\n=== GESTION DES TÂCHES ===")
    print("1. Ajouter une tâche   2. Afficher   3. Rechercher   0. Quitter")


def ajouter_tache():
    titre = input("Titre de la tâche : ").strip()
    if titre == "":
        print("Erreur : le titre ne peut pas être vide.")
        return
    taches.append(titre)
    print("Tâche ajoutée avec succès.")


def main():
    continuer = True
    while continuer:
        afficher_menu()
        choix = input("Votre choix : ").strip()
        if choix == "1":
            ajouter_tache()
        elif choix == "2":
            afficher_taches()
        elif choix == "3":
            rechercher_tache()
        elif choix == "0":
            print("Au revoir !")
            continuer = False
        else:
            print("Erreur : option invalide.")


main()