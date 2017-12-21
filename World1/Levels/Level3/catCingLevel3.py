#"Ship Kingdom Debug: 3" by Harrison Hall

import Engine.levelEngine as levelEngine

thisLevel = levelEngine.level()
thisLevel.levelStartText = "Debug1: You have unlocked boats: small and wooden, motor: manual, pider: color, height."
#level1.unlocked.append("wood", "small", "manual", "color", "height")
thisLevel.levelMap = [[1,1,1,1,1,1,1],
                      [1,9,1,0,0,0,1],
                      [1,0,1,0,1,0,1],
                      [1,0,1,0,1,0,1],
                      [1,0,1,0,1,0,1],
                      [1,0,1,0,1,0,1],
                      [1,0,1,0,1,0,1],
                      [1,0,0,0,1,0,1],
                      [1,1,1,1,1,1,1]]
thisLevel.maxTurns = 10
thisLevel.levelStartOrientation = 90
thisLevel.levelStartPosition = [5,7]
