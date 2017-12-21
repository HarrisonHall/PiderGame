#swag.py is an older version of main.py

import time
import Engine.turnEngine as turnEngine
import Engine.piderEngine as piderEngine
import Engine.shipEngine as shipEngine


#TEMP! FIX ONCE FIXED
from Levels.Level2 import catCingLevel2 as thisLevel
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
pider1.directionInputOutput = "(90,false,turn.180)"
pider2 = piderEngine.pider()
pider2.directionInputOutput = "(90,true,motor.on)"
pider3 = piderEngine.pider()
pider3.directionInputOutput = "(90,true,speech.sup)"
pider4 = piderEngine.pider()
pider4.directionInputOutput = "(90,true,turn.90)"

def fun(n): # yeah boi
    return n*n*n


swag = fun(2) # makes swag super fun

piderList = [pider1, pider2, pider3]
##
##End test input
##

print("\n\nTitle TBD: Catcing or Piders, by Harrison Hall\n")
print("This is the Map:")
shipEngine.printMap(currentLevel.levelMap) #level1's thisLevel which is an instance of levelEngine's level
print("Piders, GO!")
turnEngine.runGame(currentLevel, randomShip, piderList)

