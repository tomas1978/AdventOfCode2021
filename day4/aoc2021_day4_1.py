#answer:

def checkBingo(board):
    bingoCounter=0
    for row in range(len(board)):
        for pos in range(len(board[row])):
            if board[row][pos]=='X':
                bingoCounter+=1
    isBingo=False

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
