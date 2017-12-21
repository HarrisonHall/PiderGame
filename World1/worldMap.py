##worldMap.py

#from Levels.TestLevel import randomGameTests as test1
from Levels.Level1 import catCingLevel1 as level1
#from Levels.Level1 import catCingLevel1 as level1
#from Levels.Level1 import catCingLevel1 as level1
#from Levels.Level1 import catCingLevel1 as level1

print(level1.levelMap)

def chooseLevel():
    chosen = False
    while (chosen == False):
        levelPicked = input("Pick a level (eg. 1, 2, 3...):  ")
        if levelPicked > 0 and levelPicked < 4:
            print((level+levelPicked).levelMap)
            return (level+levelPicked) #def. needs fixing
        elif levelPicked.lower == "test1":
            return (test1)
        else:
            print("Invalid input!")
