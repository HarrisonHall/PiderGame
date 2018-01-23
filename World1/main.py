#main.py

import time
import Engine.turnEngine as turnEngine
import Engine.piderEngine as piderEngine
import Engine.shipEngine as shipEngine

customLevelNames = ["examplelevel"]

select = False
while (select == False):
    levelSelected =  input("Level: ")
    levelSelectInt = int(levelSelected)
    if levelSelectInt > 0 and levelSelectInt < 11:
        select = True
        if levelSelectInt == 10:
            from Levels.Level10 import PiderGameLevel10 as thisLevel
        elif levelSelectInt == 9:
            from Levels.Level9 import PiderGameLevel9 as thisLevel
        elif levelSelectInt == 8:
            from Levels.Level8 import PiderGameLevel8 as thisLevel
        elif levelSelectInt == 7:
            from Levels.Level7 import PiderGameLevel7 as thisLevel
        elif levelSelectInt == 6:
            from Levels.Level6 import PiderGameLevel6 as thisLevel
        elif levelSelectInt == 5:
            from Levels.Level5 import PiderGameLevel5 as thisLevel
        elif levelSelectInt ==4:
            from Levels.Level4 import PiderGameLevel4 as thisLevel
        elif levelSelectInt == 3:
            from Levels.Level3 import PiderGameLevel3 as thisLevel
        elif levelSelectInt == 2:
            from Levels.Level2 import PiderGameLevel2 as thisLevel
        else:
            from Levels.Level1 import PiderGameLevel1 as thisLevel
    elif levelSelected.lower() in customLevelNames:
        if levelSelected.lower() == "examplelevel":
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
