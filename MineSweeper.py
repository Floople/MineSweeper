import random
import math
import sys

def makeBoard(rows:int, cols:int, mines:int):
    board = [[0 for c in range(cols)] for r in range(rows)]
    while mines > 0:
        rowsRand = random.randint(0,rows - 1)
        colsRand = random.randint(0,cols -1)
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

def verifyBomb(rows:int, cols:int, agentView:list):
    mineCounter = 0
    hiddenCounter = 0
    if(agentView[rows][cols] == 'x' or agentView[rows][cols] <= 0):
        return False
    topLeftRows = rows - 1
    topLeftCols = cols - 1
    if(topLeftRows >= 0 and topLeftRows < len(agentView)) and (topLeftCols >= 0 and topLeftCols < len(agentView[0])):
        if(agentView[topLeftRows][topLeftCols] == -1 or agentView[topLeftRows][topLeftCols] == -3):
            mineCounter += 1
        elif(agentView[topLeftRows][topLeftCols] == 'x'):
            hiddenCounter += 1
    topRows = rows - 1
    topCols = cols
    if(topRows >= 0 and topRows < len(agentView)) and (topCols >= 0 and topCols < len(agentView[0])):
        if(agentView[topRows][topCols] == -1 or agentView[topRows][topCols] == -3):
            mineCounter += 1
        elif(agentView[topRows][topCols] == 'x'):
            hiddenCounter += 1
    topRightRows = rows - 1
    topRightCols = cols + 1
    if(topRightRows >= 0 and topRightRows < len(agentView)) and (topRightCols >= 0 and topRightCols < len(agentView[0])):
        if(agentView[topRightRows][topRightCols] == -1 or agentView[topRightRows][topRightCols] == -3):
            mineCounter += 1
        elif(agentView[topRightRows][topRightCols] == 'x'):
            hiddenCounter += 1
    BotLeftRows = rows + 1
    BotLeftCols = cols - 1
    if(BotLeftRows >= 0 and BotLeftRows < len(agentView)) and (BotLeftCols >= 0 and BotLeftCols < len(agentView[0])):
        if(agentView[BotLeftRows][BotLeftCols] == -1 or agentView[BotLeftRows][BotLeftCols] == -3):
            mineCounter += 1
        elif(agentView[BotLeftRows][BotLeftCols] == 'x'):
            hiddenCounter += 1
    BotRows = rows + 1
    BotCols = cols
    if(BotRows >= 0 and BotRows < len(agentView)) and (BotCols >= 0 and BotCols < len(agentView[0])):
        if(agentView[BotRows][BotCols] == -1 or agentView[BotRows][BotCols] == -3):
            mineCounter += 1
        elif(agentView[BotRows][BotCols] == 'x'):
            hiddenCounter += 1
    BotRightRows = rows + 1
    BotRightCols = cols + 1
    if(BotRightRows >= 0 and BotRightRows < len(agentView)) and (BotRightCols >= 0 and BotRightCols < len(agentView[0])):
        if(agentView[BotRightRows][BotRightCols] == -1 or agentView[BotRightRows][BotRightCols] == -3):
            mineCounter += 1
        elif(agentView[BotRightRows][BotRightCols] == 'x'):
            hiddenCounter += 1
    leftRows = rows
    leftCols = cols -1
    if(leftRows >= 0 and leftRows < len(agentView)) and (leftCols >= 0 and leftCols < len(agentView[0])):
        if(agentView[leftRows][leftCols] == -1 or agentView[leftRows][leftCols] == -3):
            mineCounter += 1
        elif(agentView[leftRows][leftCols] == 'x'):
            hiddenCounter += 1
    rightRows = rows
    rightCols = cols + 1
    if(rightRows >= 0 and rightRows < len(agentView)) and (rightCols >= 0 and rightCols < len(agentView[0])):
        if(agentView[rightRows][rightCols] == -1 or agentView[rightRows][rightCols] == -3):
            mineCounter += 1
        elif(agentView[rightRows][rightCols] == 'x'):
            hiddenCounter += 1
    
    if(agentView[rows][cols] - mineCounter == hiddenCounter):
        return True
    return False

def verifySafe(rows:int, cols:int, agentView:list, prints:bool):
    neighborCounter = 0
    hiddenCounter = 0
    if(agentView[rows][cols] == 'x' or agentView[rows][cols] <= 0):
        return False
    topLeftRows = rows - 1
    topLeftCols = cols - 1
    if(topLeftRows < 0 or topLeftRows >= len(agentView)) or (topLeftCols < 0 or topLeftCols >= len(agentView[0])):
        neighborCounter += 1
    elif(topLeftRows >= 0 and topLeftRows < len(agentView)) and (topLeftCols >= 0 and topLeftCols < len(agentView[0])):
        if(agentView[topLeftRows][topLeftCols] == 'x'):
            hiddenCounter += 1
        elif(agentView[topLeftRows][topLeftCols] >= 0 or agentView[topLeftRows][topLeftCols] == -2):
            neighborCounter += 1
    topRows = rows - 1
    topCols = cols
    if(topRows < 0 or topRows >= len(agentView)) or (topCols < 0 or topCols >= len(agentView[0])):
        neighborCounter += 1
    elif(topRows >= 0 and topRows < len(agentView)) and (topCols >= 0 and topCols < len(agentView[0])):
        if(agentView[topRows][topCols] == 'x'):
            hiddenCounter += 1
        elif(agentView[topRows][topCols] >= 0 or agentView[topRows][topCols] == -2):
            neighborCounter += 1
    topRightRows = rows - 1
    topRightCols = cols + 1
    if(topRightRows < 0 or topRightRows >= len(agentView)) or (topRightCols < 0 or topRightCols >= len(agentView[0])):
        neighborCounter += 1
    elif(topRightRows >= 0 and topRightRows < len(agentView)) and (topRightCols >= 0 and topRightCols < len(agentView[0])):
        if(agentView[topRightRows][topRightCols] == 'x'):
            hiddenCounter += 1
        elif(agentView[topRightRows][topRightCols] >= 0 or agentView[topRightRows][topRightCols] == -2):
            neighborCounter += 1
    BotLeftRows = rows + 1
    BotLeftCols = cols - 1
    if(BotLeftRows < 0 or BotLeftRows >= len(agentView)) or (BotLeftCols < 0 or BotLeftCols >= len(agentView[0])):
        neighborCounter += 1
    elif(BotLeftRows >= 0 and BotLeftRows < len(agentView)) and (BotLeftCols >= 0 and BotLeftCols < len(agentView[0])):
        if(agentView[BotLeftRows][BotLeftCols] == 'x'):
            hiddenCounter += 1
        elif(agentView[BotLeftRows][BotLeftCols] >= 0 or agentView[BotLeftRows][BotLeftCols] == -2):
            neighborCounter += 1
    BotRows = rows + 1
    BotCols = cols
    if(BotRows < 0 or BotRows >= len(agentView)) or (BotCols < 0 or BotCols >= len(agentView[0])):
        neighborCounter += 1
    elif(BotRows >= 0 and BotRows < len(agentView)) and (BotCols >= 0 and BotCols < len(agentView[0])):
        if(agentView[BotRows][BotCols] == 'x'):
            hiddenCounter += 1
        elif(agentView[BotRows][BotCols] >= 0 or agentView[BotRows][BotCols] == -2):
            neighborCounter += 1
    BotRightRows = rows + 1
    BotRightCols = cols + 1
    if(BotRightRows < 0 or BotRightRows >= len(agentView)) or (BotRightCols < 0 or BotRightCols >= len(agentView[0])):
        neighborCounter += 1
    elif(BotRightRows >= 0 and BotRightRows < len(agentView)) and (BotRightCols >= 0 and BotRightCols < len(agentView[0])):
        if(agentView[BotRightRows][BotRightCols] == 'x'):
            hiddenCounter += 1
        elif(agentView[BotRightRows][BotRightCols] >= 0 or agentView[BotRightRows][BotRightCols] == -2):
            neighborCounter += 1
    leftRows = rows
    leftCols = cols -1
    if(leftRows < 0 or leftRows >= len(agentView)) or (leftCols < 0 or leftCols >= len(agentView[0])):
        neighborCounter += 1
    elif(leftRows >= 0 and leftRows < len(agentView)) and (leftCols >= 0 and leftCols < len(agentView[0])):
        if(agentView[leftRows][leftCols] == 'x'):
            hiddenCounter += 1
        elif(agentView[leftRows][leftCols] >= 0 or agentView[leftRows][leftCols] == -2):
            neighborCounter += 1
    rightRows = rows
    rightCols = cols + 1
    if(rightRows < 0 or rightRows >= len(agentView)) or (rightCols < 0 or rightCols >= len(agentView[0])):
        neighborCounter += 1
    if(rightRows >= 0 and rightRows < len(agentView)) and (rightCols >= 0 and rightCols < len(agentView[0])):
        if(agentView[rightRows][rightCols] == 'x'):
            hiddenCounter += 1
        elif(agentView[rightRows][rightCols] >= 0 or agentView[rightRows][rightCols] == -2):
            neighborCounter += 1
    #print("Neighbor Count:" + str(neighborCounter))
    #print("Hidden Count: " + str(hiddenCounter))
    #print("Clue: " + str(agentView[rows][cols]))
    if(8 - agentView[rows][cols] - neighborCounter == hiddenCounter):
        return True
    
    return False
def basicAgent(board:list):
    # to store information agent knows
    agentView = [["x" for c in range(len(board))] for r in range(len(board[0]))]
    points = 0
    wrong = 0
    # check if board has all been uncovered
    agent = True
    row = random.randint(0, len(agentView) - 1)
    col = random.randint(0, len(agentView[0]) -1)
    tempCounter = 0
    while agent:
        # check if marked correctly, add point if it did
        if(agentView[row][col] == -3 and board[row][col] == -1):
            points += 1
        if(agentView[row][col] == -3 and board[row][col] != -1):
            wrong += 1
        # mark cell
        agentView[row][col] = board[row][col]
        
        # find surrounding cells
        # corner cells
        neighbors = findNeighbors(row,col,board)
        # if (row == 0 and col == 0) or (row == 0 and col == len(board[0])-1) or (row == len(board)-1 and col == 0) or (row == len(board)-1 and col == len(board[0])-1):
        #     neighbors = 3
        # # edge cells
        # elif row == 0 or col == 0 or row == len(board)-1 or col == len(board[0])-1:
        #     neighbors = 5
        # # middle cells
        # else:
        #     neighbors = 8
        
        # if cell is 0, mark all surrounding cells as safe (-2)
        if board[row][col] == 0:
            agentView = markAllNeighbors(agentView, row, col, neighbors, -2)
        # if number of mines = number of surroundng cells, mark all surrounding cells as mines
        for r in range(len(board)):
            for c in range(len(board[0])):
                if(verifyBomb(r,c,agentView)):
                    neighbors = findNeighbors(r,c,board)
                    agentView = markAllNeighbors(agentView, r, c, neighbors, -3)
        # if number of safe neighbors minus number of revealed safe neighbors = hidden, mark all surrounding cells as safe
        # print("After Verify Bomb")
        # for r in agentView:
        #     print(r)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if(verifySafe(r,c,agentView,tempCounter < 4)):
                    neighbors = findNeighbors(r,c,board)
                    agentView = markAllNeighbors(agentView, r, c, neighbors, -2)
                    # print("In safe")
                    # for s in agentView:
                    #     print(s)

        ### CHECKPOINT FOR TESTING
        # print(row, col)
        # for r in agentView:
        #     print(r)
        # print()

        # pick next cell
        # if safe cell available, pick next available safe cell
        row = 0
        col = 0
        nextReveal = False
        for r in range(len(agentView)):
            for c in range(len(agentView[0])):
                if agentView[r][c] == -2 or agentView[r][c] == -3:
                    nextReveal = True
                    break
            if nextReveal:
                break

        if nextReveal:
            row = r
            col = c
        # otherwise, pick random
        else:
            cnt = 0
            total = (len(agentView)-1) * (len(agentView[0])-1)
            visited = True
            while visited:
                if agentView[row][col] == "x":
                    visited = False
                    break
                if cnt == total:
                    break
                row = random.randint(0, len(agentView) - 1)
                col = random.randint(0, len(agentView[0]) -1) 
                cnt += 1
        # check if board has all been uncovered
        # for r in agentView:
        #     print(r)
        # print()
        allVisited = True
        for r in range(len(agentView)):
            for c in range(len(agentView[0])):
                if agentView[r][c] == "x" or agentView[r][c] == -2 or agentView[r][c] == -3:
                    allVisited = False
                    break
            if not allVisited:
                break
        if allVisited:
            agent = False
            #print("Total points: " + str(points))
            #print("Total wrong : " + str(wrong))
            return points
            #return agentView
        tempCounter += 1
        
    #print("Total points: " + str(points))
    #print("Total wrong : " + str(wrong))
    return points

def findNeighbors(row:int,col:int,board:list):
    if (row == 0 and col == 0) or (row == 0 and col == len(board[0])-1) or (row == len(board)-1 and col == 0) or (row == len(board)-1 and col == len(board[0])-1):
            neighbors = 3
        # edge cells
    elif row == 0 or col == 0 or row == len(board)-1 or col == len(board[0])-1:
        neighbors = 5
        # middle cells
    else:
        neighbors = 8
    return neighbors
def markAllNeighbors(agentView:list, row:int, col:int, neighbors:int, x:int):
    # x represents whether to mark all as safe or mark all as mines
    if neighbors == 3:
        #upper left corner
        if row == 0 and col == 0:
            if agentView[row][col+1] == "x":
                agentView[row][col+1] = x
            if agentView[row+1][col]== "x":
                agentView[row+1][col] = x
            if agentView[row+1][col+1]== "x":
                agentView[row+1][col+1] = x
        # upper right corner
        elif row == 0 and col == len(agentView[0])-1:
            if agentView[row][col-1]== "x":
                agentView[row][col-1] = x
            if agentView[row+1][col]== "x":
                agentView[row+1][col]= x
            if agentView[row+1][col-1]== "x":
                agentView[row+1][col-1]= x
        # lower left corner
        elif row == len(agentView)-1 and col == 0:
            if agentView[row-1][col]== "x":
                agentView[row-1][col] = x
            if agentView[row][col+1]== "x":
                agentView[row][col+1] = x
            if agentView[row-1][col+1]== "x":
                agentView[row-1][col+1] = x
        # lower right corner
        elif row == len(agentView)-1 and col == len(agentView[0])-1:
            if agentView[row][col-1]== "x":
                agentView[row][col-1] = x
            if agentView[row-1][col]== "x":
                agentView[row-1][col] = x
            if agentView[row-1][col-1]== "x":
                agentView[row-1][col-1] = x

    # edge cells
    elif neighbors == 5:
        # top edge
        if row == 0:
            if agentView[row][col-1]== "x":
                agentView[row][col-1] = x
            if agentView[row+1][col-1]== "x":
                agentView[row+1][col-1] = x
            if agentView[row+1][col]== "x":
                agentView[row+1][col] = x
            if agentView[row+1][col+1]== "x":
                agentView[row+1][col+1] = x
            if agentView[row][col+1]== "x":
                agentView[row][col+1] = x
        # left edge
        if col == 0:
            if agentView[row-1][col]== "x":
                agentView[row-1][col] = x
            if agentView[row-1][col+1]== "x":
                agentView[row-1][col+1] = x
            if agentView[row][col+1]== "x":
                agentView[row][col+1] = x
            if agentView[row+1][col+1]== "x":
                agentView[row+1][col+1] = x
            if agentView[row+1][col]== "x":
                agentView[row+1][col] = x
        # bottom edge
        if row == len(agentView)-1:
            if agentView[row][col-1]== "x":
                agentView[row][col-1] = x
            if agentView[row-1][col-1]== "x":
                agentView[row-1][col-1] = x
            if agentView[row-1][col]== "x":
                agentView[row-1][col] = x
            if agentView[row-1][col+1]== "x":
                agentView[row-1][col+1] = x
            if agentView[row][col+1]== "x":
                agentView[row][col+1] = x
        # right edge
        if col == len(agentView[0])-1:
            if agentView[row-1][col]== "x":
                agentView[row-1][col] = x
            if agentView[row-1][col-1]== "x":
                agentView[row-1][col-1] = x
            if agentView[row][col-1]== "x":
                agentView[row][col-1] = x
            if agentView[row+1][col-1]== "x":
                agentView[row+1][col-1] = x
            if agentView[row+1][col]== "x":
                agentView[row+1][col] = x
    # middle cells
    else:
        if agentView[row-1][col]== "x":
            agentView[row-1][col] = x
        if agentView[row-1][col+1]== "x":
            agentView[row-1][col+1] = x
        if agentView[row][col+1]== "x":
            agentView[row][col+1] = x
        if agentView[row+1][col+1]== "x":
            agentView[row+1][col+1] = x
        if agentView[row+1][col]== "x":
            agentView[row+1][col] = x
        if agentView[row+1][col-1]== "x":
            agentView[row+1][col-1] = x
        if agentView[row][col-1]== "x":
            agentView[row][col-1] = x
        if agentView[row-1][col-1]== "x":
            agentView[row-1][col-1] = x
    
    return agentView


def improvedAgent(board:list):
    # to store information agent knows
    agentView = [["x" for c in range(len(board))] for r in range(len(board[0]))]
    points = 0
    # check if board has all been uncovered
    agent = True
    row = random.randint(0, len(agentView) - 1)
    col = random.randint(0, len(agentView[0]) -1)
    tempCounter = 0
    while agent:
        # check if marked correctly, add point if it did
        if(agentView[row][col] == -3 and board[row][col] == -1):
            points += 1
        # if(agentView[row][col] == -3 and board[row][col] != -1):
        #     wrong += 1
        # mark cell
        agentView[row][col] = board[row][col]
        
        # find surrounding cells
        neighbors = findNeighbors(row,col,board)
        
        # if cell is 0, mark all surrounding cells as safe (-2)
        if board[row][col] == 0:
            agentView = markAllNeighbors(agentView, row, col, neighbors, -2)
        # if number of mines = number of surroundng cells, mark all surrounding cells as mines
        for r in range(len(board)):
            for c in range(len(board[0])):
                if(verifyBomb(r,c,agentView)):
                    neighbors = findNeighbors(r,c,board)
                    agentView = markAllNeighbors(agentView, r, c, neighbors, -3)
        # if number of safe neighbors minus number of revealed safe neighbors = hidden, mark all surrounding cells as safe
        # print("After Verify Bomb")
        # for r in agentView:
        #     print(r)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if(verifySafe(r,c,agentView,tempCounter < 4)):
                    neighbors = findNeighbors(r,c,board)
                    agentView = markAllNeighbors(agentView, r, c, neighbors, -2)
                    # print("In safe")
                    # for s in agentView:
                    #     print(s)

        ### CHECKPOINT FOR TESTING
        # print(row, col)
        # for r in agentView:
        #     print(r)
        # print()

        # pick next cell
        # if safe cell available, pick next available safe cell
        nextReveal = False
        for r in range(len(agentView)):
            for c in range(len(agentView[0])):
                if agentView[r][c] == -2 or agentView[r][c] == -3:
                    nextReveal = True
                    break
            if nextReveal:
                break

        if nextReveal:
            row = r
            col = c
        # otherwise, pick lowest probability
        else:
            # cnt = 0
            # total = (len(agentView)-1) * (len(agentView[0])-1)
            # visited = True
            # while visited:
            #     if agentView[row][col] == "x":
            #         visited = False
            #         break
            #     if cnt == total:
            #         break
                #gets smallest probability
            lowestProbability = sys.float_info.max
            for r in range(len(agentView)):
                for c in range(len(agentView[0])):
                    if(agentView[r][c]) == "x":
                        probability = 0
                        revealedNeighbors = 0
                        #get all neighbors and check bomb and stuff
                        def findProbability(row:int, col:int):
                            #clue - mines / hidden
                            clue = agentView[row][col]
                            if(clue != "x" and clue > 0):
                                nonlocal probability
                                nonlocal revealedNeighbors
                                revealedNeighbors += 1
                                mines = 0
                                hidden = 0
                                def countNeighbors(row:int,col:int):
                                    nonlocal mines
                                    nonlocal hidden
                                    if(agentView[row][col] == -1 or agentView[row][col] == -3):
                                        mines += 1
                                    elif(agentView[row][col] == "x"):
                                        hidden += 1
                                forEachNeighbor(row,col,agentView, countNeighbors)
                                probability += (clue - mines) / hidden      
                        forEachNeighbor(r,c,agentView,findProbability)
                        if(revealedNeighbors > 0):
                            probability = probability / revealedNeighbors
                            if(probability < lowestProbability):
                                row = r
                                col = c
                                lowestProbability = probability
                                #print("lowest found at: " + str(row) + "," + str(col) + " and is " + str(lowestProbability))
            if(lowestProbability == sys.float_info.max or lowestProbability == 0):
                row = random.randint(0, len(agentView) - 1)
                col = random.randint(0, len(agentView[0]) -1)
            #print("lowest probability at end is: " + str(lowestProbability))
            #print("Next cell will be: " + str(row) + "," + str(col))
        # check if board has all been uncovered
        # for r in agentView:
        #     print(r)
        allVisited = True
        for r in range(len(agentView)):
            for c in range(len(agentView[0])):
                if agentView[r][c] == "x" or agentView[r][c] == -2 or agentView[r][c] == -3:
                    allVisited = False
                    break
            if not allVisited:
                break
        if allVisited:
            agent = False
            #print("Total points: " + str(points))
            #print("Total wrong : " + str(wrong))
            #return agentView
            return points
        tempCounter += 1
        
    #print("Total points: " + str(points))
    #print("Total wrong : " + str(wrong))
    return points

def forEachNeighbor(row:int,col:int, agentView:list, func):
    neighbors = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 1), (row, col + 1), (row + 1, col -1), (row + 1, col), (row + 1, col + 1)]
    
    for (neighborRow, neighborCol) in neighbors:
        if(inBound(neighborRow, neighborCol,agentView)):
            func(neighborRow, neighborCol)

def inBound(row:int,col:int,agentView:list):
    if(row >= 0 and row < len(agentView) and (col >= 0 and col < len(agentView[0]))):
        return True
    else:
        return False
def main():
    x = 0
    totalOne = 0
    totalTwo = 0
    d = 10
    mineNum = 90
    while x < 1001:
        #print(x)
        board = makeBoard(d,d,mineNum)
        basicAgentView = basicAgent(board)
        #print(basicAgentView)
        totalOne += basicAgentView
        improvedAgentView = improvedAgent(board)
        #print(improvedAgentView)
        totalTwo += improvedAgentView
        x += 1
    avgOne = totalOne / 1000
    avgTwo = totalTwo / 1000
    print("average points for basic agent was " + str(avgOne))
    print("average points for improved agent was " + str(avgTwo))
main()