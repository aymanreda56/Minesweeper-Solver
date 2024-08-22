# Minesweeper-Solver

big logo here

## An attempt to automate the gameplay of the famous game, Minesweeper. using pyautogui and a bunch of algorithms.

This is just an approach to test my ability to automate simple retro games, and because I am weirdly addicted to minesweeper. this program does the following:-
* Scans the game window for all cells
* Reads the cells' contents
* Interprets the scanned cells into a software grid
* Finds the best moves (Flagging/popping/exploring cells)
* Does the best moves
* Solves the tie and ambiguity issues
* Repeats until winning or losing

Video demo here

## How to install and use
1. Clone this repo
2. ```pip install -r requirements.txt```
3. ```py Solver.py --width <your_width_here> --height <your_height_here> --bombs <your_number_of_bombs>```
4. Quickly open minesweeper, or focus on it.
5. Enjoy :)

note: the ```--bombs``` argument can accept the exact number of bombs, or any upper bound of the bombs that you are sure the actual number of bombs will never exceed it.
if you entered smaller number of bombs than the actual number, the autosolver will just halt midgame 🤷‍♂️

## For other fellow developers
here is a simple breakdown of what is really done behind the scenes, there are 4 major modules:

## 1. Cell Class
This is just a wrapper class with some helper overloadings, representing a single software cell.

## 2. Grid Class
* This is the implementation of the software grid after being scanned from the screen.
* Any computation algorithm should be performed within this class.
* Keeping track of :- Safe cells, Flagged cells and available Unknown cells
* Computing the neighbors of each cell.
* Checking for the next move (flagging and popping) is done here.
* Checking a single cell for potential moves.
* Checking the entire grid for potential moves.

## 3. Solver Class


## 4. Solver.py (the main file)
