# Application Python de gestion des tâches

## Présentation
Cette application en console permet de gérer une liste de tâches quotidiennes.
Chaque tâche possède un numéro d'affichage et un titre. 
Les tâches sont conservées dans une liste Python pendant l'exécution du programme ; 
elles ne sont pas sauvegardées après la fermeture de l'application.

## Fonctionnalités
1. **Ajouter une tâche** : demande un titre et refuse une saisie vide.
2. **Afficher les tâches** : affiche toutes les tâches avec leur numéro ou indique
   si la liste est vide.
3. **Rechercher une tâche** : recherche un mot-clé dans les titres, sans tenir
   compte des majuscules et minuscules.
0. **Quitter** : ferme le programme.
Toute autre option affiche un message d'erreur.

## Fichier
- `main.py` : code source de l'application.

## Exécution avec Visual Studio Code
1. Ouvrir le dossier du projet dans VS Code.
2. Ouvrir le fichier `main.py`.
3. Cliquer sur **Run Python File**.
4. Utiliser le menu affiché dans le terminal.


## Étapes réalisées
- Création du programme et du menu principal.
- Ajout de la fonctionnalité d'ajout avec contrôle de saisie vide.
- Ajout de l'affichage numéroté des tâches.
- Ajout de la recherche par mot-clé.
- Tests des différentes options du menu.

## Limites de cette première version
Les tâches sont stockées uniquement en mémoire. Elles disparaissent lorsque
le programme est fermé. Aucune base de données ni interface graphique n'est utilisée.

## Fonctionnalités

- Ajouter une nouvelle tâche
- Afficher toutes les tâches
- Rechercher une tâche

## Lancement du programme

Exécuter la commande suivante dans le terminal :
python main.py