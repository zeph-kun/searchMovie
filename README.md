# Installation du projet
## Introduction

Ce projet est une application web en Djanfo qui permet de rechercher des films en utilisant l'API OMDB. L'utilisateur 
peut rechercher un film par son titre et voir les détails du film.

## Prérequis

* Cloner le Repository : git clone https://github.com/zeph-kun/searchMovie.git
* Créer un environnement virtuel : python -m venv .venv
* Activer l'environnement virtuel : source .venv/bin/activate
* Installer les dépendances : pip install -r requirements.txt
* Créer une clef api sur :  http://www.omdbapi.com/
* Créer un fichier .env à la racine du projet et ajouter les variables d'environnement suivantes : SECRET_KEY=VotreClefAPI

## Lancer le projet
* Lancer le serveur : python manage.py runserver
* Aller sur : http://127.0.0.1:8000/