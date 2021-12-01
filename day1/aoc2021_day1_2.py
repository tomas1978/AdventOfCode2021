#answer: 1130
f = open('input.txt','r')
depths = f.readlines()
increases=0
for i in range(len(depths)-3):
    sum1=int(depths[i])+int(depths[i+1])+int(depths[i+2])
    sum2=int(depths[i+1])+int(depths[i+2])+int(depths[i+3])
    if sum2>sum1:
        increases+=1
print("Number of increases",increases)
