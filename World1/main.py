#main.py

import time
import Engine.turnEngine as turnEngine
import Engine.piderEngine as piderEngine
import Engine.shipEngine as shipEngine


select = False
while (select == False):
    levelSelected =  int(input("Level: "))
    if levelSelected > 0 and levelSelected < 5:
        select = True
        if levelSelected ==4:
            from Levels.Level4 import catCingLevel4 as thisLevel
        elif levelSelected == 3:
            from Levels.Level3 import catCingLevel3 as thisLevel
        elif levelSelected == 2:
            from Levels.Level2 import catCingLevel2 as thisLevel
        else:
            from Levels.Level1 import catCingLevel1 as thisLevel
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
pider9 = piderEngine.pider("(90,color.blue,motor.on)")
pider10 = piderEngine.pider("(180,color.gray,turn.0)")
pider11 = piderEngine.pider("(0,color.gray,turn.180)")

piderList = [pider10, pider11, pider9]

##
##End test input
##



print("\n\nThe PiderGame: by Harrison Hall\n")
print("This is the Map:")
shipEngine.printMap(currentLevel.levelMap) #level1's thisLevel which is an instance of levelEngine's level
print("Piders, GO!")
print("\nStartOrientation: ",currentLevel.levelStartOrientation)
turnEngine.runGame(currentLevel, randomShip, piderList)
