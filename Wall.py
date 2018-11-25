import pygame
#Pour la génération de points aléatoires
from random import randint

white = (255,255,255)


# Classe qui décrit un mur a laide de pygame.draw.lines
class Wall:
    # Constructeur de la classe
    # window : ecran de jeu
    def __init__(self, window):
        self.window = window

    # Mehode generant aléatoirement les points a lier a partir des caractérisriques de window que l'on donne au
    # constructeur
    # Il faut aussi generer des points d'atterissages pour la fusée
    # pas : espace entre les points
    # RETOURNE : une liste de points
    def genere_points(self, pas):
        # caracteristiques de l'écran
        hauteur = self.window.get_height()
        largeur = self.window.get_width()

        # Boucle generant les points
        i = 0
        liste_points = [(0, randint(hauteur/2, hauteur))]
        while i<largeur :
            i = i + pas
            liste_points.append((i,randint(hauteur/2, hauteur)))
        return liste_points


    # Methode permettant de generer les murs avec les points donnés par la méthode générant aléatoirement les points
    # liste_points : liste de points a lier
    def draw_wall(self, liste_points):
        pygame.draw.lines(self.window, white, False, liste_points, 1)
        pygame.display.update()


