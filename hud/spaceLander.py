import pygame
import math

# Initialise
pygame.init()


# Variables
# Taille fenetre
windowW = 1600
windowH = 800



class HUD:
    def __init__(self, color, x, y, window, font):

        self.hudScore = font.render("",True,color)
        self.hudTime = font.render("",True,color)
        self.hudFuel = font.render("",True,color)
        self.hudAltitude = font.render("",True,color)
        self.hudHorizontal_speed = font.render("",True,color)
        self.hudVertical_speed = font.render("",True,color)

        self.x = x
        self.y = y
        self.window = window
        self.font = font
        self.color = color

        self.lastScore = ""
        self.lastTime = ""
        self.lastFuel = ""
        self.lastAltitude = ""
        self.lastHorizontal_speed = ""
        self.lastVertical_speed = ""

        self.newScore = "1"
        self.newTime = "2"
        self.newFuel = "3"
        self.newAltitude = "4"
        self.newHorizontal_speed = "5"
        self.newVertical_speed = "6"

        self.displayRectScore = self.hudScore.get_rect()
        self.displayRectTime = self.hudTime.get_rect()
        self.displayRectFuel = self.hudFuel.get_rect()
        self.displayRectAltitude = self.hudAltitude.get_rect()
        self.displayRectHorizontal_speed = self.hudHorizontal_speed.get_rect()
        self.displayRectVertical_speed = self.hudVertical_speed.get_rect()



    def setHudScore(self, text):
        self.newScore = text

    def setHudTime(self, text):
        self.newTime = text

    def setHudFuel(self, text):
        self.newFuel = text

    def setHudAltitude(self, text):
        self.newAltitude = text

    def setHudHorizontal_speed(self, text):
        self.newHorizontal_speed = text

    def setHudVertical_speed(self, text):
        self.newVertical_speed = text


    def hudDraw(self):
        if self.lastScore != self.newScore:
            self.hudScore = self.font.render(self.newScore,True,self.color)
            self.displayRectScore = self.hudScore.get_rect()
            self.displayRectScore = (self.x+40,self.y+40)
            self.lastScore = self.newScore
        window.blit(self.hudScore, self.displayRectScore)

        if self.lastTime != self.newTime:
            self.hudTime = self.font.render(self.newTime,True,self.color)
            self.displayRectTime = self.hudTime.get_rect()
            self.displayRectTime = (self.x+40,self.y+80)
            self.lastTime = self.newTime
        window.blit(self.hudTime, self.displayRectTime)

        if self.lastFuel != self.newFuel:
            self.hudFuel = self.font.render(self.newFuel,True,self.color)
            self.displayRectFuel = self.hudFuel.get_rect()
            self.displayRectFuel = (self.x+40,self.y+120)
            self.lastFuel = self.newFuel
        window.blit(self.hudFuel, self.displayRectFuel)

        if self.lastAltitude != self.newAltitude:
            self.hudAltitude = self.font.render(self.newAltitude,True,self.color)
            self.displayRectAltitude = self.hudAltitude.get_rect()
            self.displayRectAltitude = (self.x+1040,self.y+40)
            self.lastAltitude = self.newAltitude
        window.blit(self.hudAltitude, self.displayRectAltitude)

        if self.lastHorizontal_speed != self.newHorizontal_speed:
            self.hudHorizontal_speed = self.font.render(self.newHorizontal_speed,True,self.color)
            self.displayRectHorizontal_speed = self.hudHorizontal_speed.get_rect()
            self.displayRectHorizontal_speed = (self.x+1040,self.y+80)
            self.lastHorizontal_speed = self.newHorizontal_speed
        window.blit(self.hudHorizontal_speed, self.displayRectHorizontal_speed)

        if self.lastVertical_speed != self.newVertical_speed:
            self.hudVertical_speed = self.font.render(self.newVertical_speed,True,self.color)
            self.displayRectVertical_speed = self.hudVertical_speed.get_rect()
            self.displayRectVertical_speed = (self.x+1040,self.y+120)
            self.lastVertical_speed = self.newVertical_speed
        window.blit(self.hudVertical_speed, self.displayRectVertical_speed)


# Configurations de la fenetre
window = pygame.display.set_mode((windowW,windowH))
pygame.display.set_caption("Space Lander")


font = pygame.font.Font('spacelander.ttf',30)

hud = HUD((255,255,255), 50,50,window,font)

# Fonction definissant le jeu
def gameLoop():
    # Initialisation variables de jeu
    game_over = False

    # Boucle principale
    while not game_over:
        # Gestion des evenements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP :
                hud.setHudScore("Score")
                hud.setHudTime("Time")
                hud.setHudFuel("Fuel")
                hud.setHudAltitude("Altitude")
                hud.setHudVertical_speed("Vertical_speed")
                hud.setHudHorizontal_speed("Horizontal_speed")


            window.fill((0,0,0))
            hud.hudDraw()


            pygame.display.update()



gameLoop()
pygame.quit()
quit()
