#unixmain.py

import time
import Engine.unixTurnEngine as turnEngineunix
import Engine.piderEngine as piderEngine
import Engine.unixShipEngine as shipEngine
import sys

customLevelNames = ["examplelevel"]

userCommand = "nada"
while (userCommand.lower() != "q"):
    userCommand = input(">>[Options: play level (p), edit piders (e), view levels (v), quit (q)]: ")
    if userCommand == "q":
        print("\nHave a nice day!\n")
        sys.exit()
    elif userCommand == "e":
        print("\nEdit the piders:  \n")
        piderChoice = "1"
        while(piderChoice != "q" and piderChoice != "e"):
            piderChoice = input(">>>[Options: choose pider (1, 2,...6), exit (e)]: ")
            if piderChoice == "q" or piderChoice == "e":
                pass
            else:
                piderDirection = input("Direction (0,90,180,270): ")
                piderInput = input("Input (true,speech.x,color.x): ")
                piderOutput = input("Output (motor.on/off,turn.direction,speech.x,nothing): ")
                noMistake = input("Are you sure (y/n): ")
                newPider = " = piderEngine.pider(\"(" + piderDirection + "," + piderInput + "," + piderOutput + ")\")"
                writeLine = int(piderChoice)
                if noMistake == "y":
                    if piderChoice == "1":
                        newPider = "pider1" + newPider
                    elif piderChoice == "2":
                        newPider = "pider2" + newPider
                    elif piderChoice == "3":
                        newPider = "pider3" + newPider
                    elif piderChoice == "4":
                        newPider = "pider4" + newPider
                    elif piderChoice == "5":
                        newPider = "pider5" + newPider
                    else: #piderChoice == "6"
                        writeLine = 6
                        newPider = "pider6" + newPider
                    newPider += "\n"
                    writeFile = "piderInput.py"
                    theFile = open(writeFile,"r")
                    lineNumber = 1
                    fileLines = []
                    for line in theFile:
                        fileLines.append(line)
                    fileLines[writeLine] = newPider
                    theFile.close()
                    theFile = open(writeFile,"w")
                    theFile.writelines(fileLines)
                    print("...written...")
                    theFile.close()
                    
    elif userCommand == "v":
        showLevel = False
        levelSelected =  input("\n>>Level (1-10): ")
        levelSelectInt = int(levelSelected)
        if levelSelectInt < 11 and levelSelectInt > 0:
            showLevel = True
        if levelSelectInt == 10:
            from Levels.Level10 import PiderGameLevel10 as thisLevel
        elif levelSelectInt == 9:
            from Levels.Level9 import PiderGameLevel9 as thisLevel
        elif levelSelectInt == 8:
            from Levels.Level8 import PiderGameLevel8 as thisLevel
        elif levelSelectInt == 7:
            from Levels.Level7 import PiderGameLevel7 as thisLevel
        elif levelSelectInt == 6:
            from Levels.Level6 import PiderGameLevel6 as thisLevel
        elif levelSelectInt == 5:
            from Levels.Level5 import PiderGameLevel5 as thisLevel
        elif levelSelectInt ==4:
            from Levels.Level4 import PiderGameLevel4 as thisLevel
        elif levelSelectInt == 3:
            from Levels.Level3 import PiderGameLevel3 as thisLevel
        elif levelSelectInt == 2:
            from Levels.Level2 import PiderGameLevel2 as thisLevel
        else:
            from Levels.Level1 import PiderGameLevel1 as thisLevel
        
        if levelSelected.lower() in customLevelNames:
            if levelSelected.lower() == "examplelevel":
                from Levels.ExampleLevel import piderGameExampleLevel as thisLevel
                showLevel = True
        if showLevel == True:
            print("\n",thisLevel.thisLevel.levelTitle,"\n",thisLevel.thisLevel.levelStartText,"\n\nMax Turns: ",thisLevel.thisLevel.maxTurns,"\n")
            shipEngine.printMap(thisLevel.thisLevel.levelMap)
            print("\nOrientation: ",thisLevel.thisLevel.levelStartOrientation,"\nStart Position ((0,0) in top left): ",thisLevel.thisLevel.levelStartPosition)
    elif userCommand == "p":
        select = False
        while (select == False):
            levelSelected =  input("\nLevel: ")
            levelSelectInt = int(levelSelected)
            if levelSelectInt > 0 and levelSelectInt < 11:
                select = True
                if levelSelectInt == 10:
                    from Levels.Level10 import PiderGameLevel10 as thisLevel
                elif levelSelectInt == 9:
                    from Levels.Level9 import PiderGameLevel9 as thisLevel
                elif levelSelectInt == 8:
                    from Levels.Level8 import PiderGameLevel8 as thisLevel
                elif levelSelectInt == 7:
                    from Levels.Level7 import PiderGameLevel7 as thisLevel
                elif levelSelectInt == 6:
                    from Levels.Level6 import PiderGameLevel6 as thisLevel
                elif levelSelectInt == 5:
                    from Levels.Level5 import PiderGameLevel5 as thisLevel
                elif levelSelectInt ==4:
                    from Levels.Level4 import PiderGameLevel4 as thisLevel
                elif levelSelectInt == 3:
                    from Levels.Level3 import PiderGameLevel3 as thisLevel
                elif levelSelectInt == 2:
                    from Levels.Level2 import PiderGameLevel2 as thisLevel
                else:
                    from Levels.Level1 import PiderGameLevel1 as thisLevel
            elif levelSelected.lower() in customLevelNames:
                if levelSelected.lower() == "examplelevel":
                    from Levels.ExampleLevel import piderGameExampleLevel as thisLevel
                else:
                    print("invalid")

            currentLevel = thisLevel.thisLevel

            ##
            ##Test Input, to be removed
            ##
            randomShip = shipEngine.ship()
            randomShip.type = "wood"
            randomShip.motor = "manual"
            randomShip.size = "small"

            import piderInput
            piderList = piderInput.piderList
            ##
            ##End test input
            ##

            turnEngineunix.runGame(currentLevel, randomShip, piderList)

            print("\n\n")
