## How to make a level

1. Copy the `ExampleLevel` folder and rename it to something you like.
2. Rename `ExampleLevel/PiderGameExampleLevel.py` to a custom name.
3. Edit `Main.py`
   * Add the customLevelFolder to `customLevelNames`
   * Copy ```Python
        elif levelSelcted.lower() == "customlevelfolder":
                    from Levels.ExampleLevel import PiderGameExampleLevel as thisLevel```
        under ```Python
        if levelSelcted.lower() == "examplelevel":
                    from Levels.ExampleLevel import piderGameExampleLevel as thisLevel```
4. Modify PiderGameExampleLevel.py
* thisLevel.levelStartText holds any information you would like to give the user before the game begins
* thisLevel.levelMap holds the map of the level
  * -1 is a whirlpool
  * 0 is water
  * 1 is rock
  * 2 is an iceberg
  * 3.1-3.4 are various wind directions
  * 9 is the goal
  * thisLevel.maxTurns is the number of turns piders have to complete the level
  * thisLevel.levelStartOrientation is the direction (0, 90, 180, 270) the boat will be turned
  * thisLevel.levelStartPosition is an [x,y] coordinate of the starting position, with [0,0] being in the top left
5. Enjoy your level
