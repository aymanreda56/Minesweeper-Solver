# Minesweeper-Solver :bomb:

<p align="center">
  <img src="https://github.com/aymanreda56/Minesweeper-Solver/blob/main/logo.png" width="350" title="Minesweeper Solver">
</p>



## An attempt to automate the gameplay of the famous game, Minesweeper. using pyautogui and a bunch of algorithms 💅

This is just an approach to test my ability to automate simple retro games, and because I am weirdly addicted to minesweeper. this program does the following:-
* Scans the game window for all cells
* Reads the cells' contents
* Interprets the scanned cells into a software grid
* Finds the best moves (Flagging/popping/exploring cells)
* Does the best moves
* Solves the tie and ambiguity issues
* Repeats until winning or losing

## Watch the demo 😎
[![Watch the video](https://img.youtube.com/vi/Jsr-WL50e7s/hqdefault.jpg)](https://youtu.be/Jsr-WL50e7s)

## How to install and use 🚀
1. Clone this repo
2. ```pip install -r requirements.txt```
3. ```py Solver.py --width <your_width_here> --height <your_height_here> --bombs <your_number_of_bombs>```
4. Quickly open minesweeper, or focus on it.
5. Enjoy :)

note: the ```--bombs``` argument can accept the exact number of bombs, or any upper bound of the bombs that you are sure the actual number of bombs will never exceed it.
if you entered smaller number of bombs than the actual number, the autosolver will just halt midgame 🤷‍♂️

## For other fellow developers 👽
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
* This is where anything related to IO is done
* This includes:- Scanning each cell, Scanning the entire grid, Reading cell contents, Clicking on cells, Flagging bomb cells
* This is the slowest class ever, the bottle neck happens here
* Keeps track of minisicule details like the starting pixel of the first cell and scans the entire grid via Image Processing
* Taking Actions is done here.
* The available actions are: Flagging a cell, Popping a cell, Randomly selecting a cell during ambiguities.

## 4. Solver.py (the main file)
This is just the final file where we parse arguments.
This file contains the main loop.
As long as the game is not won or lost:-
1) Scan the entire grid
2) Register the scanned grid into a software grid (or update the existing software grid)
3) Find the next actions
4) Do the actions

## Todo Work
A lot of times, the algorithm just gets stuck in an ambiguous situation and the only way out is to select a random cell and pop it.

A good approach is to search for some recurring patterns like:-

![image](https://github.com/user-attachments/assets/996b825b-b702-4d3c-b61c-19d9d680d8f9)
![image](https://github.com/user-attachments/assets/90bd4cdd-2bca-413f-898e-2c1f7dfb10ea)
![image](https://github.com/user-attachments/assets/ca69c3db-0b4f-4ea0-815f-18d4856416c4)
![image](https://github.com/user-attachments/assets/3c264500-fae8-4261-b2c5-5f5acf93452c)

Those patterns can sometimes help break an ambiguous situation, they can be implemented to further reduce the number of randomly selected cells.

## Suggestions and Improvements 😇
This repo is open for suggestions and improvements, if you have any comment, suggestion, critic, update or anything you want to reach this repo, feel free to request a pull or contact me directly via my email: ayman.mohamed00@eng-st.cu.edu.eg
