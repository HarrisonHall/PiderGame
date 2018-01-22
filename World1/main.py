#main.py

import time
import Engine.turnEngine as turnEngine
import Engine.piderEngine as piderEngine
import Engine.shipEngine as shipEngine

customLevelsNames = ["examplelevel"]

select = False
while (select == False):
    levelSelected =  input("Level: ")
    levelSelectInt = int(levelSelected)
    if levelSelectInt > 0 and levelSelectInt < 6:
        select = True
        if levelSelectInt == 5:
            from Levels.Level5 import PiderGameLevel5 as thisLevel
        elif levelSelectInt ==4:
            from Levels.Level4 import PiderGameLevel4 as thisLevel
        elif levelSelectInt == 3:
            from Levels.Level3 import PiderGameLevel3 as thisLevel
        elif levelSelectInt == 2:
            from Levels.Level2 import PiderGameLevel2 as thisLevel
        else:
            from Levels.Level1 import PiderGameLevel1 as thisLevel
    elif levelSelcted.lower() in customLevelNames:
        if levelSelcted.lower() == "examplelevel":
            from Levels.ExampleLevel import piderGameExampleLevel as thisLevel
    else:
        print("invalid")

currentLevel = thisLevel.thisLevel

##
##Test Input, to be removed
##
randomShip = shipEngine.ship()
randomShip.type = "wood"
randomShip.motor = "manual"
randomShip.size = "small"

import piderInput
piderList = piderInput.piderList
##
##End test input
##

turnEngine.runGame(currentLevel, randomShip, piderList)
