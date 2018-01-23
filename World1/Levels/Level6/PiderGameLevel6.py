#"World 1 Level 6: BoogyWoogy, This Got Harder" by Harrison Hall

import Engine.levelEngine as levelEngine

thisLevel = levelEngine.level()
thisLevel.levelTitle = "World 1 Level 6: BoogyWoogy, This Got Harder"
thisLevel.levelStartText = "More than one element means for a rough time."
thisLevel.levelMap = [[1,  1,  1,  1,  1,  1,  1,  1],
                      [1,  1,  0,  0,  2,  0, -1,  1],
                      [1,  0,  0,  0,  0,  2,  0,  1],
                      [1,  0,  0,  0,3.3,  0,  0,  1],
                      [1, -1,  0,3.1,  0,3.2, -1,  1],
                      [1,  0,  0,3.4,3.3,  0,  0,  1],
                      [1,  1,  1,  0,3.4,  0,  0,  1],
                      [1,  0,  9,  0,  0,  0,  0,  1],
                      [1,  0,  0,  0,  0,  0,  2,  1],
                      [1,  1,  1,  1,  1,  1,  1,  1]]
thisLevel.maxTurns = 10
thisLevel.levelStartOrientation = 90
thisLevel.levelStartPosition = [4,4]
