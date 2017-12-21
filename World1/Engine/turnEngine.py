#turnEngine.py

from . import piderEngine
from . import shipEngine
import time

def runGame(thisLevel, thisShip, piderList):
    gameDirection = thisLevel.levelStartOrientation
    movementDecision = ["off",gameDirection]
    returnValues = []
    currentPosition = [thisLevel.levelStartPosition[0],thisLevel.levelStartPosition[1]]
    gameTurns = 1
    score = gameTurns
    while (gameTurns <= thisLevel.maxTurns):
        print("\n\nTurn: " + str(gameTurns))
        print("")
        movementDecision = piderEngine.piderCommands(piderList,movementDecision[1],thisLevel,currentPosition[0],currentPosition[1]) #return [("on"/"off"), direction]
        returnValues = shipEngine.shipMove(thisShip.type, thisShip.size, movementDecision[1], thisLevel, movementDecision[0], 60, currentPosition[0], currentPosition[1]) #["go",xposition,yposition]
        print(returnValues) #remove**
        currentPosition = [returnValues[1],returnValues[2]]
        #movementDecision[1] = returnValues[1]
        gameTurns += 1
        
        #Score Calculation and Correction
        score = (thisLevel.maxTurns - gameTurns)
        if score < 0:
            score = 0
            
            
        if returnValues[0] == "win":
            print("\nCool. You won. Yay.")
            print("\nScore:" + str(score))
            break
        elif returnValues[0] == "lose":
            print("\nRIP")
            print("\nScore:" + str(score))
            break
        if gameTurns == (thisLevel.maxTurns+1):
            print("RIP, you lose m8. No turns.")
            print("\nScore:" + str(score))
        
        time.sleep(0.5)
