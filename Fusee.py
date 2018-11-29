import pygame
from pygame.math import Vector2
from math import *


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

        # TODO A enlever
        print(self.donne_point_origine())
        print(self.donne_largeur())
        print(self.donne_hauteur())

    def rotate(self, angle):
        self.angle += angle
        self.image = pygame.transform.rotate(self.orig_image, self.angle)
        self.rect = self.image.get_rect(center=self.pos)

    def avancer(self, speed):
        angle = radians(-self.angle)
        self.pos.x += speed*cos(angle)
        self.pos.y += speed*sin(angle)
        self.rect = self.image.get_rect(center=self.pos)

    def gravity(self, gravity):
        self.pos.y += gravity
        self.rect = self.image.get_rect(center=self.pos)

    # Donne le point en haut a gauche
    # EXEMPLE : fusee.donne_point_origine()[0] pour x, fusee.donne_point_origine()[1] pour y
    def donne_point_origine(self):
        return [self.rect.left, self.rect.top]

    # Donne la largeur de la fusee
    def donne_largeur(self):
        return self.rect.width

    def donne_hauteur(self):
        return self.rect.height
