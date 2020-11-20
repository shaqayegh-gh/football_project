from graphics import *
from field import *
class Ball(Field):

    def __init__(self):
        self.ball_pos=(465,315)
        self.ball=Circle(Point(self.ball_pos[0],self.ball_pos[1]),10)
        self.ball.setFill(color="white")

    def manage(self):
        self.add_item(self.ball.draw(self.win))


    def move_ball(self,x,y):
        self.ball.move(x,y)
        self.ball_new_pos=(self.ball.getCenter().x,self.ball.getCenter().y)
        self.full_pos.remove(self.ball_pos)
        self.full_pos.append(self.ball_new_pos)
        self.ball_pos=self.ball_new_pos

