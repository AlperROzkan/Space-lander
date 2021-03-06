import pygame
import time
from Wall import *
from Fusee import *
from pygame.math import *
from Hud import *
# Initialise
pygame.init()
# Taille fenetre
windowW = 1000
windowH = 500
# Couleurs
black = (255,255,255)
# Configurations de la fenetre
window = pygame.display.set_mode((windowW, windowH))
# Nom de la fenetre
pygame.display.set_caption("Space Lander")


# Musique
music1 = pygame.mixer_music.load("brodyquest1.ogg")

# Verifie si il y a un game over
# murs : Classe Wall : les murs de la partie
# fusee : Classe Fusee : la fusee
# tolerance : ecart accorde a la fusee
def is_over(murs, fusee, tolerance):
    touche_bord = False
    touche_mur = False
    # Sortie de la fenetre
    if fusee.donne_point_origine()[0] < -10 or fusee.donne_point_origine()[0]+fusee.donne_largeur() > windowW+10 or fusee.donne_point_origine()[1] < -10 or fusee.donne_point_origine()[1]+fusee.donne_hauteur() > windowH+10:
        touche_mur = True;
    # Collisions avec les murs
    # On calcule les vecteurs de chacun des sols et on regarde si ils sont du même coté que la fusee
    # On separe tous les points de la fusee pour une meilleure lisibilite, tourne autour d'un carre, premier lettre du numero
    liste_points = murs.donne_points()
    U = [fusee.donne_point_origine()[0]+tolerance,fusee.donne_point_origine()[1]+tolerance]
    D =  [fusee.donne_point_origine()[0]+fusee.donne_largeur()-tolerance, fusee.donne_point_origine()[1]+tolerance]
    T = [fusee.donne_point_origine()[0]+fusee.donne_largeur()-tolerance, fusee.donne_point_origine()[1]+fusee.donne_hauteur()-tolerance]
    Q = [fusee.donne_point_origine()[0]+tolerance, fusee.donne_point_origine()[1]+fusee.donne_hauteur()-tolerance]
    # Boucle de verification de chaque point generé
    for i in range(0,len(liste_points)-1) :
        # Deux points du sol se suivant
        A = [liste_points[i][0], liste_points[i][1]]
        B = [liste_points[i+1][0], liste_points[i+1][1]]

        # Verification du point un
        if((B[0] - A[0]) * (U[1] - A[1]) - (B[1] - A[1]) * (U[0] - A[0]) > 0 and U[0] >= A[0] and U[0] < B[0]) :
            touche_mur = True
        # Verification du point deux
        if((B[0] - A[0]) * (D[1] - A[1]) - (B[1] - A[1]) * (D[0] - A[0]) > 0 and D[0] >= A[0] and D[0] < B[0]) :
            touche_mur = True
        # Verification du point trois
        if ((B[0] - A[0]) * (T[1] - A[1]) - (B[1] - A[1]) * (T[0] - A[0]) > 0 and T[0] >= A[0] and T[0] < B[0]):
            # Conditions en plus pour permettre a la fusée de gagner
            if(fusee.donne_angle()==90 and A[1]==B[1] and T[1]==A[1] and T[1]==B[1] and T[0]>=A[0] and T[0]+10==B[0]\
                    and Q[1]==A[1] and Q[1] == B[1] and Q[0]-10>=A[0] and Q[0]<=B[0]):
                touche_mur=False
            else :
                touche_mur = True
        # Verification du point quatre
        if ((B[0] - A[0]) * (Q[1] - A[1]) - (B[1] - A[1]) * (Q[0] - A[0]) > 0 and Q[0] >= A[0] and Q[0] < B[0]):
            # Conditions en plus pour permettre a la fusée de gagner
            if (fusee.donne_angle() == 90 and A[1]==B[1] and Q[1]==A[1] and Q[1] == B[1] and Q[0]-10>=A[0] and Q[0]<=B[0] \
                    and T[1] == A[1] and T[1] == B[1] and T[0] >= A[0] and T[0] + 10 == B[0]):
                touche_mur = False
            else:
                touche_mur = True

        # Verification entre les intervalles
        if(A[1]<Q[1] and A[1]>U[1]) :
            if(A[0]<T[0] and A[0]>Q[0]):
                touche_mur = True
    return touche_bord or touche_mur

# Dit si jeu est gagne
# sols : sols du jeu
# fusee : fusee
# RETOURNE : true si gagne
def gagne(murs, fusee, tolerance) :
    T = [fusee.donne_point_origine()[0] + fusee.donne_largeur() - tolerance,
         fusee.donne_point_origine()[1] + fusee.donne_hauteur() - tolerance]
    Q = [fusee.donne_point_origine()[0] + tolerance, fusee.donne_point_origine()[1] + fusee.donne_hauteur() - tolerance]
    # Boucle de verification de chaque point generé
    liste_points = murs.liste_points
    for i in range(0, len(liste_points) - 1):
        # Deux points du sol se suivant
        A = [liste_points[i][0], liste_points[i][1]]
        B = [liste_points[i + 1][0], liste_points[i + 1][1]]
        if (fusee.getAngle() == 90 or fusee.getAngle() == -270) and A[1]==B[1] and T[1]==Q[1] \
            and A[1]<=T[1] and T[0]>=A[0] and T[0]<=B[0]\
                and A[1]<=Q[1] and Q[0]>=A[0] and Q[0]<=B[0]:
            return True

# Fonction definissant le jeu
def gameLoop():
    # Musique
    pygame.mixer_music.play(-1,0)
    # Horloge
    clock = pygame.time.Clock()
    font = pygame.font.Font('spacelander.ttf',30)
    hud = HUD((255,255,255), 10,10,window,font)
    game_over = False
    score = 0
    time = 300
    fuel = 1000
    end = False
    auto = False

    win = False # Booleene indiquant si on a gagné
    fusee = Fusee((100, 100), "fusee.png", (60, 40))
    murs = Wall(window)
    all_sprites = pygame.sprite.Group(fusee)
    counter = 0 # acceleration/vitesse
    lastcounter = 0 #acceleration sauvegarder pour l'"inertie"
    gravityacce = 0.5 #acceleration de la gravité
    lastangle = fusee.getAngle() #garde l'angle de la fusee
    released = False #booleen pour tester si la touche est relchee
    speedcalculrefresher = 0 #compteur
    lastX = fusee.getX()
    lastY = fusee.getY()
    altitude = 0
    vertical_speed = 0
    horizontal_speed = 0
    # Generation des murs
    liste_points = murs.genere_points([20,40])

    # Boucle principale
    while not game_over:

        # Gestion des evenements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT] and not win and not end:
            fusee.rotate(-10)
        if keys[pygame.K_q] or keys[pygame.K_LEFT] and not win and not end:
            fusee.rotate(10)
        if keys[pygame.K_z] or keys[pygame.K_UP] and not win and fuel > 0 and not end:
            if (gravityacce > 0.5): #la gravite ne peut pas etre inferieur à o,5
                gravityacce -= 0.06 #la gravite de 0.06 par tick (~30 ticks par seconde)
            if (counter < 2):#la vitesse ne peut pas être > 2
                counter+=0.033 #+1 par seconde pcque 30 fps
            fusee.avancer(counter) #methode qui modifie la position de la fusee
            released = True #on dit que la touche peut etre relachee
            fuel -= 0.33 #-10 fuel par sec
        elif event.type == pygame.KEYUP and released and not win and not end: #si la touche est relachee et quelle peut etre relachee
            lastangle = fusee.getAngle() #l'angle est sauvegarde pour l'inertie
            if (lastcounter <= counter): #si la derniere vitesse d'"inertie" est < a la vitesse actuelle (oui on peut augmanter sa vitesse en changeant d'angle et en double pressant la touche pour avancer dans certains cas :/)
                lastcounter = counter #la vitesse actuelle est sauvegarder
            counter = 0 #la vitesse est remise à 0
            released = False #la touche n'est plus dans une position où elle peut etre relachee
        if keys[pygame.K_SPACE] and win:
            score += 100
            win = False # Booleene indiquant si on a gagné
            fusee = Fusee((100, 100), "fusee.png", (60, 40))
            murs = Wall(window)
            all_sprites = pygame.sprite.Group(fusee)
            counter = 0 # acceleration/vitesse
            lastcounter = 0 #acceleration sauvegarder pour l'"inertie"
            gravityacce = 0.5 #acceleration de la gravité
            lastangle = fusee.getAngle() #garde l'angle de la fusee
            released = False #booleen pour tester si la touche est relchee
            speedcalculrefresher = 0 #compteur
            lastX = fusee.getX()
            lastY = fusee.getY()
            altitude = 0
            vertical_speed = 0
            horizontal_speed = 0
            # Generation des murs
            liste_points = murs.genere_points([20, 40])
        if keys[pygame.K_r] and end:
            fusee = Fusee((100, 100), "fusee.png", (60, 40))
            murs = Wall(window)
            all_sprites = pygame.sprite.Group(fusee)
            counter = 0 # acceleration/vitesse
            lastcounter = 0 #acceleration sauvegarder pour l'"inertie"
            gravityacce = 0.5 #acceleration de la gravité
            lastangle = fusee.getAngle() #garde l'angle de la fusee
            released = False #booleen pour tester si la touche est relchee
            speedcalculrefresher = 0 #compteur
            lastX = fusee.getX()
            lastY = fusee.getY()
            altitude = 0
            vertical_speed = 0
            horizontal_speed = 0
            # Generation des murs
            liste_points = murs.genere_points([20, 40])
            fuel = 1000
            time = 300
            score = 0
            end = False
        if keys[pygame.K_p] and auto:
                auto = False
        if keys[pygame.K_o] and not auto:
                auto = True


        ###########################################################################
            #Auto play
        ##########################################################################
        if fuel > 0 and not end and not win:
            if(auto):
                if (fusee.getX() < (murs.liste_atterissage[0][0]-murs.largeur_atterissage/2)-10) or (fusee.getX() > (murs.liste_atterissage[0][0]-murs.largeur_atterissage/2)+10):
                    if (altitude < windowH/2+100):
                        if (fusee.getAngle() > 90):
                            fusee.rotate(-10)
                        if (fusee.getAngle() < 90):
                            fusee.rotate(10)
                        if (vertical_speed < 10):
                            if (gravityacce > 0.5): #la gravite ne peut pas etre inferieur à o,5
                                gravityacce -= 0.06 #la gravite de 0.06 par tick (~30 ticks par seconde)
                            if (counter < 2):#la vitesse ne peut pas être > 2
                                counter+=0.033 #+1 par seconde pcque 30 fps
                            fusee.avancer(counter) #methode qui modifie la position de la fusee
                            fuel -= 0.33 #-10 fuel par sec

                    elif (fusee.getX() > (murs.liste_atterissage[0][0]-murs.largeur_atterissage/2)):
                        if (fusee.getAngle() < 180):
                            fusee.rotate(10)
                        else:
                            if (gravityacce > 0.5): #la gravite ne peut pas etre inferieur à o,5
                                gravityacce -= 0.06 #la gravite de 0.06 par tick (~30 ticks par seconde)
                            if (counter < 2):#la vitesse ne peut pas être > 2
                                counter+=0.033 #+1 par seconde pcque 30 fps
                            fusee.avancer(counter) #methode qui modifie la position de la fusee
                            fuel -= 0.33 #-10 fuel par sec

                    else:
                        if (fusee.getAngle() > 0):

                            fusee.rotate(-10)
                        else:
                            if (gravityacce > 0.5): #la gravite ne peut pas etre inferieur à o,5
                                gravityacce -= 0.06 #la gravite de 0.06 par tick (~30 ticks par seconde)
                            if (counter < 2):#la vitesse ne peut pas être > 2
                                counter+=0.033 #+1 par seconde pcque 30 fps
                            fusee.avancer(counter) #methode qui modifie la position de la fusee
                            fuel -= 0.33 #-10 fuel par sec


                else:
                    if (fusee.getAngle() > 90):
                        fusee.rotate(-10)
                    if (fusee.getAngle() < 90):
                        fusee.rotate(10)
                    if vertical_speed < -16 and (murs.liste_atterissage[0][1] - fusee.getY()) < vertical_speed*-5:
                        if (gravityacce > 0.5): #la gravite ne peut pas etre inferieur à o,5
                            gravityacce -= 0.06 #la gravite de 0.06 par tick (~30 ticks par seconde)
                        if (counter < 2):#la vitesse ne peut pas être > 2
                            counter+=0.033 #+1 par seconde pcque 30 fps
                        fusee.avancer(counter) #methode qui modifie la position de la fusee
                        fuel -= 0.33 #-10 fuel par sec

        ##########################################################################

        speedcalculrefresher += 0.066
        if speedcalculrefresher >= 1: #Toute les 0.5 seconde on verifie la position actuelle par rapport à celle d'il y a 0.5 sec pour trouver une vitesse verticale et horizontale
            horizontal_speed = abs(lastX-fusee.getX())
            lastX = fusee.getX()
            vertical_speed = lastY-fusee.getY()
            lastY = fusee.getY()
            speedcalculrefresher = 0

        # Gestion de l'altitude
        altitude = windowH - fusee.getY() #pour le moment par rapport au bas de la fenetre

        # Affichage HUD
        hud.setHudScore("Score : "+str(score))
        hud.setHudTime("Time : "+str(int(time)))
        hud.setHudFuel("Fuel : "+ str(int(fuel)))
        hud.setHudAltitude("Altitude : "+str(int(altitude)))
        hud.setHudVertical_speed("Vertical_speed : "+str(int(vertical_speed)))
        hud.setHudHorizontal_speed("Horizontal_speed : "+str(int(horizontal_speed)))


        if (lastcounter > 0): #si la vitesse d'"inertie" est superieur a 0
            lastcounter -= 0.015 #on la diminue
            fusee.avancerbis(lastangle, lastcounter) #on actualise la position de la fusee selon l'inertie
        if  not win and not end:
            gravityacce += 0.02 #on augmente l'acceleration due a la gravite de 0.02 par tick
            time -= 0.033 #-1 par seconde pcque 30 fps

        # Gestion de la victoire
        if (gagne(murs, fusee, 0) and vertical_speed >= -20) and not win and not end:
            fusee.gravity(0)
            gravityacce = 0
            fusee.avancer(0)
            fusee.avancerbis(lastangle, 0)
            print("Gagne")
            win = True

        # Gestion de la fin du jeu
        if (gagne(murs, fusee, 0) and vertical_speed < -20) or time <= 0 or is_over(murs, fusee,17) and not end:
            fusee.gravity(0)
            gravityacce = 0
            fusee.avancer(0)
            fusee.avancerbis(lastangle, 0)
            print("Game Over")
            end = True
            #game_over = True

        window.fill((0, 0, 0))

        # A enlever si l'on ne veut pas du rectangle entourant la fusée
        # pygame.draw.rect(window, white, fusee, 5)

        fusee.gravity(gravityacce)
        hud.hudDraw()
        murs.draw_wall(liste_points)
        if win:
            hud.DrawNextlvl(windowW/2, windowH/2)
        if end:
            hud.DrawRestart(windowW/2, windowH/2, str(int(score)))
        all_sprites.draw(window)

        pygame.display.flip()
        clock.tick(30)
        pygame.display.update()

gameLoop()
pygame.mixer_music.stop()
pygame.quit()
quit()
