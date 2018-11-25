import pygame
from Wall import *

# Initialise
pygame.init()


# Variables
# Taille fenetre
windowW = 800
windowH = 500

# Couleurs
black = (255,255,255)

# Configurations de la fenetre
window = pygame.display.set_mode((windowW, windowH))
pygame.display.set_caption("Space Lander")


# Fonction definissant le jeu
def gameLoop():
    # Variables de jeu
    game_over = False
    murs = Wall(window)

    # Generation des murs
    liste_points = murs.genere_points(10)
    murs.draw_wall(liste_points)

    # Boucle principale
    while not game_over:
        # Gestion des evenements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True




gameLoop()
pygame.quit()
quit()
