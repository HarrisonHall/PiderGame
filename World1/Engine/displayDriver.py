#displayDriver.py

import pygame, sys
from pygame.locals import *
import copy

import os
from os.path import dirname, realpath, abspath

Black = (0,0,0)
Brown = (153,76,0)
Green = (0,255,0)
Green2 = (0,200,0)
Blue = (0,0,255)
Silverleft = (192,190,192)
Silverright = (192,191,192)
Silverup = (192,192,192)
Silverdown = (192,193,192)
Silverdead = (200,200,200)
windleft = (0,0,120)
windright = (0,0,140)
windup = (0,0,160)
winddown = (0, 0, 180)
White = (255,255,255)

def pygameMap(inputMap, blockSizex, blockSizey):
    textures= { Black : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/deathblock.png'), (blockSizex,blockSizey)),
                Brown : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/rock.png'), (blockSizex,blockSizey)),
                Green : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/flag.png'), (blockSizex,blockSizey)),
                Green2 : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/shipwin.png'), (blockSizex,blockSizey)),
                Blue : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/water.png'), (blockSizex,blockSizey)),
                Silverleft : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/shipleft.png'), (blockSizex,blockSizey)),
                Silverright : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/shipright.png'), (blockSizex,blockSizey)),
                Silverup : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/shipup.png'), (blockSizex,blockSizey)),
                Silverdown : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/shipdown.png'), (blockSizex,blockSizey)),
                windleft : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/windleft.png'), (blockSizex,blockSizey)),
                windright : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/windright.png'), (blockSizex,blockSizey)),
                windup : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/windup.png'), (blockSizex,blockSizey)),
                winddown : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/winddown.png'), (blockSizex,blockSizey)),
                White : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/iceberg.png'), (blockSizex,blockSizey)),
                Silverdead : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/shipwreck.png'), (blockSizex,blockSizey)),
            }
    newMap = copy.deepcopy(inputMap)
    pygame.display.set_caption("Piders and Stuffs", "None")
    row = 0
    while row < len(inputMap):
        column = 0
        while column < len(inputMap[0]):
            if inputMap[row][column] == 0:
                newMap[row][column] = Blue
            elif inputMap[row][column] == 1:
                newMap[row][column] = Brown
            elif inputMap[row][column] == 9:
                newMap[row][column] = Green
            elif (inputMap[row][column] == 7.1):
                newMap[row][column] = Silverleft
            elif (inputMap[row][column] == 7.2):
                newMap[row][column] = Silverright
            elif (inputMap[row][column] == 7.3):
                newMap[row][column] = Silverup
            elif (inputMap[row][column] == 7.4):
                newMap[row][column] = Silverdown
            elif inputMap[row][column] == 2:
                newMap[row][column] = White
            elif inputMap[row][column] == 3.1:
                newMap[row][column] = windleft
            elif inputMap[row][column] == 3.2:
                newMap[row][column] = windright
            elif inputMap[row][column] == 3.3:
                newMap[row][column] = windup
            elif inputMap[row][column] == 3.4:
                newMap[row][column] = winddown
            elif inputMap[row][column] == 7.8:
                newMap[row][column] = Silverdead
            elif inputMap[row][column] == 7.7:
                newMap[row][column] = Green2
            else:
                newMap[row][column] = Black
            column += 1
        row += 1
   
    mapHeight = len(inputMap)
    mapWidth = len(inputMap[0])
    #tileSize = blockSize
    displaySurf = pygame.display.set_mode((mapWidth*blockSizex,mapHeight*blockSizey))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            print("\n\nHave a nice day!")
            pygame.quit()
            pygame.display.quit()
            sys.exit()
    
    for row in range(mapHeight):
        for column in range(mapWidth):
            displaySurf.blit(textures[newMap[row][column]], (column*blockSizex, row*blockSizey))
            #pygame.draw.rect(displaySurf, newMap[row][column], (column*tileSize, row*tileSize, tileSize,tileSize)) #change to display color version
    pygame.display.update()
