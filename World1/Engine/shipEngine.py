#shipEngine.py

import time
import math
import copy
from . import displayDriver

class ship():
    type = "wood" #Types: wood, steel, aluminum   #compute densities for distance
    size = "small" #Size: small, medium, large
    motor = "manual" #Motor: manual, automatic
    direction = 0

def printMap(mapListofLists):
    for x in mapListofLists:
        print(x)
    print("")
        
def shipMove(shipMaterial, shipSize, shipDirection, thisLevel, motorOn, mapSize, xposition, yposition): #return ["(win/lose/go)",xposition,yposition]
    lose = False
    win = False
    currentMap = copy.deepcopy(thisLevel.levelMap)
    currentMap[yposition][xposition] = 7
    if shipMaterial.lower() == "aluminum": #also check unlocked for these
        mass = 2
    elif shipMaterial.lower() == "steel":
        mass = 3
    else:
        mass = 1 #wood, or else
    if shipSize.lower() == "large":
        volume = 3
    elif shipSize.lower() == "medium":
        volume = 2
    else:
        volume = 1
    density = mass / volume
    
    if density <=1:
        move = 100
    else:
        move = math.ceil(density)
    
    shipSprite = 7
    currentMap[yposition][xposition] = shipSprite
    printMap(currentMap)
    
    if motorOn == "on":
        while (move > 0):
            currentMap = copy.deepcopy(thisLevel.levelMap)
            if (shipDirection == 0 or shipDirection == 360):
                if (thisLevel.levelMap[yposition][xposition+1] == 0):
                    xposition += 1
                elif (thisLevel.levelMap[yposition][xposition+1] == 1):
                    move = 0
                elif (thisLevel.levelMap[yposition][xposition+1] == 9):
                    win = True
                    xposition += 1
                else: # -1
                    xposition += 1
                    lose = True
            elif shipDirection == 90:
                if (thisLevel.levelMap[yposition-1][xposition] == 0):
                    yposition -= 1
                elif (thisLevel.levelMap[yposition-1][xposition] == 1):
                    move = 0
                elif (thisLevel.levelMap[yposition-1][xposition] == 9):
                    win = True
                    yposition -= 1
                else: # -1
                    yposition -=1
                    lose = True
            elif shipDirection == 180:
                if (thisLevel.levelMap[yposition][xposition-1] == 0):
                    xposition -= 1
                elif (thisLevel.levelMap[yposition][xposition-1] == 1):
                    move = 0
                elif (thisLevel.levelMap[yposition][xposition-1] == 9):
                    win = True
                    xposition -= 1
                else: # -1
                    xposition -= 1
                    lose = True
            else: #shipDirection = 270 or wrong value
                if (thisLevel.levelMap[yposition+1][xposition] == 0):
                    yposition += 1
                elif (thisLevel.levelMap[yposition+1][xposition] == 1):
                    move = 0
                elif (thisLevel.levelMap[yposition+1][xposition] == 9):
                    win = True
                    yposition += 1
                else: # -1
                    yposition += 1
                    lose = True
            
            currentMap[yposition][xposition] = shipSprite
            
            if lose == True:
                time.sleep(1)
                shipSprite = 7.8
                currentMap[yposition][xposition] = shipSprite
                printMap(currentMap)
                displayDriver.pygameMap(currentMap, mapSize)
                print("Game Over")
                time.sleep(5)
                return ["lose",xposition,yposition]
            if win == True:
                time.sleep(1)
                shipSprite = 7.1
                currentMap[yposition][xposition] = shipSprite
                printMap(currentMap)
                displayDriver.pygameMap(currentMap, mapSize)
                print("")
                print("You win! Good Job!")
                print("")
                time.sleep(5)
                return ["win",xposition,yposition]
            
            currentMap[yposition][xposition] = shipSprite
            time.sleep(1)
            printMap(currentMap) #change position
            displayDriver.pygameMap(currentMap, mapSize)
            ##Comment out if visual map cannot display
            
            
            move -= 1
            if move <= 0:
                return ["go",xposition,yposition]
    else:
        currentMap[yposition][xposition] = shipSprite
        time.sleep(1)
        printMap(currentMap) #change position
        displayDriver.pygameMap(currentMap, mapSize)
        return ["stop",xposition,yposition]
