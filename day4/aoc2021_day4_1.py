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
            if bingoCounter==3:
                isBingo=True
    return isBingo

def checkVerticalBingo(board):
    isBingo=False
    for col in range(len(board)-1):
        bingoCounter=0
        for pos in range(len(board[col])-1):
            if board[pos][col]=='X':
                bingoCounter+=1
            if bingoCounter==3:
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


print(boards[0])
testBoard=[ ['X', 'X', '9'],
            ['X', 'X', '9'],
            ['X', 'X', '9'],
            ['X', 'X', '9'] ]

isBingo=checkVerticalBingo(testBoard)
print(isBingo)
