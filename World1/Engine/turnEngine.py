#turnEngine.py

from . import piderEngine
from . import shipEngine
import time

def runGame(thisLevel, thisShip, piderList):
    print("\nThe Pider Game\n\nBy Harrison Hall\n")
    gameDirection = thisLevel.levelStartOrientation
    movementDecision = ["off",gameDirection]
    returnValues = []
    currentPosition = [thisLevel.levelStartPosition[0],thisLevel.levelStartPosition[1]]
    gameTurns = 1
    score = gameTurns
    print("\n",thisLevel.levelTitle,'\n\n"',thisLevel.levelStartText,'"\n')
    shipEngine.printMap(thisLevel.levelMap)
    while (gameTurns <= thisLevel.maxTurns):
        print("\n\nTurn: " + str(gameTurns))
        print("")
        movementDecision = piderEngine.piderCommands(piderList,movementDecision[1],thisLevel,currentPosition[0],currentPosition[1]) #return [("on"/"off"), direction]
        returnValues = shipEngine.shipMove(thisShip.type, thisShip.size, movementDecision[1], thisLevel, movementDecision[0], 60, currentPosition[0], currentPosition[1], gameTurns) #["go",xposition,yposition]
        #print(returnValues) #remove**
        currentPosition = [returnValues[1],returnValues[2]]
        #movementDecision[1] = returnValues[1]
        gameTurns += 1
        
        #Score Calculation and Correction
        score = (thisLevel.maxTurns - gameTurns)
        if score < 0:
            score = 0
            
            
        if returnValues[0] == "win":
            print("\nCongratulations!")
            print("\nScore:" + str(score))
            break
        elif returnValues[0] == "lose":
            print("\nThe ship has crashed!")
            print("\nScore:" + str(score))
            break
        if gameTurns == (thisLevel.maxTurns+1):
            print("The piders have run out of energy!")
            print("\nScore:" + str(score))
        
        time.sleep(0.5)
