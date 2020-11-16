import numpy as np
import matplotlib.pyplot as plt
import random
from graphics import *


class Field:
    full_pos = [ (10.5 * 30, 3.5 * 30), (20.5 * 30, 3.5 * 30), (10.5 * 30, 17.5 * 30), (20.5 * 30, 17.5 * 30),
                (18.5 * 30, 10.5 * 30), (12.5 * 30, 10.5 * 30), (45, 10.5 * 30),
                (29.5 * 30, 10.5 * 30)]  # newest positions of the players in the field

    win = GraphWin("Soccer Game", 930,
                   630)  # open a drawing window named Soccer Game with a width of 930 and length of 630
    win.setBackground(color="green")

    def __init__(self):
        for i in range(0, 930,
                       30):  # drawing a checkered page (930=31*30) --> 31:block in width of field   30: the width of each block
            for j in range(0, 630, 30):  # (630=21*30) --> 21:block in length of the field  30 :the width of each block
                rectangle = Rectangle(Point(i, j), Point(i + 30, j + 30))
                rectangle.setOutline(color="black")
                rectangle.setWidth(1.4)
                rectangle.draw(self.win)

        gate1 = Rectangle(Point(0, 240), Point(30, 390))  # drawing two rectangle for the gates
        gate1.setFill(color="red")
        gate2 = Rectangle(Point(900, 240), Point(930, 390))
        gate2.setFill(color="blue")
        gate1.draw(self.win)
        gate2.draw(self.win)

    @classmethod
    def add_item(cls, func):  # add new object like the players sign(circle) into the drawing window(win)
        # cls.win.flush()
        cls.win.addItem(func)
        cls.win.getMouse()


######################  Robot class  ###################

class Robot(Field):
    moves = [(0, -30), (0, 30), (-30, 0), (30, 0)]  # the moves which the players can have

    def __init__(self):
        self.charge = random.randint(250, 500)  # get a random charge to the player


    def move_robot(self):
        self.direction = random.choice(self.moves)
        while ((self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]) in self.full_pos) or (self.pos[0] +self.direction[0]) < 15 or (self.pos[0] + self.direction[0]) > (30.5 * 30) or (self.pos[1] + \
                self.direction[1]) < 15 or (self.pos[1] + self.direction[1]) > (20.5 * 30):     # check if the selected pos is empty and not going out the field
            self.direction = random.choice(self.moves)  # if the selected pos is full then select another direction

        self.player.move(self.direction[0], self.direction[1])  # move the player into the new pos based on direction
        self.new_pos = (self.player.getCenter().x, self.player.getCenter().y)
        self.full_pos.remove(self.pos)
        self.full_pos.append(self.new_pos)
        self.pos = self.new_pos
        self.win.getMouse()

    def shoot(self):
        pass


#########################  first Halfbacks classes ###############################

class Halfback1_1(Robot):  # the first halfback of the first team
    def __init__(self):
        Robot.__init__(self)
        self.pos = (10.5 * 30, 3.5 * 30)  # the center of the circle for showing the player

    def manage(self, color="red"):  # set the first manage of the players in the field
        self.player = Circle(Point(self.pos[0], self.pos[1]), 10)
        self.player.setFill(color=color)
        self.add_item(self.player.draw(self.win))


class Halfback1_2(Halfback1_1):  # the first halfback of the second team
    def __init__(self):
        Halfback1_1.__init__(self)
        self.pos = (20.5 * 30, 3.5 * 30)

    def manage(self):
        super(Halfback1_2, self).manage(color="blue")


####################### Second Halfbacks classes ###################################

class Halfback2_1(Halfback1_1):  # the second halfback of the first team
    def __init__(self):
        Robot.__init__(self)
        self.pos = (10.5 * 30, 17.5 * 30)


class Halfback2_2(Halfback1_1):  # the second halfback of the second team
    def __init__(self):
        Halfback1_1.__init__(self)
        self.pos = (20.5 * 30, 17.5 * 30)

    def manage(self):
        super(Halfback2_2, self).manage(color="blue")


#####################  Forwards classes ####################################

class Forward_1(Halfback1_1):  # the forward of the first team
    def __init__(self):
        Robot.__init__(self)
        self.pos = (18.5 * 30, 10.5 * 30)


class Forward_2(Halfback1_1):  # the forward of the second team
    def __init__(self):
        Halfback1_1.__init__(self)
        self.pos = (12.5 * 30, 10.5 * 30)

    def manage(self):
        super(Forward_2, self).manage(color="blue")


####################  Goalers classes ###################################

class Goaler_1(Halfback1_1):  # goaler of the first team
    goaler_pos = [(45, 8.5 * 30), (45, 9.5 * 30), (45, 10.5 * 30), (45, 11.5 * 30), (45, 12.5 * 30)]

    def __init__(self):
        Robot.__init__(self)
        self.pos = (45, 10.5 * 30)
        self.direction = random.choice(self.goaler_pos)

    def move_robot(self):  # movement of the goalers is just along the length of the gates

        while (self.direction[0],self.direction[1]) in self.full_pos:
            self.direction = random.choice(self.goaler_pos)

        self.player.move(self.direction[0] - self.pos[0], self.direction[1] - self.pos[1])
        self.new_pos = (self.player.getCenter().x, self.player.getCenter().y)
        self.full_pos.remove(self.pos)
        self.full_pos.append(self.new_pos)
        self.pos = self.new_pos
        self.win.getMouse()


class Goaler_2(Goaler_1):  # goaler of the second team
    goaler_pos = [(29.5 * 30, 8.5 * 30), (29.5 * 30, 9.5 * 30), (29.5 * 30, 10.5 * 30), (29.5 * 30, 11.5 * 30),
                  (29.5 * 30, 12.5 * 30)]

    def __init__(self):
        Robot.__init__(self)
        self.pos = (29.5 * 30, 10.5 * 30)
        self.direction = random.choice(self.goaler_pos)

    def manage(self):
        super(Goaler_2, self).manage(color="blue")
