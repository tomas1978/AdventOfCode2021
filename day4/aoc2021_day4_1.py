#answer:

f = open('input.txt','r')
#bingoData = f.readlines()
continueRead=True
lineConter=0
drawnNumbers=[]
while continueRead:
    line=f.readline()
    if lineConter==0:
        drawnNumbers.append(line)
    lineConter+=1
    if not line:
        continueRead=False

print(drawnNumbers)
