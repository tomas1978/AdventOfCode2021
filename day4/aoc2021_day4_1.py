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
boardList=[]

for i in range (1, len(boards)):
    for j in range(len(boards[1])):
        board.append(boards[i][j].split())
    if i%5==0:
        print(board)
    #boardList.append(board)

#print(boards)
lastBoard=[ ['23', '61', '97', '1', '69' ],
            ['53', '98', '28', '52', '19'],
            ['66', '51', '46', '77', '15'],
            ['34', '36', '47', '80', '14'],
            ['7', '89', '62',  '9',  '49'] ]

#boardList.append(lastBoard)
#print(boardList)
#print(boardList[0])
#print(testBoard)
#isBingo=checkHorizontalBingo(testBoard)
#print(isBingo)
