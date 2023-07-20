<p align='center' >
<img src='logo.png' >
</p>

# Créez une API sécurisée RESTful en utilisant Django REST

SoftDesk, une société d'édition de logiciels de collaboration, a décidé de publier une application permettant de remonter et suivre des problèmes techniques
Il faut alors trouver un moyen standard de traiter les données, ce qui peut se faire en développant une API RESTful.

___


## Cloner le projet:

    git clone https://github.com/LGD-P/P10_Open_C.git

## Installer le gestinnaire de dépendances poetry:
    
    pip3 install poetry 

## Activer l'environnement virtuel:

    poetry shell 

## Installer les dépendances:

    poetry install 


## Appliquer une 1ère migration:

    python3 manage.py migrate

## Lancer Django REST:

    python3 manage.py runserver

*En général c'est le port 8000 qui est ouvert il n'y a plus qu'a suivre le lien : "Starting development server at http://......." pour accéder à l'application.*







