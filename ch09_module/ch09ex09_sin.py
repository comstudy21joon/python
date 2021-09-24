import math

for i in range(1,60):
    print(math.floor((math.sin(i/10)*100) ), end=" ")
    if(i%20 == 0) : print()
