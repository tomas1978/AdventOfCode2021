#answer:

def convertBinArrayToInt(binArray):
    decNumber=0
    for i in range(len(binArray)):
        if binArray[i]=='1':
            decNumber+=2**(len(binArray)-1-i)
    return decNumber

f = open('input.txt','r')
diagnostic = f.readlines()
zeros=0
ones=0
oxygenGenerator=['0','0','0','0','0','0','0','0','0','0','0','0']
co2Scrubber=['0','0','0','0','0','0','0','0','0','0','0','0']
keepNumbers=[]

for position in range(len(diagnostic[0])-1):
    for row in range(len(diagnostic)-1):
        if diagnostic[row][position]=='0':
            zeros+=1
        else:
            ones+=1
    if ones>=zeros:
        mostCommon=1
    else:
        mostCommon=0
    zeros=0
    ones=0
