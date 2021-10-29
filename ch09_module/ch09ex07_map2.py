def mult(i) :
    return i *  100

lis = [10, 20, 30, 40]

result = map(mult, lis)

# for item in result :
#     print(item, end=" ")


while True :
    try :
        element = result.__next__()
        print(element)
    except:
        break


