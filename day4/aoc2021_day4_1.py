#answer:

def checkBingo(board):
    bingoCounter=0
    isBingo=False;
    for row in range(len(board)):
        print(board[row])
        #bingoCounter=0
        for pos in range(len(board[row])):
            if board[row][pos]=='X':
                bingoCounter+=1
            if bingoCounter==3:
                isBingo=True
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
testBoard=[ ['2', 'X', 'X'],
            ['1', '4', '3'],
            ['2', '3', '2'],
            ['3', '3', '5'] ]

isBingo=checkBingo(testBoard)
print(isBingo)
