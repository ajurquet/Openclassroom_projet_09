# Projet Développez une application Web en utilisant Django,  HTML - CSS - Python

### Openclassroom projet 09

Projet consistant à créer un site web pour la start-up LITReview. Son objectif est de créer un site web permettant à une communauté de passionnés de livres de pouvoir échanger des avis.

La conception du site doit utiliser le framework Django, et doit se concentrer sur le backend. La partie frontend du site est volontairement minimaliste.  

Le site doit respecter les directives suivantes :
 - L'utilisateur doit pouvoir créer un compte et se connecter.
 - L'utilisateur doit pouvoir demander et poster des critiques.
 - L'utilisateur doit pouvoir suivre d'autres d'utilisateurs, et avoir accès à une page où il peut vérifier les utilisateurs suivis ainsi que ceux qui le suivent.
 - L'utilisateur doit avoir accès à une page où sont situés toutes ses critiques et demandes de critiques.
 - L'utilisateur doit avoir accès à une page de flux, affichant les différentes critiques et demandes, suivant une logique prédéfinie. 

Le projet utilise les langages HTML, CSS et Python.

## Prérequis

Vous devez installer python, la dernière version se trouve à cette adresse 
https://www.python.org/downloads/

Les scripts python se lancent depuis un terminal, pour ouvrir un terminal sur Windows, pressez ``` touche windows + r``` et entrez ```cmd```.

Sur Mac, pressez ```touche command + espace``` et entrez ```terminal```.

Sur Linux, vous pouvez ouvrir un terminal en pressant les touches ```Ctrl + Alt + T```.

Le programme utilise plusieurs librairies externes, et modules de Python, qui sont répertoriés dans le fichier ```requirements.txt```


Il est préférable d'utiliser un environnement virtuel, vous pouvez l'installer via la commande :  
```bash
pip install venv
```

Vous devez ensuite créer et activer un environnement en entrant les commandes suivantes dans le terminal:

##LINUX MACOS

```bash
python3 -m venv env
```
puis :
```bash
source env/bin/activate
```
et enfin :

```bash
pip install -r requirement.txt
```
afin d'installer toutes les librairies.

##WINDOWS

```bash
python -m venv env
```
puis :
```bash
source env/Scripts/activate
```
et enfin :

```bash
pip install -r requirement.txt
```
afin d'installer toutes les librairies.

## Démarrage 

Le programme est écrit en Python, copier tous les fichiers et répertoires du repository, naviguer vers le répertoire LITReview et entrez dans la commande suivante dans le terminal :

```bash
python manage.py runserver
```

pour lancer le serveur, puis entrez l'adresse suivante dans le navigateur : http:/127.0.0.1:8000/

Afin de tester les différentes fonctionalités du site, il y a 3 utilisateurs crées : "Alex", "Florent" et "Martin".
Le mot de passe est le même pour les 3 : "setting4321" (sans les guillemets).

Vous pouvez vous connecter à l'interface d'administration via le compte "admin", mot de passe "admin" (sans les guillemets).


## Rapport flake8

Le programme est conforme à la PEP8, le repository contient un rapport flake8, qui n'affiche aucune erreur. Il est possible d'en générer un nouveau en installant le module ```flake8``` et en entrant dans le terminal :

```bash
flake8
```

Le fichier ```setup.cfg``` à la racine contient les paramètres concernant la génération du rapport.
