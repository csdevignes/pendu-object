'''
Activité n°7
Jeu du pendu en objet - Objet Lexique
Cet objet crée le lexique de mots à partir d'un fichier.
Il permet ensuite de choisir aleatoirement un mot

@Usage:
python pendu.py [-l <lexique.txt>]

@author: Claire-Sophie Devignes
@copyright: Institut des sciences du Digital, Management & Cognition – IDMC
@license: MIT License
@version: 1.0
@email: claire-sophie.devignes9@etu.univ-lorraine.fr
@date: 31 janv 24
'''
import logging
import random


class Lexique:
    def __init__(self, nom_fichier=None):
        '''
        Constructeur qui crée le lexique à partir d'un fichier.
        Les mots sont stockés dans une liste.
        :param nom_fichier: str nom du fichier txt contenant les mots
        Par défaut None: si on ne donne pas de nom de fichier, utilise une liste de test
        '''

        if nom_fichier == None:
            #Charge la liste de test
            self.contenu = ['Elephant', 'Gateau', 'Python', 'Algorithme', 'Parapluie']
            return  #Veut dire qu'on s'arrete et qu'on sort du constructeur
        try:
            self.contenu = []
            with open(nom_fichier, "r", encoding='UTF-8') as f:
                for ligne in f:
                    ligne = ligne.strip().upper()
                    self.contenu.append(ligne)
        except:
            logging.warning(f'Erreur de fichier {nom_fichier}.\n Chargement des valeurs par défaut.')
            #Charge la liste de test
            self.contenu = ['Elephant', 'Gateau', 'Python', 'Algorithme', 'Parapluie']
    def _print(self):
        '''
        Méthode privée pour afficher le contenu: sert à tester
        '''
        print(self.contenu)
    def choisir(self):
        '''
        Choisir au hasard un mot
        :return: str
        '''
        choixmot = random.randint(0, len(self.contenu) - 1)
        return self.contenu[choixmot]

#Test
if __name__ == "__main__":
    l1 = Lexique("dico.txt")
    l1._print()
    for i in range(10):
        print(l1.choisir())