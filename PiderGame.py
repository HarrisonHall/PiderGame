## PiderGame Gui Execution Script
## By Harrison Hall

from os import system
import pygame
from pygame.locals import *

pygame.init()

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')



startPressed = False
while (startPressed != True):

    mouse = pygame.mouse.get_pos()
    menuWidth = 500
    menuHeight = 800

    menu = pygame.display.set_mode((menuWidth,menuHeight))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    menu.fill((119,136,153))
    pidergameFont = pygame.font.Font('freesansbold.ttf',60)
    harryFont = pygame.font.Font('freesansbold.ttf',25)
    
    title = pidergameFont.render("PiderGame",1,(169,169,169))
    #title.get_rect.width()
    creator = harryFont.render("By Harrison Hall",1,(11,11,11))
    menu.blit(title, (menuWidth/2-title.get_rect().width/2,menuHeight/7))
    menu.blit(creator, (menuWidth/2-creator.get_rect().width/2,menuHeight/7*2))

    menuStart = pidergameFont.render("Start",1,(169,169,169))
    menuExit = pidergameFont.render("Exit",1,(250,250,250))

    menu.blit(menuStart, (menuWidth/2-menuStart.get_rect().width/2,menuHeight/7*5))
    menu.blit(menuExit, (menuWidth/2-menuExit.get_rect().width/2,menuHeight/7*6))

    if pygame.mouse.get_pressed()[0]:
        pygame.quit()
        print("swag")
        system('python3 World1/main.py')
        quit()
    
    pygame.display.update()
