
class Calc :
    def __init__(self, num):
        self.result = num

    def add(self, num):
        self.result += num

    def sub(self, num):
        self.result -= num

    def mult(self, num):
        self.result *= num

    def div(self, num):
        self.result /= num

    def getResult(self):
        return self.result
