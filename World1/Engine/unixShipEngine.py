#shipEngine.py

import time
import math
import copy
#from . import displayDriver

class ship():
    type = "wood" #Types: wood, steel, aluminum   #compute densities for distance
    size = "small" #Size: small, medium, large
    motor = "manual" #Motor: manual, automatic
    direction = 0

def printMap(mapListofLists):
    maxLength = 0
    for x in mapListofLists:
        for tile in x:
            tile = len(str(tile))
            if tile > maxLength:
                maxLength = tile
    count = 0
    maxLength = 3
    for tile in mapListofLists[0]:
        count += maxLength + 2
    while(count >= 1):
        print("-",end="")
        count -= 1
    print("-")
    #print("maxLength",maxLength)
    spacingNumber = 0
    spacing = ""
    while(spacingNumber < (maxLength + 2)):
        spacing = spacing + " "
        spacingNumber += 1
    maxLength = 3
    for x in mapListofLists:
        maxLength = 3
        for tile in x:
            integer = str(tile)
            integerLength = len(integer)
            while(integerLength < maxLength+2):
                integer = integer + " "
                #print(".",integer,".")
                integerLength = len(integer)
            print(integer,end="")
        print("")
    print("")

def shipMove(shipMaterial, shipSize, shipDirection, thisLevel, motorOn, blockSizex, blockSizey, xposition, yposition, gameTurns): #return ["(win/lose/go)",xposition,yposition]
    lose = False
    win = False
    currentMap = copy.deepcopy(thisLevel.levelMap)
    if shipDirection == 0 or shipDirection == 360:
        currentMap[yposition][xposition] = 7.2
    elif shipDirection == 180:
        currentMap[yposition][xposition] = 7.1
    elif shipDirection == 90:
        currentMap[yposition][xposition] = 7.3
    elif shipDirection == 270:
        currentMap[yposition][xposition] = 7.4
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
    #currentMap[yposition][xposition] = shipSprite
    printMap(currentMap)
    
    if motorOn == "on":
        while (move > 0):
            currentMap = copy.deepcopy(thisLevel.levelMap)
            if (shipDirection == 0 or shipDirection == 360):
                if (thisLevel.levelMap[yposition][xposition+1] == 0):#water
                    xposition += 1
                elif (thisLevel.levelMap[yposition][xposition+1] == 1):#rock
                    move = 0
                elif (thisLevel.levelMap[yposition][xposition+1] == 9):#flag
                    win = True
                    xposition += 1
                elif (thisLevel.levelMap[yposition][xposition+1] == 2):#iceburg
                    xposition += 1
                    gameTurns += 1
                elif (thisLevel.levelMap[yposition][xposition+1] == 3.1):#windleft
                    move = 0
                elif (thisLevel.levelMap[yposition][xposition+1] == 3.2):#windright
                    xposition += 2
                elif (thisLevel.levelMap[yposition][xposition+1] == 3.3):#windup
                    yposition -= 1
                    xposition += 1
                elif (thisLevel.levelMap[yposition][xposition+1] == 3.4):#winddown
                    yposition -= 1
                    xposition += 1
                else: # -1, whirlpool
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
                elif (thisLevel.levelMap[yposition-1][xposition] == 2):#iceburg
                    yposition -= 1
                    gameTurns += 1
                elif (thisLevel.levelMap[yposition-1][xposition] == 3.1):#windleft
                    xposition -= 1
                    yposition -= 1
                elif (thisLevel.levelMap[yposition-1][xposition] == 3.2):#windright
                    xposition += 1
                    yposition -= 1
                elif (thisLevel.levelMap[yposition-1][xposition] == 3.3):#windup
                    yposition -= 2
                    print("We got here!")
                elif (thisLevel.levelMap[yposition-1][xposition] == 3.4):#winddown
                    move = 0
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
                elif (thisLevel.levelMap[yposition][xposition-1] == 2):#iceburg
                    xposition -= 1
                    gameTurns += 1
                elif (thisLevel.levelMap[yposition][xposition-1] == 3.1):#windleft
                    xposition -= 2
                elif (thisLevel.levelMap[yposition][xposition-1] == 3.2):#windright
                    move = 0
                elif (thisLevel.levelMap[yposition][xposition-1] == 3.3):#windup
                    yposition -= 1
                    xposition -= 1
                elif (thisLevel.levelMap[yposition][xposition-1] == 3.4):#winddown
                    yposition += 1
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
                elif (thisLevel.levelMap[yposition+1][xposition] == 2):#iceburg
                    yposition += 1
                    gameTurns += 1
                elif (thisLevel.levelMap[yposition+1][xposition] == 3.1):#windleft
                    xposition -= 1
                    yposition += 1
                elif (thisLevel.levelMap[yposition+1][xposition] == 3.2):#windright
                    xposition += 1
                    yposition += 1
                elif (thisLevel.levelMap[yposition+1][xposition] == 3.3):#windup
                    move = 0
                elif (thisLevel.levelMap[yposition+1][xposition] == 3.4):#winddown
                    yposition += 2
                else: # -1
                    yposition += 1
                    lose = True
            
#            currentMap[yposition][xposition] = shipSprite
            
            if lose == True:
                time.sleep(1)
                shipSprite = 7.8
                currentMap[yposition][xposition] = shipSprite
                printMap(currentMap)
                #displayDriver.pygameMap(currentMap, blockSizex, blockSizey)
                print("Game Over")
                time.sleep(5)
                return ["lose",xposition,yposition]
            if win == True:
                time.sleep(1)
                shipSprite = 7.7
                currentMap[yposition][xposition] = shipSprite
                printMap(currentMap)
                #displayDriver.pygameMap(currentMap, blockSizex, blockSizey)
                print("")
                print("You win! Good Job!")
                print("")
                time.sleep(5)
                return ["win",xposition,yposition]

            if shipDirection == 180:
                currentMap[yposition][xposition] = 7.1
            elif shipDirection == 0 or shipDirection == 360:
                currentMap[yposition][xposition] = 7.2
            elif shipDirection == 90:
                currentMap[yposition][xposition] = 7.3
            else:
                currentMap[yposition][xposition] = 7.4
            #currentMap[yposition][xposition] = shipSprite
            time.sleep(1)
            printMap(currentMap) #change position
            #displayDriver.pygameMap(currentMap, blockSizex, blockSizey)
            ##Comment out if visual map cannot display
            
            
            move -= 1
            if move <= 0:
                return ["go",xposition,yposition]
    else:
        #currentMap[yposition][xposition] = shipSprite
        if shipDirection == 180:
            currentMap[yposition][xposition] = 7.1
        elif shipDirection == 0 or shipDirection == 360:
            currentMap[yposition][xposition] = 7.2
        elif shipDirection == 90:
            currentMap[yposition][xposition] = 7.3
        else:
            currentMap[yposition][xposition] = 7.4
        time.sleep(1)
        printMap(currentMap) #change position
        #displayDriver.pygameMap(currentMap, blockSizex, blockSizey)
        return ["stop",xposition,yposition]
