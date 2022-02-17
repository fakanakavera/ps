import random


class Check():
    def __init__(self):
        self.aa = random.randint(0,100)
    
    def c(self):
        if self.c == 9:
            return 0

    def check(self):
        print(self.t)

class Table(Check):
    def __init__(self):
        Check.__init__(self)
        self.t = random.randint(0,10)

t = Table()
t.t = 888
t.a = Table()
t.a.t = 99999

t.check()