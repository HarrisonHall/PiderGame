# PiderGame
Arcade game using automated piders. Unix version requires Python3. Gui version requires Python3 and pygame.  

This is a personal project I'll be working on for the next few years. World 1 is approximately 80% complete with a completion date sometime before June 2018. 

## Getting Started
You can play PiderGame in both a text-only unix format with Python3, or via a gui in Python3 and PyGame.

### Text-Only
*Prerequisites*
* Install Python3
*Running*

* Clone or download to your desired location
* Launch UnixPiderGame.py 
  * Use your Python launcher
  * or in unix: `Python3 UnixPiderGame.py*`

### Gui-Version (in development)
*Prerequisites*
* Install Python3
* Install PyGame for Python3

*Running*
* Clone or download to your desired location
* Launch PiderGame.py 
  * Use your Python launcher
  * or in unix: `Python3 PiderGame.py*`

## Playing the game
Depending on the way you intend to play PiderGame, the rules are different.

### Editing the Piders
* Pider files are located in `World1/piderInput.py`
* piderEngine.py explanation:
```Python
class pider():
    def __init__(self, PiderDirectionInputOutput):
        self.directionInputOutput = PiderDirectionInputOutput
    #ex (270,speech.yes,speech.no) (90,true,turn.0)
    #outputs: motor.on, motor.off, turn.0, turn.90, turn.180, turn.270, speech.""
    #inputs: speech."", color.color, height.height
```
* You can use the unix pider-editor in `UnixPiderGame.py` to edit the piders (gui version coming soon)

## Dev Plan
I plan on working on PiderGame very slowly for the next few years. World 1 will use ships to get the user used to trusting and using piders to play the game for them. The following three worlds will slowly integrate a more physics-based experience.

### World 1
1. ~~Add color to piders~~
2. ~~Add animations to ship (probably not going to happen (nope I did it))~~
3. ~~Add new tiles to tilemap (along with functionality)~~
4. Create 10 levels
   * Keep in debug levels
5. Levelmap
6. World1 menu or gui

## Example Code and Execution

*Example Level File*
```Python
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
```
*Snip from piderEngine.py*
```Python
def piderCommands(piderList,shipDirection,thisLevel,xposition,yposition): #Add and position*
    runningPiderList = copy.deepcopy(piderList)
    speechArray = []
    outputArray = ["off",shipDirection] #[motorOn,direction]
    sightPidersArray = []
    speechPidersArray = []

    for x in runningPiderList:
        direction = findDirectionInputOutput(x, shipDirection)[0]
        y = copy.deepcopy(x)
        Input = findDirectionInputOutput(x, shipDirection)[1]
        Output = findDirectionInputOutput(x, shipDirection)[2]

        ##Section runs outputs if input is "true" (and does other inputs)
        ##else sends to runOutputsAgain
        if Input == "true":
            if Output == "motor.off":
                outputArray[0] = "off"
            elif Output == "motor.on":
                outputArray[0] = "on"
```
[//]: #![code1](/ExampleFiles/code1.png)
[//]: #![code2](/ExampleFiles/code2.png)

## Pictures and Example Output

![Game Output](/ExampleFiles/Level2.png)

```
Turn: 10

------------------------------------
1    1    1    1    1    1    1    
1    9    1    0    0    0    1    
1    0    1    0    1    0    1    
1    0    1    0    1    0    1    
1    0    1    0    1    0    1    
1    0    1    0    1    0    1    
1    0    1    0    1    0    1    
1    0    0    0    1    7.1  1    
1    1    1    1    1    1    1    

------------------------------------
1    1    1    1    1    1    1    
1    9    1    0    0    0    1    
1    0    1    0    1    0    1    
1    0    1    0    1    0    1    
1    0    1    0    1    0    1    
1    0    1    0    1    0    1    
1    0    1    0    1    0    1    
1    0    0    0    1    7.1  1    
1    1    1    1    1    1    1    

The piders have run out of energy!

Score:0
```

