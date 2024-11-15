import pygame
import math
import random
SCREEN=612,382
COL=255,0,0
player_x_pos = 350
player_y_pos = 300
pygame.init()
screen =pygame.display.set_mode(SCREEN)
bg =pygame.image.load("space.png")
screen.blit(bg,(0,0))


#class Sprite(pygame.sprite.Sprite):
    #def __init__(self,color,height,width):
        #super().__init__()

        #self.image = pygame.Surface([width, height])
        #self.image.fill(COL)
        #self.image.set_colorkey(color)

        #pygame.draw.rect(self.image,color,pygame.Rect(0,0, width,height))

        #self.rect = self.image.get._rect()

        #return()

playerimg = pygame.image.load("spaceship.png")
playerx = player_x_pos
playery = player_y_pos
#screen.blit(playerimg,(playerx,playery))
playerx_change = 0
def player(x,y):
    screen.blit(playerimg,(x,y))
#while runing == True:
    #for event in pygame.event.get():
        #if event.type == pygame.K_a:
            #obj.rect.x = obj.rect.x + 10
runing=True
while runing:
    screen.blit(bg,(10,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  
    player(playerx,playery)
    pygame.display.update()  
#playerx += playerx_change
#playerimg(playerx,playery)
         
    