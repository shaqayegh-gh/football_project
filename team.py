import logging
from robots import *


class Team( Robot):
    def __init__(self, color):
        # super(Ball).__init__()
        self.color = color  # set the color of the team
        self.halfback1 = Halfback1(self.color)  # set 4 players for team
        self.halfback2 = Halfback2(self.color)
        self.forward = Forward(self.color)
        self.goaler = Goaler(self.color)
        self.list_robots = [self.halfback1, self.halfback2, self.forward, self.goaler]
        self.halfback1.manage()  # add the players to the field
        self.halfback2.manage()
        self.forward.manage()
        self.goaler.manage()

        self.goal = 0



    def Calculate_goal(self,ball_position):
        # Calculate team goals
        if self.color == "red":
            if 900 <= ball_position[0]<= 930 & 240 <= ball_position[1] <= 390:
                self.goal += 1
                logging.basicConfig(filename='footbaler_robot_log.log', format='%(asctime)s %(message)s')
                logging.info('The red team scored a goal')
                self.full_pos = [(10.5 * 30, 3.5 * 30), (20.5 * 30, 3.5 * 30), (10.5 * 30, 17.5 * 30),
                                 (20.5 * 30, 17.5 * 30),
                                 (18.5 * 30, 10.5 * 30), (12.5 * 30, 10.5 * 30), (45, 10.5 * 30),
                                 (29.5 * 30, 10.5 * 30)]

        if self.color == "blue":
            if 0 <= ball_position[0]<= 30 & 240 <= ball_position[1] <= 390:
                self.goal += 1
                logging.basicConfig(filename='footbaler_robot_log.log', filemode='w', format='%(asctime)s %(message)s')
                logging.info("The blue team scored a goal")
                self.full_pos = [(10.5 * 30, 3.5 * 30), (20.5 * 30, 3.5 * 30), (10.5 * 30, 17.5 * 30),
                                 (20.5 * 30, 17.5 * 30),
                                 (18.5 * 30, 10.5 * 30), (12.5 * 30, 10.5 * 30), (45, 10.5 * 30),
                                 (29.5 * 30, 10.5 * 30)]

    def team_move(self):
        # Move the rebels of a team
        for robot in self.list_robots:
            robot.move_robot()
            if 30 <= hypot(robot.new_pos[0] - self.ball_pos[0], robot.new_pos[1] - self.ball_pos[1]) <= sqrt(2) * 30:
                self.shoot()

            robot.charge -= 1
            if robot.charge <= 0:
                self.list_robots.remove(robot)
                logging.basicConfig(filename='footbaler_ball_log.log', filemode='w', format='%(asctime)s %(message)s')
                logging.info("A robot was removed")
