# Réponses aux questions de TP

## I. Prise en main

### Question 1

Il s'agit d'une topology en étoile. Tous les périphériques du réseau sont connecté sur un même serveur central.

### Question 2

Il est possible de lire les messages dans le terminal serveur "python3 source/chat_server.py".
On a accès aux noms et messages des utilisateurs.

### Question 3

C'est un problème de sécurité. Car il est possible de récupérer des informations confidentielles : nom, mots de passe, IP ...
Ce problème viole le principe de Kerckhoffs.

### Question 4

La solution la plus évidente est de mettre en place un système de chiffrement.

## II. Chiffrement

### Question 1

urandom n'est pas considéré comme un choix sûr pour la cryptographie. Cette fonction fournit des nombres aléatoires en utilisant des sources fournies par le système d'exploitation. Cependant, sa qualité et sa prévisibilité dépendent fortement de l'environnement du système.

### Question 2

Utiliser des primitives cryptographiques de manière incorrecte peut être dangereux car cela peut affaiblir ou complètement annuler les garanties de sécurité offertes par ces primitives.

### Question 3

Le serveur malveillant peut collecter des informations sur l'utilisateur, telles que son adresse IP ou les données qu'il envoie, et les utiliser pour lancer des attaques ultérieures.

### Question 4

Il manque la vérification de l'intégrité des données ciruculant sur le serveur.


# III. Authenticated Symetric Encryption

### Question 1

Fernet est moins risqué que le chiffrement en termes d'implémentation car il gère  automatiquement la génération des clés, l'initialisation du vecteur d'initialisation et la gestion des erreurs.

### Question 2

Il s'agit d'une attaque de rejeu. L'attaquant enregistre des messages chiffrés précédemment échangés entre deux utilisateurs et les renvoie à l'un des deux. Si les messages renvoyés sont acceptés, l'attaquant peut accéder aux données échangées.

### Question 3

Pour se protéger contre les attaques de rejeu, on utilise un nonce, il s'agit d'un nombre aléatoire généré par l'émetteur. Le récepteur vérifie que le nonce est unique pour chaque message reçu, ce qui empêche l'attaquant de renvoyer des messages précédemment échangés.