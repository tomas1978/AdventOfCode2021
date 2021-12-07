#answer:

def checkBingo(board):
    bingoCounter=0
    for row in range(len(board)):
        #bingoCounter=0
        for pos in range(len(board[row])):
            if board[row][pos]=='X':
                bingoCounter+=1
            if bingoCounter==3:
                return True
            else:
                return False



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
testBoard=[ ['X', 'X', 'X'],
            ['X', 'X', 'X'],
            ['X', 'X', 'X'],
            ['4', '7', '5'] ]

isBingo=checkBingo(testBoard)
print(isBingo)
