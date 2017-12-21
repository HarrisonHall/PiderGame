#main.py

import time
import Engine.turnEngine as turnEngine
import Engine.piderEngine as piderEngine
import Engine.shipEngine as shipEngine


select = False
while (select == False):
    levelSelected =  int(input("Level: "))
    if levelSelected > 0 and levelSelected < 4:
        select = True
        if levelSelected == 3:
            from Levels.Level3 import catCingLevel3 as thisLevel
        elif levelSelected ==2:
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

pider1 = piderEngine.pider()
pider1.directionInputOutput = "(90,true,turn.180)"
pider2 = piderEngine.pider()
pider2.directionInputOutput = "(90,true,motor.on)"
pider3 = piderEngine.pider()
pider3.directionInputOutput = "(90,true,speech.sup)"
pider4 = piderEngine.pider()
pider4.directionInputOutput = "(90,speech.sup,turn.90)"
pider5 = piderEngine.pider()
pider5.directionInputOutput = "(0,height.1,turn.180)"
pider6 = piderEngine.pider()
pider6.directionInputOutput = "(90,height.0,speech.sup)"
pider7 = piderEngine.pider()
pider7.directionInputOutput = "(180,height.1,turn.0)"
pider8 = piderEngine.pider()
pider8.directionInputOutput = "(90,speech.sup,motor.on)"


piderList = [pider6, pider7, pider5, pider8]
##
##End test input
##

print("\n\nThe PiderGame: by Harrison Hall\n")
print("This is the Map:")
shipEngine.printMap(currentLevel.levelMap) #level1's thisLevel which is an instance of levelEngine's level
print("Piders, GO!")
print("\nStartOrientation: ",currentLevel.levelStartOrientation)
turnEngine.runGame(currentLevel, randomShip, piderList)
