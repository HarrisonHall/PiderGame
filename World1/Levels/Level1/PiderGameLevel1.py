#"World 1 Level 1: A Rocky Start" by Harrison Hall

import Engine.levelEngine as levelEngine

thisLevel = levelEngine.level()
thisLevel.levelTitle = "World 1 Level 1: A Rocky Start"
thisLevel.levelStartText = "Ships cannot pass through rocks."
thisLevel.levelMap = [[1,  1,  1,  1,  1,  1,  1],
                      [1,  0,  1,  9,  1,  0,  1],
                      [1,  0,  1,  0,  1,  0,  1],
                      [1,  0,  1,  0,  1,  0,  1],
                      [1,  0,  1,  0,  1,  0,  1],
                      [1,  0,  1,  0,  1,  0,  1],
                      [1,  0,  1,  0,  1,  0,  1],
                      [1,  1,  1,  1,  1,  1,  1]]
thisLevel.maxTurns = 3
thisLevel.levelStartOrientation = 90
thisLevel.levelStartPosition = [3,6]

## Winning Piders:
'''
pider1 = piderEngine.pider("(90,true,motor.on)")
pider2 = piderEngine.pider("(90,true,nothing)")
pider3 = piderEngine.pider("(90,true,nothing)")
pider4 = piderEngine.pider("(90,true,nothing)")
pider5 = piderEngine.pider("(90,true,nothing)")
pider6 = piderEngine.pider("(90,true,nothing)")

piderList = [pider1,pider2,pider3,pider4,pider5,pider6]     
'''
