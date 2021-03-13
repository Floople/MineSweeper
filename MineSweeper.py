import random
import math

def makeBoard(rows:int, cols:int, mines:int):
    board = [[0 for c in range(cols)] for r in range(rows)]
    while mines > 0:
        rowsRand = random.randint(0,rows - 1)
        colsRand = random.randint(0,cols -1)
        print(rowsRand,colsRand)
        if(board[rowsRand][colsRand] != -1):
            board[rowsRand][colsRand] = -1
            mines -= 1
    for i in range(rows):
        for j in range(cols):
            if(board[i][j] == -1):
                continue
            counter = checkNeighbors(i,j,board) 
            board[i][j] = counter
    return board

def checkNeighbors(rows:int, cols:int, board:list):
    counter = 0
    topLeftRows = rows - 1
    topLeftCols = cols - 1
    if(topLeftRows >= 0 and topLeftRows < len(board)) and (topLeftCols >= 0 and topLeftCols < len(board[0])):
        if(board[topLeftRows][topLeftCols] == -1):
            counter += 1
    topRows = rows - 1
    topCols = cols
    if(topRows >= 0 and topRows < len(board)) and (topCols >= 0 and topCols < len(board[0])):
        if(board[topRows][topCols] == -1):
            counter += 1
    topRightRows = rows - 1
    topRightCols = cols + 1
    if(topRightRows >= 0 and topRightRows < len(board)) and (topRightCols >= 0 and topRightCols < len(board[0])):
        if(board[topRightRows][topRightCols] == -1):
            counter += 1
    BotLeftRows = rows + 1
    BotLeftCols = cols - 1
    if(BotLeftRows >= 0 and BotLeftRows < len(board)) and (BotLeftCols >= 0 and BotLeftCols < len(board[0])):
        if(board[BotLeftRows][BotLeftCols] == -1):
            counter += 1
    BotRows = rows + 1
    BotCols = cols
    if(BotRows >= 0 and BotRows < len(board)) and (BotCols >= 0 and BotCols < len(board[0])):
        if(board[BotRows][BotCols] == -1):
            counter += 1
    BotRightRows = rows + 1
    BotRightCols = cols + 1
    if(BotRightRows >= 0 and BotRightRows < len(board)) and (BotRightCols >= 0 and BotRightCols < len(board[0])):
        if(board[BotRightRows][BotRightCols] == -1):
            counter += 1
    leftRows = rows
    leftCols = cols -1
    if(leftRows >= 0 and leftRows < len(board)) and (leftCols >= 0 and leftCols < len(board[0])):
        if(board[leftRows][leftCols] == -1):
            counter += 1
    rightRows = rows
    rightCols = cols + 1
    if(rightRows >= 0 and rightRows < len(board)) and (rightCols >= 0 and rightCols < len(board[0])):
        if(board[rightRows][rightCols] == -1):
            counter += 1
    return counter

def basicAgent(board:list, agentView:list, row:int, col:int):
    # check cell
    # if cell is a mine
    if board[row][col] == -1:
        agentView[row][col] == -1

    # if cell is 0, aka no mines around, mark cell and surrounding cells as safe (safe = -2)
    elif board[row][col] == 0:
        # mark all surrounding cells safe
        neighbors = 0
        # corner cells
        if row == 0 & col == 0 | row == 0 & col == len(board[0])-1 | row == len(board)-1 & col == 0 | row == len(board)-1 & col == len(board[0])-1:
            neighbors = 3
        # edge cells
        elif row == 0 | col == 0 | row == len(board)-1 | col == len(board[0])-1:
            neighbors = 5
        # middle cells
        else:
            neighbors = 8
        if board[row][col] == neighbors:
            markAllNeighbors(board, agentView, row, col, neighbors, -2)

    # if cell is safe but not 0, mark with number of mines surrounding
    else:
        agentView[row][col] = board[row][col]
        # if number of mines == number of neighbors, mark all neighbors as mines
        neighbors = 0
        # corner cells
        if row == 0 & col == 0 | row == 0 & col == len(board[0])-1 | row == len(board)-1 & col == 0 | row == len(board)-1 & col == len(board[0])-1:
            neighbors = 3
        # edge cells
        elif row == 0 | col == 0 | row == len(board)-1 | col == len(board[0])-1:
            neighbors = 5
        # middle cells
        else:
            neighbors = 8
        if board[row][col] == neighbors:
            markAllNeighbors(board, agentView, row, col, neighbors, -1)

    for r in agentView:
        print(r)

    # check if board has all been uncovered
    allVisited = True
    for r in range(agentView):
        for c in range(agentView[0]):
            if agentView[r][c] == False:
                allVisited == False
                break
    # if everything has been uncovered, return agentView
    if allVisited:
        return agentView

    # pick next cell
    # if safe cell available, pick next available safe cell
    safeCell = False
    for r in range(agentView):
        for c in range(agentView[0]):
            if agentView[r][c] == -2:
                safeCell == True
                break
    if safeCell:
        newRow = r
        newCol = c
    # otherwise, pick random
    else:
        newRow = random.randint(0, len(board) - 1)
        newCol = random.randint(0, len(board[0]) -1)
        visited = True
        while visited:
            if agentView[col][row] == False:
                visited = False
            newRow = random.randint(0, len(board) - 1)
            newCol = random.randint(0, len(board[0]) -1) 
    
    return basicAgent(board, agentView, newRow, newCol)

def markAllNeighbors(board:list, agentView:list, row:int, col:int, neighbors:int, x:int):
    # x represents whether to mark all as safe or mark all as mines
    if neighbors == 3:
        #upper left corner
        if row == 0 & col == 0:
            agentView[row][col+1] = x
            agentView[row+1][col] = x
            agentView[row+1][col+1] = x
        # upper right corner
        if row == 0 & col == len(board[0])-1:
            agentView[row][col-1] = x
            agentView[row+1][col] = x
            agentView[row+1][col-1] = x
        # lower left corner
        if row == len(board)-1 & col == 0:
            agentView[row-1][col] = x
            agentView[row][col+1] = x
            agentView[row-1][col+1] = x
        # lower right corner
        if row == len(board)-1 & col == len(board[0])-1:
            agentView[row][col-1] = x
            agentView[row-1][col] = x
            agentView[row-1][col-1] = x

    # edge cells
    elif row == 0 | col == 0 | row == len(board)-1 | col == len(board[0])-1:
        neighbors = 5
        if board[row][col] == neighbors:
            # top edge
            if row == 0:
                agentView[row][col-1] = x
                agentView[row+1][col-1] = x
                agentView[row+1][col] = x
                agentView[row+1][col+1] = x
                agentView[row][col+1] = x
            # left edge
            if col == 0:
                agentView[row-1][col] = x
                agentView[row-1][col+1] = x
                agentView[row][col+1] = x
                agentView[row+1][col+1] = x
                agentView[row+1][col] = x
            # bottom edge
            if row == len(board)-1:
                agentView[row][col-1] = x
                agentView[row-1][col-1] = x
                agentView[row-1][col] = x
                agentView[row-1][col+1] = x
                agentView[row][col+1] = x
            # right edge
            if col == len(board[0])-1:
                agentView[row-1][col] = x
                agentView[row-1][col-1] = x
                agentView[row][col-1] = x
                agentView[row+1][col-1] = x
                agentView[row+1][col] = x
    # middle cells
    else:
        neighbors = 8
        if board[row][col] == neighbors:
            agentView[row-1][col] = x
            agentView[row-1][col+1] = x
            agentView[row][col+1] = x
            agentView[row+1][col+1] = x
            agentView[row+1][col] = x
            agentView[row+1][col-1] = x
            agentView[row][col-1] = x
            agentView[row-1][col-1] = x

def main():
    board = makeBoard(5,5,3)
    for r in board:
        print(r)
    agentView = [[False for i in range(board)] for j in range(board[0])]
    basicAgent(board, agentView, 0, 0)
    for r in agentView:
        print(r)

main()