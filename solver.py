import pyautogui
from time import sleep
from Grid import GridObj, Cell, SolverObj
import random
import argparse


parser = argparse.ArgumentParser(
                    prog='Minesweeper Solver',
                    description='This is just an amateur code that tries to solve the minesweeper problem using pyautogui. you should enter the width, height and number of bombs of the game, if you dont know the number of bombs then enter any big number that you are sure exceeds the actual number of bombs',
                    epilog='Please pray for me, I am living the worst days of my life')

parser.add_argument('--width')
parser.add_argument('--height')
parser.add_argument('--bombs')
args = parser.parse_args()

columns = int(args.width)
rows = int(args.height)
bombs = int(args.bombs)

Solver = SolverObj(columns=columns, rows=rows)

Solver.Preparation_Step()


newgrid = GridObj(rows= rows, columns= columns)

newgrid, big_string = Solver.CheckPlayground2(newgrid)

newgrid.PrettyPrint()


new_flags, new_pops = newgrid.CheckAllPlayground()

Solver.Take_Action(new_flags, new_pops, gridobj=newgrid)

#after each click or pop, we should check the playground, this is bcs a lot of holes can appear due to the click, so we need to scan for them.

while(Solver.WinCondition(gridObj=newgrid, number_of_Bombs_in_game=bombs)):
    newgrid, big_string = Solver.CheckPlayground2(newgrid)
    new_flags, new_pops = newgrid.CheckAllPlayground()
    Solver.Take_Action(new_flags, new_pops, gridobj=newgrid, duration=0)

Solver.PopRemainingUnknownCells(gridObj=newgrid, duration=0)


winCond = False
loseCond = False
try:
    winCond = pyautogui.locateAllOnScreen(image='win.png', confidence=0.8)
except: pass
try:
    loseCond = pyautogui.locateAllOnScreen(image='lose.png', confidence=0.8)
except: pass

while(not winCond):
    try:
        winCond = pyautogui.locateAllOnScreen(image='win.png', confidence=0.8)
    except: pass

    try:
        loseCond = pyautogui.locateAllOnScreen(image='lose.png', confidence=0.8)
    except: pass
    if(loseCond):
        break
    newgrid, big_string = Solver.CheckPlayground2(newgrid)
    new_flags, new_pops = newgrid.CheckAllPlayground()
    Solver.Take_Action(new_flags, new_pops, gridobj=newgrid, duration=0)


