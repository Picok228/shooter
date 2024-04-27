import random

import pygame

class UFO:
    def __init__(self,x,y,w,h,img,speed):
        self.photo = pygame.transform.scale(pygame.image.load(img), (w,h))
        self.hitbox = self.photo.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed


    def draw(self,window):
        #pygame.draw.rect(window,(225,0,0),self.hitbox)
        window.blit(self.photo,(self.hitbox.x, self.hitbox.y))



