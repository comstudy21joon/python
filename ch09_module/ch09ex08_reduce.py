from functools import reduce

def sum(x, y) :
    return x+y

#lis2 =  [x for x in range(1,11)]
lis2 = list(range(1,11))
print(lis2)

total = reduce(sum, lis2)

print("total =>", total)