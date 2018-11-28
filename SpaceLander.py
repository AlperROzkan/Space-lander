import pygame
import time
from Wall import *
from Fusee import *
from pygame.math import *

# Initialise
pygame.init()

# Taille fenetre
windowW = 1000
windowH = 500

# Couleurs
black = (255,255,255)

# Nom de la fenetre
pygame.display.set_caption("Space Lander")

# Chargement image
imgBalloon = pygame.image.load("Balloon.png")

# Verifie si le jeu est termine
# murs : Classe Wall : les murs de la partie
# fusee : Classe Fusee : la fusee
def is_over(murs, fusee):
    touche_bord = False
    touche_mur = False

    # Sortie de la fenetre
    if fusee.donne_point_origine()[0] < -10 or fusee.donne_point_origine()[0]+fusee.donne_largeur() > windowW+10 or fusee.donne_point_origine()[1] < -10 or fusee.donne_point_origine()[1]+fusee.donne_hauteur() > windowH+10:
        touche_mur = True;

    # Collisions avec les murs
    # On calcule les vecteurs de chacun des sols et on regarde si ils sont du même coté que la fusee
    # On separe tous les points de la fusee pour une meilleure lisibilite, tourne autour d'un carre, premier lettre du numero
    liste_points = murs.donne_points()
    U = [fusee.donne_point_origine()[0],fusee.donne_point_origine()[1]]
    D =  [fusee.donne_point_origine()[0]+fusee.donne_largeur(), fusee.donne_point_origine()[1]]
    T = [fusee.donne_point_origine()[0]+fusee.donne_largeur(), fusee.donne_point_origine()[1]+fusee.donne_hauteur()]
    Q = [fusee.donne_point_origine()[0], fusee.donne_point_origine()[1]+fusee.donne_hauteur()]

    # Boucle de verification de chaque point generé
    for i in range(0,len(liste_points)-1) :
        # Deux points du sol se suivant
        A = [liste_points[i][0], liste_points[i][1]]
        B = [liste_points[i+1][0], liste_points[i+1][1]]
        # On calcule les vecteurs de chaque points du sol et du point de la fusee
        AB = [B[0]-A[0], B[1]-A[1]]
        AU = [U[0]-A[0], U[1]-A[1]]
        AD = [D[0]-A[0], D[1]-A[1]]
        AT = [T[0]-A[0], T[1]-A[1]]
        AQ = [Q[0]-A[0], Q[1]-A[1]]

        # Verification
        if ((AB[0]*AU[1] - AB[1]*AU[0]) * (AB[0]*AD[1] - AB[1]*AD[0]))<0 :
            #print(AB)
            #print(AU)
            #print(AD)
            #print(AT)
            #print(AQ)
            #print((AB[0]*AU[1] - AB[1]*AU[0]) * (AB[0]*AD[1] - AB[1]*AD[0]))
            touche_mur = True


    return False #or touche_bord or touche_mur


# Fonction definissant le jeu
def gameLoop():
    # Configurations de la fenetre
    window = pygame.display.set_mode((windowW, windowH))
    # Horloge
    clock = pygame.time.Clock()

    fusee = Fusee((100, 100), "fusee.png", (60, 40))
    murs = Wall(window)
    all_sprites = pygame.sprite.Group(fusee)
    game_over = False

    # Generation des murs
    liste_points = murs.genere_points(5)

    # Boucle principale
    while not game_over:
        # Gestion des evenements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            fusee.rotate(-10)
        if keys[pygame.K_q] or keys[pygame.K_LEFT]:
            fusee.rotate(10)
        if keys[pygame.K_z] or keys[pygame.K_UP]:
            fusee.avancer(10)

        # Gestion de la fin du jeu
        if is_over(murs, fusee) == True:
            print("Fin du jeu")
            print(fusee.donne_point_origine())
            game_over = True

        window.fill((0, 0, 0))
        all_sprites.draw(window)
        murs.draw_wall(liste_points)
        pygame.display.flip()
        clock.tick(30)
        pygame.display.update()

gameLoop()
pygame.quit()
quit()
