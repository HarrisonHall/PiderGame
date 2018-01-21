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

#Example Piders
pider1 = piderEngine.pider("(90,true,turn.180)")
pider2 = piderEngine.pider("(90,true,motor.on)")
pider3 = piderEngine.pider("(90,true,speech.sup)")
pider4 = piderEngine.pider("(90,speech.sup,turn.90)")
pider5 = piderEngine.pider("(0,height.1,turn.180)")
pider6 = piderEngine.pider("(90,height.0,speech.sup)")
pider7 = piderEngine.pider("(180,height.1,turn.0)")
pider8 = piderEngine.pider("(90,speech.sup,motor.on)")
pider9 = piderEngine.pider("(90,true,motor.on)")
pider10 = piderEngine.pider("(180,color.gray,turn.0)")
pider11 = piderEngine.pider("(0,color.gray,turn.180)")

piderList = [pider10, pider11, pider9]

##
##End test input
##

turnEngine.runGame(currentLevel, randomShip, piderList)
