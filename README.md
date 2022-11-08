# Exercices - Méthodes et Statistiques

Ces exercices tournent autour de la maitrise de Python dans le but d'évaluer le ou la candidat·e sur ses capacités d'organisation et de développement.

Pour ces exercices, nous proposons de travailler sur les données fournies par nos soins.

## Préparation de l'environnement et présentation des attentes

Nous utiliserons Python dans sa version [3.10](https://www.python.org/downloads/).
Il est attendu du ou de la candidat·e le projet structuré final permettant de répondre aux problématiques décrites ci-après.

La base de données est fournie par le fichier SQLite `data/penguins.sqlite`.

L'exploitation de cette base de données peut-être réalisée en utilisant le module `sqlite3` de la bibliothèque standard de Python :

```python
import sqlite3

with sqlite3.connect("data/penguins.sqlite") as co:
    co.execute(
            "SELECT * FROM penguins"
        ).fetchall()
```

Nous encourageons le ou la candidat·e à utiliser les outils de son choix, tant que l'approche est documentée et reproductible (par exemple, fournir un fichier `requirements.txt`).

## Évaluation

L'enjeu de ces exercices est de mettre en valeur votre capacité à fournir un travail réutilisable par d'autres collaborateurs.
Nous serons particulièrement intéressés par les structures de programmation que vous mettrez en place.
Nous accordons au sein de nos équipes une grande importance au fait de pouvoir reprendre le travail d'une autre personne.
Par conséquent, le travail restitué sera évalué selon les modalités suivantes (par ordre décroissant d'importance) :
- **Organisation** : le travail est-il correctement structuré ? Est-ce aisé de naviguer dans le projet et de réutiliser les briques développées ? L'historique de développement est-il correctement versionné ?
- **Documentation** : les fonctionnalités sont-elles suffisamment documentées pour être facilement réutilisables par d'autres personnes ? 
- **Clean code** : le code source est-il de qualité ? Bien formaté, construit, et respectant les conventions stylistiques du langage ?
- **Résultat** : les résultats sont-ils conformes aux attentes ?

## Tâches

### Création d'un module d'analyses descriptives

- 1.1 Reproduire l'arborescence de fichiers suivante à la racine du projet
```text
/
├── main.py
├── description/
│   └── __init__.py
└── ...
```
- 1.2 Dans le fichier `main.py`, ajouter le nécessaire pour la lecture des données depuis la base fournie dans le dossier `data/` à la racine du projet

### Création des fonctions d'analyse

- 2.2 Dans le module `description`, ajouter une fonction permettant d'obtenir une table des fréquences à partir d'une série de données. Utiliser cette fonction dans le fichier racine `main.py`
- 2.3 Dans le module `description`, ajouter une fonction de création d'un histogramme pour décrire visuellement une série de données numériques. Utiliser cette fonction dans le fichier racine `main.py`
- 2.4 TODO : utilisation d'un modèle ?

### Conversion d'un code existant

- 3.1 TODO : conversion d'une macro SAS ?




