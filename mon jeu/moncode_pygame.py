import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()

fenetre = pygame.display.set_mode((640, 480))

perso = pygame.image.load("perso.png").convert_alpha()

position_perso = perso.get_rect()

pas_deplacement = 15

while True :
    fenetre.fill([10,186,181])
    position_perso.topleft = (randint(0,540), randint(0,380))
    fenetre.blit(perso, position_perso)
    pygame.display.flip()
    pygame.time.delay(1000)
    
    for event in pygame.event.get():   
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                print("flèche droite appuyée")
    pygame.key.set_repeat(50)
    
    for event in pygame.event.get():    
        if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                print("clic gauche détecté")
    pygame.mouse.get_pos()




