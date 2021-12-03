#answer:2972336

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
gamma=['0','0','0','0','0','0','0','0','0','0','0','0']
epsilon=['0','0','0','0','0','0','0','0','0','0','0','0']

for position in range(len(diagnostic[0])-1):
    for row in range(len(diagnostic)-1):
        if diagnostic[row][position]=='0':
            zeros+=1
        else:
            ones+=1
    if ones>zeros:
        gamma[position]='1'
    else:
        gamma[position]='0'
    zeros=0
    ones=0

for i in range(len(gamma)):
    if(gamma[i]=='0'):
        epsilon[i]='1'

gammaDecimal=convertBinArrayToInt(gamma)
epsilonDecimal=convertBinArrayToInt(epsilon)

print("Power consumption: ",gammaDecimal*epsilonDecimal)
