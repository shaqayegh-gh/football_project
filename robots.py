import random

from field import *
from ball import *
import time
from math import hypot,sqrt

######################  Robot class  ###################

class Robot(Field):
    moves = [(0, -30), (0, 30), (-30, 0), (30, 0)]  # the moves which the players can have

    def __init__(self):
        self.charge = random.randint(1,2)  # get a random charge to the player



    def move_robot(self):
        if self.charge>0:
            self.direction = random.choice(self.moves)
            while ((self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]) in self.full_pos) or (self.pos[0] +self.direction[0]) < 15 or (self.pos[0] + self.direction[0]) > (30.5 * 30) or (self.pos[1] + \
                    self.direction[1]) < 15 or (self.pos[1] + self.direction[1]) > (20.5 * 30):     # check if the selected pos is empty and not going out the field
                self.direction = random.choice(self.moves)  # if the selected pos is full then select another direction

            self.player.move(self.direction[0], self.direction[1])  # move the player into the new pos based on direction
            self.new_pos = (self.player.getCenter().x, self.player.getCenter().y)



            self.full_pos.remove(self.pos)
            self.full_pos.append(self.new_pos)
            self.pos = self.new_pos
            self.charge-=1
        else:
            self.player.undraw()
            left_message=Text(Point(15.5*30,21.5*30),"the {0} team player left the game".format(self.color))
            left_message.draw(self.win)
            time.sleep(3)
            left_message.undraw()

            def shoot(self):
                if self.color == "red":  # the red team should shoot to the right
                    self.shoot_power = (random.randrange(30, 4 * 30, 30), random.randrange(-60, 60, 30))
                elif self.color == "blue":  # the blue team should shoot to the left
                    self.shoot_power = (random.randrange(-30, -4 * 30, -30), random.randrange(-60, 60, 30))
                self.move_ball(self.shoot_power[0], self.shoot_power[1])


        

#########################  first Halfbacks classes ###############################

class Halfback1(Robot):  # the first halfback of the  team
    def __init__(self,color):
        Robot.__init__(self)
        self.color=color
        if self.color=="red":
            self.pos = (10.5 * 30, 3.5 * 30)  # the center of the circle for showing the player
        elif self.color=="blue":
            self.pos = (20.5 * 30, 3.5 * 30)

    def manage(self):  # set the first manage of the players in the field
        self.player = Circle(Point(self.pos[0], self.pos[1]), 10)
        self.player.setFill(color=self.color)
        self.add_item(self.player.draw(self.win))

####################### Second Halfbacks classes ###################################

class Halfback2(Halfback1):  # the second halfback of the team
    def __init__(self,color):
        Robot.__init__(self)
        self.color = color
        if color=="red":
            self.pos = (10.5 * 30, 17.5 * 30)
        elif color=="blue":
            self.pos = (20.5 * 30, 17.5 * 30)

#####################  Forwards classes ####################################

class Forward(Halfback1):  # the forward of the team
    def __init__(self,color):
        Robot.__init__(self)
        self.color = color
        if color == "red":
            self.pos = (18.5 * 30, 10.5 * 30)
        elif color=="blue":
            self.pos = (12.5 * 30, 10.5 * 30)

####################  Goalers classes ###################################

class Goaler(Halfback1):  # goaler of the  team
    red_goaler_pos = [(45, 8.5 * 30), (45, 9.5 * 30), (45, 10.5 * 30), (45, 11.5 * 30), (45, 12.5 * 30)]
    blue_goaler_pos = [(29.5 * 30, 8.5 * 30), (29.5 * 30, 9.5 * 30), (29.5 * 30, 10.5 * 30), (29.5 * 30, 11.5 * 30),
                  (29.5 * 30, 12.5 * 30)]

    def __init__(self,color):
        Robot.__init__(self)
        self.color = color
        if self.color=="red":
            self.pos = (45, 10.5 * 30)
            self.direction = random.choice(self.red_goaler_pos)
        elif self.color=="blue":
            self.pos = (29.5 * 30, 10.5 * 30)
            self.direction = random.choice(self.blue_goaler_pos)

    def move_robot(self):  # movement of the goalers is just along the length of the gates

        while (self.direction[0],self.direction[1]) in self.full_pos:
            if self.color == "red":
                self.direction = random.choice(self.red_goaler_pos)
            elif self.color=="blue":
                self.direction = random.choice(self.blue_goaler_pos)

        self.player.move(self.direction[0] - self.pos[0], self.direction[1] - self.pos[1])
        self.new_pos = (self.player.getCenter().x, self.player.getCenter().y)
        self.full_pos.remove(self.pos)
        self.full_pos.append(self.new_pos)
        self.pos = self.new_pos




