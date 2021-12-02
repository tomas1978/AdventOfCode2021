#answer: 2215080
f = open('input.txt','r')
commands = f.readlines()
depth=0
horizontalPosition=0
for i in range(len(commands)):
    space=commands[i].find(' ')
    command=commands[i][0:space]
    steps=commands[i][space:len(commands)]
    if command=="down":
        depth+=int(steps)
    if command=="up":
        depth-=int(steps)
    if command=="forward":
        horizontalPosition+=int(steps)

print(depth*horizontalPosition)

