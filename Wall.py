import pygame
#Pour la génération de points aléatoires
from random import *

white = (255,255,255)


# Classe qui décrit un mur a laide de pygame.draw.lines
class Wall:
    # Constructeur de la classe
    # window : ecran de jeu
    def __init__(self, window):
        self.window = window
        self.liste_sols = []
        self.liste_points = 0

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
        largeur_restante = 0 # largeur a incrementer au fur et a mesure de l'avancement du terrain
        self.liste_points = [[0, randint(hauteur/2, hauteur)]] # commencement de la
        while largeur_restante<largeur :
            # Generation terrain "normal"
            largeur_restante = largeur_restante + randint(20,40)# pas
            hauteur_mur = randint(hauteur/2, hauteur)
            self.liste_points.append([largeur_restante,hauteur_mur])

            # Generation terrain plat
            proba_terrain_plat = randint(0,100)
            if proba_terrain_plat < 10 :
                largeur_restante=largeur_restante+90
                self.liste_points.append([largeur_restante,hauteur_mur])
        # Retour de la liste
        return self.liste_points


    # Methode permettant de generer les murs avec les points donnés par la méthode générant aléatoirement les points
    # liste_points : liste de points a lier
    def draw_wall(self, liste_points):
        for i in range(0, len(liste_points) - 1):
            self.liste_sols.append(pygame.draw.line(self.window, white, (liste_points[i][0], liste_points[i][1]), (liste_points[i+1][0], liste_points[i+1][1]),1))
            #pygame.draw.rect(self.window, (255,0,0), self.liste_sols[i], 1)

    # Methode permettant d'avoir la liste des points
    def donne_points(self):
        return self.liste_points



