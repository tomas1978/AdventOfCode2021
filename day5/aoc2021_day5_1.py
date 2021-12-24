f = open('input.txt','r')
ventLines = f.readlines()
lineList=[]
for line in range(len(ventLines)-1):
    lineList.append(line)

print(lineList[2])
