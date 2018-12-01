import pygame
#Pour la génération de points aléatoires
from random import *

white = (255,255,255)
blue = (0, 100, 175)

# Classe qui décrit un mur a laide de pygame.draw.lines
class Wall:
    # Constructeur de la classe
    # window : ecran de jeu
    # liste_sols : les sols en tant que rectangles
    # liste_points : les points dans une liste
    # liste_atterissage : les deuxiemes points des pistes d'atterissages
    #
    def __init__(self, window):
        self.window = window
        self.liste_sols = []
        self.liste_points = []
        self.liste_atterissage = []
        self.largeur_atterissage = 90
        self.nb_plateforme = 0

    # Mehode generant aléatoirement les points a lier a partir des caractérisriques de window que l'on donne au
    # constructeur
    # Il faut aussi generer des points d'atterissages pour la fusée
    # pas : espace entre les points
    # RETOURNE : une liste de points
    def genere_points(self, pas):
        # caracteristiques de l'écran
        hauteur = self.window.get_height()
        largeur = self.window.get_width()

        while  self.nb_plateforme < 2 :

            # Boucle generant les points
            largeur_restante = 0 # largeur a incrementer au fur et a mesure de l'avancement du terrain
            self.liste_points = [[0, randint(hauteur/2, hauteur)]] # commencement de la
            self.liste_atterissage = []
            self.nb_plateforme = 0
            
            while largeur_restante<largeur :
                # Generation terrain "normal"
                largeur_restante = largeur_restante + randint(20,40)# pas
                hauteur_mur = randint(hauteur/2, hauteur)
                self.liste_points.append([largeur_restante,hauteur_mur])
<<<<<<< HEAD

                # Generation terrain plat
                proba_terrain_plat = randint(0,100)
                if proba_terrain_plat < 2 and self.nb_plateforme < 3:
                    largeur_restante=largeur_restante+self.largeur_atterissage
                    self.liste_points.append([largeur_restante,hauteur_mur])
                    self.liste_atterissage.append([largeur_restante,hauteur_mur])
                    self.nb_plateforme = self.nb_plateforme+1

=======
                self.liste_atterissage.append([largeur_restante,hauteur_mur])
                self.nb_plateforme = self.nb_plateforme+1
>>>>>>> da0b11d380dcee8435135c06c1fea717dcdd293e
        # Retour de la liste
        return self.liste_points


    # Methode permettant de generer les murs avec les points donnés par la méthode générant aléatoirement les points
    # liste_points : liste de points a lier
    def draw_wall(self, liste_points):
        for i in range(0, len(liste_points) - 1):
            self.liste_sols.append(pygame.draw.line(self.window, white, (liste_points[i][0], liste_points[i][1]), (liste_points[i+1][0], liste_points[i+1][1]),1))

        for j in range(0, len(self.liste_atterissage)) :
            pygame.draw.line(self.window, blue, (self.liste_atterissage[j][0]-self.largeur_atterissage, self.liste_atterissage[j][1]), (self.liste_atterissage[j][0], self.liste_atterissage[j][1]), 3)

    # Methode permettant d'avoir la liste des points
    def donne_points(self):
        return self.liste_points
