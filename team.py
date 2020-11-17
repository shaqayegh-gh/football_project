from robots import *


class Team():
    def __init__(self,color):
        self.color=color
        self.halfback1=Halfback1(self.color)
        self.halfback2=Halfback2(self.color)
        self.forward=Forward(self.color)
        self.goaler=Goaler(self.color)
