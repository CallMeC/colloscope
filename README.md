# colloscope
Export de colloscope vers Googe Agenda

Ce proramme permet d'exporter les colles présents sur le document excel vers son compte Google Agenda.


Instructions :


Créer un dossier "colloscope" et y mettre tous les fichiers présents sur ce github.


Installer Python et PIP :

https://matthewhorne.me/how-to-install-python-and-pip-on-windows-10/


Installation des dépendences :

pip install pandas

pip install auth2client

pip install xlrd

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib


How to :
Activer l'API Google Agenda (Penser à se connecter avec le compte google sur lequel nous voulons l'agenda):

https://developers.google.com/calendar/quickstart/python

Télecharger le fichier de configuration credentials.json et le copier dans le dossier précédement créé


Décommenter la fonction envoi dans TRUC.py pour le premier lancement.

Lancer le script TRUC.py, cela devrait ouvrir une nouvelle fenetre internet.

Connectez vous à votre compte Google et acceptez les autorisations nécessaires, puis fermez la fenetre.

Re-commentez la fonction envoi dans TRUC.py


Vous pouvez ouvrir le fichier quickstart.py

Les instructions sont à la fin

