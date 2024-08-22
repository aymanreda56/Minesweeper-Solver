import pyautogui
from time import sleep
from Grid import GridObj, Cell, SolverObj
import random


Solver = SolverObj(columns=30, rows=16)

Solver.Preparation_Step()


newgrid = GridObj(rows= 16, columns= 30)

newgrid, big_string = Solver.CheckPlayground(newgrid)

newgrid.PrettyPrint()


new_flags, new_pops = newgrid.CheckAllPlayground()

Solver.Take_Action(new_flags, new_pops, gridobj=newgrid)

#after each click or pop, we should check the playground, this is bcs a lot of holes can appear due to the click, so we need to scan for them.

while(Solver.WinCondition(gridObj=newgrid, number_of_Bombs_in_game=99)):
    newgrid, big_string = Solver.CheckPlayground(newgrid)
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
    newgrid, big_string = Solver.CheckPlayground(newgrid)
    new_flags, new_pops = newgrid.CheckAllPlayground()
    Solver.Take_Action(new_flags, new_pops, gridobj=newgrid, duration=0)


