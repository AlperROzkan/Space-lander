import pygame

white = (255,255,255)


# Classe qui décrit un mur a laide de pygame.draw.lines
class Wall:
    # Constructeur de la classe
    # window : ecran de jeu
    def __init__(self, window):
        self.window = window

    # Mehode generant aléatoirement les points a lier a partir de window que l'on donne au constructeur
    # Il faut aussi generer des points d'atterissages pour la fusée
    # listePoints : la liste de points a lier
    # largeur : largeur des lignes
    # pasX : distance entre les points
    # RETOURNE : une liste de points

    def draw_wall(self):
        pygame.draw.lines(self.window, white, False, ((10, 10), (20, 20), (30, 30), (100, 200)), 10)
        pygame.display.update()


