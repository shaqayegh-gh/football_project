from field import *
import random
class Ball(Field):

    def __init__(self):
        self.ball_pos=(465,315)    
        self.ball=Circle(Point(self.ball_pos[0],self.ball_pos[1]),10)   #draw a white circle for ball on the window
        self.ball.setFill(color="white")

    def manage(self):  # set the ball in the field
        self.add_item(self.ball.draw(self.win))


    def move_ball(self,x,y):     
        while (self.ball_pos[0]+x,self.ball_pos[1]+y) in self.full_pos:
            x+=random.choice([30,-30])
        self.ball.move(x,y)   
        self.ball_new_pos=(self.ball.getCenter().x,self.ball.getCenter().y)
        self.full_pos.remove(self.ball_pos)
        self.full_pos.append(self.ball_new_pos)
        self.ball_pos=self.ball_new_pos
        return self.ball_pos

    def ball_reset(self):    # move ball to the center of field after a goal
        self.ball.move(465-self.ball_pos[0],315-self.ball_pos[1])
        self.ball_new_pos = (self.ball.getCenter().x, self.ball.getCenter().y)
        self.full_pos.remove(self.ball_pos)
        self.full_pos.append(self.ball_new_pos)
        self.ball_pos = self.ball_new_pos


