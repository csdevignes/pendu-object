'''
Activité n°7
Jeu du pendu en objet - Objet jeu
Cet objet gère la partie de pendu pour un mot donné en argument.
Il contient le mot à deviner et la liste des lettres proposées (joue)
ainsi que les méthodes utilisées pour jouer.

@Usage:
python pendu.py [-l <lexique.txt>]

@author: Claire-Sophie Devignes
@copyright: Institut des sciences du Digital, Management & Cognition – IDMC
@license: MIT License
@version: 1.0
@email: claire-sophie.devignes9@etu.univ-lorraine.fr
@date: 31 janv 24
'''
import lexique

class Jeu:
    def __init__(self, mot="PYTHON"): #Le mot par défaut est PYTHON
        self.joue = set()
        self.mot = mot

    def afficher(self):
        '''
        Affiche le mot a deviner avec les lettres trouvées et des _ pour les lettres non trouvées
        '''
        for car in self.mot:
            if car in self.joue:
                print(car, end='') #On spécifie end='' pour éviter les retours à la ligne entre chaque print()
            else:
                print('_', end='')
        print('\n')
    def jouer(self, car):
        '''
        Compare la lettre proposée avec le mot, et stocke la lettre proposée dans joue
        :param car: str de taille 1, contient la lettre proposée
        :return: boolean: True si la lettre est dans le mot, False si elle n'y est pas
        '''
        if car in self.mot:
            trouve = True
            print("Vrai")
        else:
            trouve = False
            print("Faux")
        self.joue.add(car)
        return trouve
    def coup_joue(self):
        '''
        Compte le nombre d'erreurs en comparant les lettres proposées avec les lettres du mot
        :return: entier
        '''
        erreurs = 0
        for lettre in self.joue:
            if lettre not in self.mot:
                erreurs += 1
        return erreurs

    def est_complet(self):
        '''
        Vérifier si tous les caractères ont été joués, pour savoir si la partie est finie.
        :return: boolean
        '''
        for car in self.mot:
            if not car in self.joue:
                return False
        return True


#Test
if __name__ == "__main__":
    l1 = lexique.Lexique("dico.txt")
    partie = Jeu()
    print(partie.joue)
    print(partie.mot)
    partie.afficher()
    partie.jouer('Y')
    print(partie.joue)
    partie.afficher()
    print(partie.coup_joue())
