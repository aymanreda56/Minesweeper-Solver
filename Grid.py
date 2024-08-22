import numpy as np
import pyautogui
from time import sleep
import random


class Cell:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.value = "U"      #all possible values are: 0,1,2,3,4,5,6,UNK,FLG
        self.isSafe = False


    def __repr__(self):
        # return f"{self.x}, {self.y}, {self.value}, {self.isSafe}"
        return (self.x, self.y, self.value,)

    def __str__(self):
        return f"X: {self.x}, Y: {self.y}, Value: {self.value}"
    
    def __hash__(self):
        return hash((self.x, self.y, self.value,))
    
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and self.value == other.value)




class GridObj:
    def __init__(self, rows, columns):
        self.Grid = list()
        self.FlagCells = list()
        self.SafeCells = list()
        self.UnknownCells = list()

        self.rows = rows
        self.columns = columns

        for i in range(rows):
            self.Grid.append([])
            for j in range(columns):
                new_cell = Cell()
                new_cell.x = j
                new_cell.y = i
                self.Grid[i].append(new_cell)
                self.UnknownCells.append(new_cell)



    def GetNeighbors(self, cell:Cell) -> list:
        returned_list = list()

        # if(cell.x < self.columns - 1):
        #     returned_list.append(self.Grid[cell.y][cell.x+1])
        #     if(cell.y < self.rows - 1):
        #         returned_list.append(self.Grid[cell.y+1][cell.x+1])


        # if(cell.x > 1):
        #     returned_list.append(self.Grid[cell.y][cell.x-1])
        #     if(cell.y < self.rows - 1):
        #         returned_list.append(self.Grid[cell.y+1][cell.x-1])


        # if(cell.y < self.rows - 1):
        #         returned_list.append(self.Grid[cell.y+1][cell.x])


        # if(cell.y > 1):
        #         returned_list.append(self.Grid[cell.y-1][cell.x])
        #         if(cell.x > 1):
        #             returned_list.append(self.Grid[cell.y-1][cell.x-1])
        #         if(cell.x < self.columns - 1):
        #             returned_list.append(self.Grid[cell.y-1][cell.x+1])

        returned_list = [
            self.Grid[cell.y-1][cell.x-1] if (cell.y > 0 and cell.x > 0 and self.Grid[cell.y-1][cell.x-1].value in ["U", "F"]) else None,
                 self.Grid[cell.y-1][cell.x] if (cell.y > 0 and self.Grid[cell.y-1][cell.x].value in ["U", "F"]) else None,
                 self.Grid[cell.y-1][cell.x+1] if(cell.y > 0 and cell.x < len(self.Grid[0]) - 1 and self.Grid[cell.y-1][cell.x+1].value in ["U", "F"]) else None,
                 self.Grid[cell.y][cell.x-1] if (cell.x > 0 and self.Grid[cell.y][cell.x-1].value in ["U", "F"]) else None,
                 self.Grid[cell.y][cell.x+1] if (cell.x < len(self.Grid[0]) - 1 and self.Grid[cell.y][cell.x+1].value in ["U", "F"]) else None,
                 self.Grid[cell.y+1][cell.x-1] if (cell.y < len(self.Grid) - 1 and cell.x > 0 and self.Grid[cell.y+1][cell.x-1].value in ["U", "F"]) else None,
                 self.Grid[cell.y+1][cell.x] if (cell.y < len(self.Grid) - 1 and self.Grid[cell.y+1][cell.x].value in ["U", "F"]) else None,
                 self.Grid[cell.y+1][cell.x+1] if (cell.y < len(self.Grid) - 1 and cell.x < len(self.Grid[0]) - 1 and self.Grid[cell.y+1][cell.x+1].value in ["U", "F"]) else None
                 ]
    
        return [i for i in returned_list if i] #return all non None neighbors
    


    def CheckCell(self, cell:Cell):

        print(f'Checking Cell {cell}')
        allNeighbors = self.GetNeighbors(cell)
        print(f'Checking Cell {cell} with neighbors: {len(allNeighbors)}')
        if(cell.value in ["1", "2", "3", "4", "5", "6"]):
            if(len(allNeighbors) == int(cell.value)):

                #I will just return the neighbours to be flagged as bombs, and the current cell to be popped.

                print(f"The Cell is checked and we will take an action")
                print(f"Flagging {[str(i) for i in allNeighbors]}\n\n\n\n")
                # sleep(2)
                return allNeighbors, cell
            
            else:
                #if number of neighbors exceeds the value of the current cell -> check for the number of flags in those neighbors
                number_flags = 0
                for neighbor in allNeighbors:
                    if neighbor.value == "F": number_flags+= 1
                if(number_flags == int(cell.value)):

                    #I will just return the neighbours to be flagged as bombs, and the current cell to be popped.

                    print(f"The Cell is checked and we will take an action ")
                    print(f"bombs are already flagged, which are at {[str(i) for i in allNeighbors]}\n\n\n\n")
                    # sleep(2)
                    return [], cell
            

            print(f"The Cell is ambigious, no neighbors = {len(allNeighbors)}   value of cell = {cell.value}\n")
            return None, None
        
        # print(f"Cell is not Interesting \n")
        return None, None
    


    def CheckAllPlayground(self):
        cells_to_be_popped = list()
        cells_to_be_flagged = list()
        for eachcells_row in self.Grid:
            for eachcell in eachcells_row:
                neighbors, pop_this_cell = self.CheckCell(eachcell)
                if(neighbors or pop_this_cell):
                    cells_to_be_popped.append(pop_this_cell)
                    cells_to_be_flagged += neighbors


        
        cells_to_be_flagged = list(set(cells_to_be_flagged))
            

        #updating our records of all flagged cells to not flag them again
        self.FlagCells += cells_to_be_flagged
        self.FlagCells = list(dict.fromkeys(self.FlagCells))


        self.SafeCells += cells_to_be_popped
        self.SafeCells = list(dict.fromkeys(self.SafeCells))

        return cells_to_be_flagged, cells_to_be_popped

        


    def PrettyPrint(self):
        final_text = r""
        for row_idx in range(len(self.Grid)):
            final_text += "\n"
            for col_idx in range(len(self.Grid[0])):
                if self.Grid[row_idx][col_idx].value == "U":
                    final_text += " ▣ "
                elif self.Grid[row_idx][col_idx].value == "0":
                    final_text += " □ "
                elif self.Grid[row_idx][col_idx].value == "F":
                    final_text += " ❂ "
                else:
                    final_text += " " + self.Grid[row_idx][col_idx].value + " "
        
        print(final_text)


    def PlayRound(self):
        pass









############################################ pyautogui functions (not logic oriented) ###############################




class SolverObj:

    def __init__(self, columns=30, rows=16):
        self.start_x = 0
        self.start_y = 0
        self.first_cell_x = 0
        self.first_cell_y = 0

        self.rows = rows
        self.columns = columns
    


    
    def Preparation_Step(self, title="Minesweeper X"):
        
        window = pyautogui.getWindowsWithTitle(title)[0]
        rect = window._rect

        self.start_x = rect.x
        self.start_y = rect.y
        self.width_of_window = window.width
        self.height_of_window = window.height

        # sleep(1)

        allcells = list()
        for i, pos in enumerate(pyautogui.locateAllOnScreen(image='unknown_cell.png', confidence=0.8)):
            center_x, center_y = pos.left + (pos.width / 2) , pos.top + (pos.height / 2)
            allcells.append((center_x, center_y,))

        self.first_cell_x = allcells[0][0]
        self.first_cell_y = allcells[0][1]

        print(len(allcells))

        number_of_cells = self.columns * self.rows
        # assert (len(allcells) == number_of_cells)





    

    def CheckPlayground(self, grid_obj:GridObj) -> list:
        pyautogui.moveTo(self.first_cell_x, self.first_cell_y)

        imaginary_cursor_x, imaginary_cursor_y = int(self.first_cell_x), int(self.first_cell_y)

        big_string = ""

        new_unknown_cells_list = []
        for cell_y in range(self.rows):
            for cell_x in range(self.columns):
                
                #searching for the cell in the safe (finished) cells, if it is already safe, then don't scan it again. 
                jmp_flag = False
                this_fucking_cell = None
                for safecell in grid_obj.SafeCells:
                    if safecell.x == cell_x and safecell.y == cell_y:
                        this_fucking_cell = safecell
                        jmp_flag = True
                        break

                if(jmp_flag):
                    printed = this_fucking_cell.value
                else:
                    printed = self.CheckCurrentCell(imaginary_cursor_x, imaginary_cursor_y)
                    if(printed == '0'):
                        new_cell = Cell()
                        new_cell.x, new_cell.y, new_cell.value, new_cell.isSafe = cell_x, cell_y, '0', True
                        grid_obj.SafeCells.append(new_cell)
                
                if(printed != "WTF"):
                    big_string += f"{printed}  "
                
                
                
                grid_obj.Grid[cell_y][cell_x].value = printed

                if(printed == "U"):
                    for unk_cell in grid_obj.UnknownCells:
                        if unk_cell.x == cell_x and unk_cell.y == cell_y:
                            new_unknown_cells_list.append(unk_cell)
                    

                # print(big_string)
                # print(chr(27) + "[2J")

                # pyautogui.move(xOffset=16, yOffset=0)
                imaginary_cursor_x += 16

            # pyautogui.move(xOffset=-(total_columns*16), yOffset=16)
            imaginary_cursor_x -= self.columns*16
            imaginary_cursor_y += 16
            big_string += "\n\n"

        grid_obj.UnknownCells = list(set(new_unknown_cells_list))

        return grid_obj, big_string
    

    def Take_Action(self, cells_to_be_flagged: list, cells_to_be_popped:list, gridobj:GridObj,duration=0):
        print("\n\n\n")
        print(f"Taking Action, flagging {[str(i) for i in cells_to_be_flagged]} and popping {[str(i) for i in cells_to_be_popped]}")

        if(not(cells_to_be_flagged or cells_to_be_popped)):
            self.Randomized_Click(gridObj=gridobj, duration = duration)

        else:
            action_result_bool = 0
            for neighbor_cell in cells_to_be_flagged:
                flagging_result = self.FlagCell(neighbor_cell, gridObj= gridobj, duration = duration)
                action_result_bool = action_result_bool or flagging_result

            for pop_cell in cells_to_be_popped:
                popping_result = self.PopCell(pop_cell, gridObj=gridobj, duration = duration)
                action_result_bool = action_result_bool or popping_result


            if(not(action_result_bool)):
                self.Randomized_Click(gridObj=gridobj, duration = duration)

        # sleep(2)
        

        

    

    
    def CheckCurrentCell(self, x:None, y:None) -> str:
        # img_1 = pyautogui.screenshot('sample_screenshot.png', region=(pyautogui.position().x-8, pyautogui.position().y-8, 16, 16))
        img_1 = pyautogui.screenshot(region=(x-8, y-8, 16, 16))
        
        for i in ['1', '2', '3', '4', '5', '6', 'F']:
            try:
                pos = pyautogui.locate(needleImage=f'{i}.png', haystackImage=img_1, confidence=0.8, grayscale=True)
                if(pos):
                    return i
            except:
                continue

        try:
            pos = pyautogui.locate(needleImage='unknown_cell.png', haystackImage=img_1, confidence=0.7, grayscale=True)
            return 'U'
        except:
            try:
                pos = pyautogui.locate(needleImage='0.png', haystackImage=img_1, confidence=0.95, grayscale=True)
                return '0'
            except:
                return 'WTF'
        
        return 'WTF'


    def Randomized_Click(self, gridObj: GridObj, duration = 0) -> None:
        random_idx = random.randint(0, len(gridObj.UnknownCells) - 1)

        random_x = gridObj.UnknownCells[random_idx].x
        random_y = gridObj.UnknownCells[random_idx].y

        pyautogui.moveTo(self.first_cell_x, self.first_cell_y, duration=duration)

        pyautogui.move(random_x*16, random_y*16)
        pyautogui.click()



    def PopRemainingUnknownCells(self, gridObj:GridObj, duration=0):
        pyautogui.moveTo(self.first_cell_x, self.first_cell_y, duration=duration)

        for rem_cell in gridObj.UnknownCells:
            pyautogui.move(rem_cell.x*16, rem_cell.y*16)
            pyautogui.click()
    



    def PopCell (self, target_cell:Cell, gridObj:GridObj, duration=0) -> int:


        this_fucking_cell = None
        for f in gridObj.SafeCells:
            if target_cell.x == f.x and target_cell.y == f.y:
                this_fucking_cell = f
                if(f.isSafe == True):
                    print(f'already Popped ({target_cell.x}, {target_cell.y})')
                    return 0

        pyautogui.moveTo(self.first_cell_x, self.first_cell_y, duration=duration)
        pyautogui.move(target_cell.x*16, target_cell.y*16)

        pyautogui.mouseDown(button='left')
        pyautogui.mouseDown(button='right')

        # A short delay to simulate the simultaneous click
        # sleep(0.005)  # 5 milliseconds

        # Release both buttons
        pyautogui.mouseUp(button='left')
        pyautogui.mouseUp(button='right')

        this_fucking_cell.isSafe = True
        return 1


    def FlagCell (self, target_cell:Cell, gridObj:GridObj ,duration=0) -> int:

        this_fucking_cell = None
        for f in gridObj.FlagCells:
            if target_cell.x == f.x and target_cell.y == f.y:
                this_fucking_cell = f
                if(f.value == 'F'):
                    print('already flagged')
                    return 0

        
        pyautogui.moveTo(self.first_cell_x, self.first_cell_y, duration=duration)
        pyautogui.move(target_cell.x*16, target_cell.y*16)
        pyautogui.rightClick()

        this_fucking_cell.value = 'F'
        return 1



    def WinCondition(self, gridObj: GridObj, number_of_Bombs_in_game: int) ->bool:
        return (len(gridObj.FlagCells) < number_of_Bombs_in_game)



