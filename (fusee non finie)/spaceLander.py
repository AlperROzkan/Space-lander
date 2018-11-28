import pygame
from pygame.math import Vector2
from math import *

# Initialise
pygame.init()

# Variables
# Taille fenetre
windowW = 1600
windowH = 800

class Fusee(pygame.sprite.Sprite):
    def __init__(self, pos, img, size):
        super().__init__()
        self.img = pygame.image.load(img)
        self.image = pygame.transform.scale(self.img, size)
        # reference vers l'image originale pour eviter deformation
        self.orig_image = self.image
        self.rect = self.image.get_rect(center=pos)
        self.pos = Vector2(pos)  # coordonne du point centre de la rotation (correspond ici au centre de l'image)
        self.angle = 0

    def rotate(self, angle):
        self.angle += angle
        self.image = pygame.transform.rotate(self.orig_image, self.angle)
        self.rect = self.image.get_rect(center=self.pos)

    def avancer(self, speed):
        angle = radians(-self.angle)
        self.pos.x += speed*cos(angle)
        self.pos.y += speed*sin(angle)
        self.rect = self.image.get_rect(center=self.pos)

def gameLoop():
    window = pygame.display.set_mode((windowW, windowH))
    clock = pygame.time.Clock()
    fusee = Fusee((100, 100), "fusee.png", (60,40))
    all_sprites = pygame.sprite.Group(fusee)
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            fusee.rotate(-3)
        if keys[pygame.K_q] or keys[pygame.K_LEFT]:
            fusee.rotate(3)
        if keys[pygame.K_z] or keys[pygame.K_UP]:
            fusee.avancer(3)

        window.fill((0,0,0))
        all_sprites.draw(window)
        pygame.display.flip()
        clock.tick(30)




gameLoop()
pygame.quit()
