from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import pandas as pd
import TRUC


file = 'colloscope.xlsx'    #Nom du fichier excel
xl = pd.read_excel(file)    #Lecture du fichier ecel

j_indice, cellule, salle, matiere, description, date, date_2, gu, titre, annee= '', '', '', '', '', '', '', '', 'Colle de ', '2019'
liste, colle, sem, heure = [], [], [], []
mois, jour, type_matiere = {'1':'01','2':'02','3':'03','4':'04','5':'05','6':'06','7':'07','8':'08','9':'09','10':'10','11':'11','12':'12',}, {'lun':0,'mar':1,'mer':2,'jeu':3,'ven':4,}, {'maths':[1,14], 'physique':[14,23],'SI':[28,37],'francais':[37,42],'anglais':[42,50]}
heure_d, heure_f, uio, target, inter_debut, inter_fin = 0, 0, 8, 8, 0, 0


def recup_val(collone,ligne):
    '''Cette fonction renvoie le contenu d'une cellule, prenant comme parametre le nom de la collone et le numero de la ligne'''
    cellule = str(xl[str(collone)][(ligne)])
    return(cellule)
def maths(groupe, bool_affichage, bool_envoi, nom_matiere):
    '''Cette fonction fait tout !'''
    inter_debut = int(type_matiere.get(nom_matiere)[0])
    inter_fin = int(type_matiere.get(nom_matiere)[1])
    for j in range(6,26,1):                                 #Pour les semaines 6 à 26 (restantes)
        for u in range(inter_debut, inter_fin, 1):                            #Lignes
            j_indice = 'S' + str(j)
            try:
                if recup_val(j_indice,u) == str(groupe):    #Si le groupe X a colle :
                    #RECUPERATIONS DONEES
                    matiere = str(recup_val('Matiere',u))
                    liste.append(recup_val(j_indice,0)) #SEMAINE
                    liste.append(recup_val('Heure',u))
                    salle = str(recup_val('Salle',u))
                    colleur = (recup_val('Prof',u))
                    heure = recup_val('Heure',u)


                    #TRAITEMENT DES VARIABLES
                    heure = heure.split('.')
                        #JOUR SEM
                    jour_sem = heure[0]
                    jour_sem = jour.get(jour_sem)
                        #HEURES
                    heure = heure[1]
                    heure = heure.split('-')
                    heure = heure[0]
                    heure = heure.split(' ')
                    heure = heure[1]
                    heure_d = int(heure)
                    heure_f = heure_d + 1
                        #SEMAINES
                    sem = recup_val(j_indice,0)
                    sem = sem.split('/')
                        #MOIS
                    mois_f = sem[1]
                    mois_f = mois.get(mois_f)
                        #JOURS
                    jour_f = jour_sem + int(sem[0])

                    if bool_affichage == True:                   #Si on veut afficher
                        print("Matiere :", matiere)
                        print("Jour :",jour_f)
                        print("Mois :",mois_f)
                        print("Heure debut :",heure_d)
                        print('Heure Fin :',heure_f)
                        print("Colleur :",colleur)
                        print('Salle :',salle)

                    titre = 'Colle de ' + str(matiere)
                    salle = str(salle)
                    description = 'Colle de ' + str(matiere) + ' en ' + str(salle) + ' de ' + str(heure_d) + ' à ' + str(heure_f) + ' avec ' + str(colleur)
                    date = str(annee) +'-' + str(mois_f) + '-' + str(jour_f) + 'T' + str(heure_d) + ':00:00%s'
                    date_2 = str(annee) +'-' + str(mois_f) + '-' + str(jour_f) + 'T' + str(heure_f) + ':00:00%s'
                    
                    if bool_envoi == True:
                        print("DONNEES PREPAREES")
                        TRUC.envoi(titre,salle,description,date,date_2)     #Si on veut envoyer vers google agenda
                        print("DONNEES ENVOYEES")

                liste = []
            except:
                ()
    print("")
def export(groupe):
    maths(groupe, True, True, 'maths')
    maths(groupe, True, True, 'francais')
    maths(groupe, True, True, 'SI')
    maths(groupe, True, True, 'francais')
    maths(groupe, True, True, 'anglais')