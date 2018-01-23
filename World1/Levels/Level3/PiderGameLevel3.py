#"World 1 Level 3: Twisty and Turny" by Harrison Hall

import Engine.levelEngine as levelEngine

thisLevel = levelEngine.level()
thisLevel.levelStartText = "Piders can see both color and height of the objects. See if you can make choose to turn."
thisLevel.levelTitle = "World 1 Level 3: Twisty and Turny"
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
