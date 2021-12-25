f = open('input.txt','r')
ventLines = f.readlines()
lineList=[]
startPoints=[]
endPoints=[]
for line in range(len(ventLines)-1):
    arrowIndex=ventLines[line].find("->")
    startPoint=ventLines[line][0:arrowIndex]
    startPoints.append(startPoint)
    endPoint=ventLines[line][arrowIndex:len(ventLines[line])]
    endPoints.append(startPoints)

print(startPoints)
