class Washer:
    def __init__(self, size, maker):
        self.size = size
        self.maker = maker

    def washing(self):
        detergent()
        print("{}세탁기가 {}킬로의 빨래를 한다~".format(self.maker, self.size))

# end of Washer class

def detergent():
    print("세제 투입!")


washer = Washer(10, "LG")
washer.washing()