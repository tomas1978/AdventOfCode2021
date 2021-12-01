#answer: 1167
f = open('input.txt','r')
depths = f.readlines()
increases=0
for i in range(len(depths)-1):
    if int(depths[i+1])>int(depths[i]):
        increases+=1
print("Number of increases",increases)
