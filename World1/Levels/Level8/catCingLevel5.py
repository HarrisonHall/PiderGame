#"Ship Kingdom: 2" by Harrison Hall
#import numpy as np

import Engine.levelEngine as levelEngine

thisLevel = levelEngine.level()
thisLevel.levelStartText = "Debug1: You have unlocked boats: small and wooden, motor: manual, pider: color, height."
#level1.unlocked.append("wood", "small", "manual", "color", "height")
thisLevel.levelMap = [[1,1,1,1,1,1,1,1],
                      [1,0,0,0,0,1,9,1],
                      [1,0,0,0,0,1,0,1],
                      [1,0,0,0,0,1,0,1],
                      [1,0,0,0,0,1,0,1],
                      [1,0,0,0,0,0,0,1],
                      [1,0,0,0,0,0,0,1],
                      [1,0,0,0,0,0,0,1],
                      [1,1,1,1,1,1,1,1]]
#level1.levelStartPosition = [0, 0]
thisLevel.maxTurns = 10
thisLevel.levelStartOrientation = 0
thisLevel.levelStartPosition = [1,1]

#level1.levelShip.type = "wood"

#print("\n" + level1.levelShip.size + "\n" + level1.levelShip.type)


#levelrun        
x = 0
score = 0
#currentMap = level1.levelMap
#while (x < level1.maxTurns):
#        print("\n\nswag")
#        game.turn(level1)
#        x += 1
#        
#print(score)
