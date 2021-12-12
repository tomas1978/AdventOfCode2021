#answer:

def checkHorizontalBingo(board):
    bingoCounter=0
    isBingo=False
    for row in range(len(board)):
        print(board[row])
        bingoCounter=0
        for pos in range(len(board[row])):
            if board[row][pos]=='X':
                bingoCounter+=1
            if bingoCounter==5:
                isBingo=True
    return isBingo

def checkVerticalBingo(board):
    isBingo=False
    for col in range(len(board)):
        bingoCounter=0
        for pos in range(len(board[col])):
            if board[pos][col]=='X':
                bingoCounter+=1
            if bingoCounter==5:
                isBingo=True;
    return isBingo

f = open('input.txt','r')
#bingoData = f.readlines()
continueRead=True
lineCounter=0
drawnNumbers=[]
board=[]
boards=[]
while continueRead:
    line=f.readline()
    if lineCounter==0:
        drawnNumbers.append(line)
    else:
        if(line!='\n'):
            board.append(line)
        else:
            boards.append(board)
            board=[]

    lineCounter+=1
    if not line:
        continueRead=False

board=[]
for i in range(6):
    board.append(boards[1][0].split())
print(board)


testBoard=[ ['1', 'X', 'X', 'X', 'X'],
            ['X', 'X', '8', 'X', 'X'],
            ['X', '5', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', '6', '3'] ]
#print(testBoard)
#isBingo=checkHorizontalBingo(testBoard)
#print(isBingo)
