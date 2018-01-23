# "World 1 Level 5: Learn the Winds" by Harrison Hall

import Engine.levelEngine as levelEngine

thisLevel = levelEngine.level()
thisLevel.levelStartText = "Winds sure are harsh."
thisLevel.levelTitle = "World 1 Level 5: Learn the Winds"
thisLevel.levelMap = [[1  ,1  ,1  ,1  ,1],
                      [1  ,2  ,9  ,2  ,1],
                      [1  ,3.2,3.4,3.1,1],
                      [1  ,2  ,0  ,0  ,1],
                      [1  ,3.3,0  ,0  ,1],
                      [1  ,0  ,0  ,0  ,1],
                      [1,  1  ,1  ,1  ,1]]
thisLevel.maxTurns = 10
thisLevel.levelStartOrientation = 90
thisLevel.levelStartPosition = [2,5]


x = 0
score = 0

