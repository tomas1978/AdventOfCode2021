#answer:
f = open('input.txt','r')
commands = f.readlines()
depth=0
horizontalPosition=0
aim=0
for i in range(len(commands)):
    space=commands[i].find(' ')
    command=commands[i][0:space]
    steps=commands[i][space:len(commands)]
    if command=="down":
        aim+=int(steps)
    if command=="up":
        aim-=int(steps)
    if command=="forward":
        horizontalPosition+=int(steps)
        depth+=aim*int(steps)

print(depth*horizontalPosition)
