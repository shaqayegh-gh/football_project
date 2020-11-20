import logging
from robots import *


class Team (Ball,Robot):
    def __init__(self,color):
        super(Team, self).__init__()
        self.color = color  # set the color of the team
        self.goal = 0   # count of the team's scores

        self.halfback1 = Halfback1(self.color)  # set 4 players for team
        self.halfback2 = Halfback2(self.color)
        self.forward = Forward(self.color)
        self.goaler = Goaler(self.color)

        self.list_robots=[self.halfback1,self.halfback2,self.forward,self.goaler]

        self.halfback1.manage()      # add the players to the field
        self.halfback2.manage()
        self.forward.manage()
        self.goaler.manage()



    def Calculate_goal(self):
        # Calculate team goals
        if self.color == "red":
            if 900 <= self.ball_pos[0] <= 930 & 240 <= self.ball_pos[1] <= 390:
                self.goal += 1
                logging.basicConfig(filename='footbaler_robot_log.log', format='%(asctime)s %(message)s')
                logging.info('The red team scored a goal')
                self.full_pos = [(10.5 * 30, 3.5 * 30), (20.5 * 30, 3.5 * 30), (10.5 * 30, 17.5 * 30),
                            (20.5 * 30, 17.5 * 30),
                            (18.5 * 30, 10.5 * 30), (12.5 * 30, 10.5 * 30), (45, 10.5 * 30),
                            (29.5 * 30, 10.5 * 30)]

        if self.color == "blue":
            if 0 <= self.ball_pos[0] <= 30 & 240 <= self.ball_pos[1] <= 390:
                self.goal += 1
                logging.basicConfig(filename='footbaler_robot_log.log', filemode='w', format='%(asctime)s %(message)s')
                logging.info("The blue team scored a goal")
                self.full_pos = [(10.5 * 30, 3.5 * 30), (20.5 * 30, 3.5 * 30), (10.5 * 30, 17.5 * 30),
                            (20.5 * 30, 17.5 * 30),
                            (18.5 * 30, 10.5 * 30), (12.5 * 30, 10.5 * 30), (45, 10.5 * 30),
                            (29.5 * 30, 10.5 * 30)]


