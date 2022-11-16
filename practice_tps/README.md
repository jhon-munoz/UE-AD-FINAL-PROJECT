# UE-AD-FINAL-PROJECT

## Tasks

### TP1 - Créer un service pour la gestion d’utilisateurs

1.Compléter le modèle pour les utilisateurs
- [x] Avec le rôle et d’autres attributs de base.
2. Mettre en place un système de rôles avec les droits suivants : 
- [ ] Admin → a accès à toutes les fonctionnalitées 
- [ ] Player → peut s’enregistrer et consulter ses informations mais pas celles des autres utilisateurs; il peut juste voir leur noms. Un utilisateur de type player peut avoir 0, 1 ou plusieurs badges (récompenses)
- [ ] Reporter → a accès à toutes les informations mais en lecture seule 
3. Implementer les endpoints
- [x] Création d’un utilisateur avec un email + mot de passe avec un payload JSON
- [x] Mettre à jour les informations d’un utilisateur avec un payload JSON
- [x] Effacer un utilisateur en mode soft-delete (on le garde en BD mais il n’est plus visible)
- [x] Listing des utilisateurs
- [ ] Ajouter un paramètre pour voir les utilisateurs effacés (seulement disponible pour le rôle Admin)
- [x] Trouver un utilisateur par son id : GET users/123
- [x] Trouver un utilisateur par son nom : GET users?name=toto
- [x] Gérer correctement les erreurs (retourner les bons codes HTTP)

### TP2

1. On va avoir besoin d’un nouveau endpoint côté users-api pour retrouver un utilisateur à partir d’un username et password
2. Créer un service d'authentification. Le service communique avec le service users-api pour récupérer les informations d’un utilisateur. Il expose deux endpoints :
- [ ] POST /authenticate
Récupère les informations de l’utilisateur pour générer un tokenInput : username, password
Output: un token qui contient le username et rôle de l’utilisateur
- [ ] GET /user-context
Décode le token pour extraire les informations de l’utilisateur
Input : le  token d’authentification
Output : {username, rôle}
3. Exécuter les deux services (users-ap & auth) dans des conteneurs via docker-compose


The project is composed of 4 services each one with its own folder. The services are:
* `movie` (GraphQL)
* `showtime` (gRPC)
* `booking` (gRPC)
* `user` (the only one accessed through a REST API)

Each service runs using Python 3.10

Inside each folder you will find:
* Main server file (`*.py`)
* Dockerfile to build service image
* Python library requirements (`requirements.txt`)
* `data` folder with the `.json` file that holds the service data
* `protos` folder with the `.proto` file of the service describing its stubs

### Running locally

```
make
cd movie
python3.10 movie.py
cd showtime
python3.10 showtime.py
cd booking
python3.10 booking.py
cd user
python3.10 user.py [-H HOST] -p PORT
```

### Running with Docker

```
make
docker-compose up [--build] ${SERVICE}
```
