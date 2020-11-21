from field import *


class Ball(Field):

    def __init__(self):
        self.ball_pos = (465, 315)
        self.ball = Circle(Point(self.ball_pos[0], self.ball_pos[1]), 10)
        self.ball.setFill(color="white")

    def manage(self):
        self.add_item(self.ball.draw(self.win))

    def move_ball(self, x, y):
        if (x, y) in self.full_pos:
            x -= 30
        self.ball.move(x, y)
        self.ball_new_pos = (self.ball.getCenter().x, self.ball.getCenter().y)
        if self.ball_pos in self.full_pos:
            try:
                self.full_pos.remove(self.ball_pos)
                self.full_pos.append(self.ball_new_pos)
                self.ball_pos = self.ball_new_pos
            except ValueError:
                self.full_pos.append(self.ball_new_pos)


    # reset ball position and bring it to the center of field after a goal
    def reset(self):
        self.ball_pos = [15.5 * 30, 10.5 * 30]
