#"Ship Kingdom Debug: 1" by Harrison Hall
#import numpy as np

import Engine.levelEngine as levelEngine

thisLevel = levelEngine.level()
thisLevel.levelStartText = "Debug1: You have unlocked boats: small and wooden, motor: manual, pider: color, height."
#thisLevel.unlocked.append("wood", "small", "manual", "color", "height")
thisLevel.levelMap = [[1,1,1,1,1,1],
                      [1,0,0,-1,0,1],
                      [1,0,0,0,0,1],
                      [1,0,0,0,9,1],
                      [1,1,1,1,1,1],]
thisLevel.maxTurns = 10
thisLevel.levelStartOrientation = 0
thisLevel.levelStartPosition = [1,3]
