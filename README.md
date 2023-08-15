<p align='center' >
<img src='logo.png' >
</p>

# Créez une API sécurisée RESTful en utilisant Django REST

SoftDesk, une société d'édition de logiciels de collaboration, a décidé de publier une application permettant de remonter et suivre des problèmes techniques
Il faut alors trouver un moyen standard de traiter les données, ce qui peut se faire en développant une API RESTful.

___

# Installation du projet:

## Cloner le projet:
```bash
    git clone https://github.com/LGD-P/P10_Open_C.git
```
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

-----


# Listing des End-Points et usages avec Postman ou Curl: 



|C.R.U.D method|URI & Catégories |Réponse|
|:-:|:-:|:-:|
||**User**||
|GET|api/user|Liste des Utilisateurs|
|GET|api/user/id|Utilisateur selon son id|
|POST|api/user|Création d'un utilisateur|
|PUT or PATCH|api/user/id|PUT modifie et écrase les données de l'Utilisateur non renseignées, PATCH modifie uniquement les champs renseignés|
|DELETE|api/user/id|Supprime l'utilisateur selon son id|
||**Contributor**||
|GET|api/contributor|Liste des Contributeurs|
|GET|api/contributor/id|Détail du contributeur selon son id|
|POST|api/contributor/|Ajout d'un contributeur à un projet|
|PUT or PATCH|api/contributor/id|PUT modifie et écrase les données du Contributeur non renseignées, PATCH modifie uniquement les champs renseignés|
|DELETE|api/contributor/id|Supprime le Contributeur selon son id|
||**Project**||
|GET|api/project/|Liste des Projets|
|GET|api/project/id|Détail du Projet selon son Id|
|POST|api/project/Création d'un projet|
|PUT or PATCH|api/project/id|PUT modifie et écrase les données du Projet non renseignées, PATCH modifie uniquement les champs renseignés|
|DELETE|api/project/id|Supprime le Contributeur selon son id|
||**Issue**||
|GET|api/issue/|Liste de toutes issues|
|GET|api/issue/id| Détail de l'issue selon son id|
|POST|api/issue/Création d'un issue|
|PUT or PATCH|api/issue/id|PUT modifie et écrase les données de l'Issue non renseignées, PATCH modifie uniquement les champs renseignés|
|DELETE|api/issue/id|Supprime l'Issue selon son id|
||**Comment**||
|GET|api/comment/|Liste de toutes les Comments|
|GET|api/comment/id|Détails du Comment selon son id|
|POST|api/comment/|Création d'un Comment|
|PUT or PATCH|api/comment/id|PUT modifie et écrase les données du Comment non renseignées, PATCH modifie uniquement les champs renseignés|
|DELETE|api/comment/id|Supprime le Comment selon son id|

## Le CRUD avec POSTMAN: 

- *Assurez vous  d'avoir dans le **Header** la clefs Content-Type et la valeur application/json* 
- *Dans le **Body** les data sont passées en raw format en JSON*

exemple pour la création d'un utilisateur: 


|Method|URL|URI|Body (raw JSON)|
|:-:|:-:|:-:|:-:|
|POST|127.0.0.1:8000/|api/user/|{"username": "Marie","age": 32, "can_be_shared": false, "can_be_contacted": false}|




## Le CRUD exemple d'utilisation avec curl:

* Le flag -X spécifie la méthode HTTP à utiliser, 
* Le flag -H spécifie l'en-tête de la requête, dans notre cas : "Content-Type: application/json" pour indiquer que les données sont au format JSON.
* Le flag -d spécifie les données à envoyer dans la requête dans notre cas un dictionnaire de données.


Pour créer une nouvelle ressource avec curl, vous pouvez utiliser la méthode POST :

    curl -X POST -H "Content-Type: application/json" -d '{
        "username": "Marie",
        "age": 32,
        "can_be_shared": false,
        "can_be_contacted": false
    }' http://127.0.0.1:8000/api/user/

Pour récupérer une ressource existante avec curl, vous pouvez utiliser la méthode GET :

    curl -X GET http://127.0.0.1:8000/api/user/1/

Pour mettre à jour une ressource existante avec curl, vous pouvez utiliser la méthode PUT ou PATCH :

Avec PUT (remplacement complet de la ressource) :

    curl -X PUT -H "Content-Type: application/json" -d '{
        "username": "Marie",
        "age": 33,
        "can_be_shared": true,
        "can_be_contacted": true
    }' http://127.0.0.1:8000/api/user/1/

Avec PATCH (mise à jour partielle de la ressource) :

    curl -X PATCH -H "Content-Type: application/json" -d '{
        "age": 33
    }' http://127.0.0.1:8000/api/user/1/

Pour supprimer une ressource avec curl, vous pouvez utiliser la méthode DELETE :

    curl -X DELETE http://127.0.0.1:8000/api/user/1/






