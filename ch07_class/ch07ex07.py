class Washer:
    def __init__(self, size, maker):
        self.size = size
        self.maker = maker

    def washing(self):
        print("{}세탁기가 {}킬로의 빨래를 한다~".format(self.maker, self.size))

    def __str__(self):
        return "size:{}, maker:{}".format(self.size, self.maker)
# end of Washer class


class SamsungWasher(Washer):
    def __init__(self, size, maker, name):
        super().__init__(size, maker)
        self.name = name

    def info(self):
        print("크기:", self.size)
        print("회사:", self.maker)
        print("상품명:", self.name)

    def __str__(self):
        return super().__str__() + ", name:{}".format(self.name)


samsungWasher = SamsungWasher(10, "Samgsung", "그랑데")
print(samsungWasher)
samsungWasher.washing()