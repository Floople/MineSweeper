import random
import math

def makeBoard(rows:int,cols:int,mines:int):
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

def checkNeighbors(rows:int,cols:int,board):
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


def main():
    board = makeBoard(10,10,5)
    for r in board:
        print(r)

main()