import pygame, sys
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640, 480))
fenetre.fill([10,186,181])

perso = pygame.image.load("perso.png").convert_alpha()
position_perso = perso.get_rect()
position_perso.topleft = randint(a,b)
pygame.time.delay(1000)
fenetre.blit(perso, position_perso)

pygame.display.flip()

while True :
    for event in pygame.event.get():   
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                print("flèche droite appuyée")
    pygame.key.set_repeat(50)
    
    for event in pygame.event.get():    
        if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                print("clic gauche détecté")
    pygame.mouse.get_pos()




