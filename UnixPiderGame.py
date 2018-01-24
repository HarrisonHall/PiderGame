## A unix-based version of PiderGame by Harrison Hall

import time
import os
import sys

print("\nThis is an unix-based version of PiderGame")
input("\nFor a gui-version, launch 'PiderGame.py'. Press <enter> to continue.")
os.system("clear")

print("\n\t\t\t   PiderGame\n\n\t\t\tBy Harrison Hall")
time.sleep(3)

selectedWorld = 0
while ((selectedWorld < 1) or (selectedWorld > 1)):
    selectedWorld = int(input("\n\n>>Which world would you like to play? (only 1 is available): "))
    if selectedWorld == 1:
        os.chdir('World1')
        os.system('python3 unixmain.py')
        sys.exit()
