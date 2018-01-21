#"World 1 Level 1: A Rocky Start" by Harrison Hall

import Engine.levelEngine as levelEngine

thisLevel = levelEngine.level()
thisLevel.levelTitle = "World 1 Level 1: A Rocky Start"
thisLevel.levelStartText = "Ships cannot pass through rocks."
thisLevel.levelMap = [[1,  1,  1],
                      [1,  9,  1],
                      [1,  0,  1],
                      [1,  0,  1],
                      [1,  0,  1],
                      [1,  0,  1],
                      [1,  0,  1],
                      [1,  1,  1]]
thisLevel.maxTurns = 3
thisLevel.levelStartOrientation = 90
thisLevel.levelStartPosition = [1,6]
