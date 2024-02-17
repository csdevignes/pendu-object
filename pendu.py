'''
Activité n°7
Jeu du pendu en objet

@Usage:
python pendu.py [-l <lexique.txt>]

@author: Claire-Sophie Devignes
@copyright: Institut des sciences du Digital, Management & Cognition – IDMC
@license: MIT License
@version: 1.0
@email: claire-sophie.devignes9@etu.univ-lorraine.fr
@date: 5 février 24
'''

import lexique
import jeu
import argparse

## Définition d'arguments pour l'utilisation en ligne de commande
#Création d'un objet parser de type ArgumentParser
parser = argparse.ArgumentParser(description="Analyse d'arguments")
#Ajouter l'argument -l --lexique
parser.add_argument('-l', '--lexique', help="Chemin vers le dictionnaire de mots.")
#Analyse des arguments de la ligne de commande
args = parser.parse_args()
#Recupérer le chemin du fichier lexique à partir des arguments
lexique_file = args.lexique
nom_fichier = lexique_file

#Chargement du dictionnaire de mots par défaut, si non spécifié.
if not nom_fichier:
    nom_fichier = "dico.txt"
lex = lexique.Lexique(nom_fichier)

#Création de la partie avec tirage d'un mot
partie = jeu.Jeu(lex.choisir())
nbcoups = 9 #Nombre d'erreurs autorisées avant d'être pendu
#On affiche une première fois le mot
partie.afficher()
lettre = "1"
#Cette boucle continue tant qu'il reste des erreurs autorisées
#ou que le mot n'a pas été trouvé
while partie.coup_joue() < nbcoups and not partie.est_complet():
    lettre = input('Entrez une lettre: ')
    #Cette boucle sert a vérifier que l'utilisateur n'a pas entré autre chose qu'une lettre
    while not lettre.isalpha() or len(lettre) != 1:
        lettre = input('Caractère non reconnu. Entrez une lettre: ')
    #On met a jour le nombre d'erreurs
    partie.jouer(lettre.upper())
    #On affiche le mot
    partie.afficher()
    print(f"Nombre d'erreurs : {partie.coup_joue()}. Déjà testé: {partie.joue}")

if partie.est_complet():
    print(f"Bravo ! Le mot était {partie.mot}")
else:
    print(f"Perdu... Le mot était {partie.mot}")

