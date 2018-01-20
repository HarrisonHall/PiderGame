#displayDriver.py


import pygame, sys
from pygame.locals import *
import copy

import os
from os.path import dirname, realpath, abspath

Black = (0,0,0)
Brown = (153,76,0)
Green = (0,255,0)
Blue = (0,0,255)
Silver = (192,192,192)
windleft = (0,0,120)
windright = (0,0,140)
windup = (0,0,160)
winddown = (0, 0, 180)
White = (255,255,255)

def pygameMap(inputMap, blockSize):
    print(os.getcwd())
    textures= {
                #Black : pygame.transform.scale(pygame.image.load('BlockSprites/deathblock.png'), (blockSize,blockSize)),
                #Brown : pygame.transform.scale(pygame.image.load('BlockSprites/rock.png'), (blockSize,blockSize)),
                #Green : pygame.transform.scale(pygame.image.load('BlockSprites/flag.png'), (blockSize,blockSize)),
                #Blue : pygame.transform.scale(pygame.image.load('BlockSprites/water.png'), (blockSize,blockSize)),
                #Silver : pygame.transform.scale(pygame.image.load('BlockSprites/woodship.png'), (blockSize,blockSize)),
                #Black : pygame.image.load(World1/BlockSprites/deathblock.png),

                #pygame.transform.scale(pygame.image.load((os.path.join('\\test', 'energy.png')))

                
                
                Black : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/deathblock.png'), (blockSize,blockSize)),
                Brown : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/rock.png'), (blockSize,blockSize)),
                Green : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/flag.png'), (blockSize,blockSize)),
                Blue : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/water.png'), (blockSize,blockSize)),
                Silver : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/woodship.png'), (blockSize,blockSize)),
        windleft : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/windleft.png'), (blockSize,blockSize)),
        windright : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/windright.png'), (blockSize,blockSize)),
        windup : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/windup.png'), (blockSize,blockSize)),
        winddown : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/winddown.png'), (blockSize,blockSize)),
        White : pygame.transform.scale(pygame.image.load('Engine/BlockSprites/iceberg.png'), (blockSize,blockSize)),

                
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
            elif inputMap[row][column] == 7:
                newMap[row][column] = Silver
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
            else:
                newMap[row][column] = Black
            column += 1
        row += 1
    
    #print(newMap)                ##Prints value
    
    mapHeight = len(inputMap)
    mapWidth = len(inputMap[0])
    tileSize = blockSize
    displaySurf = pygame.display.set_mode((mapWidth*tileSize,mapHeight*tileSize))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.exit(0)
            pygame.display.quit(0)
            sys.exit(0)
    
    for row in range(mapHeight):
        for column in range(mapWidth):
            displaySurf.blit(textures[newMap[row][column]], (column*tileSize, row*tileSize))
            #pygame.draw.rect(displaySurf, newMap[row][column], (column*tileSize, row*tileSize, tileSize,tileSize)) #change to display color version
    pygame.display.update()
