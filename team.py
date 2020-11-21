import logging
from time import sleep

from robots import *


class Team(Ball, Robot):
    tyep_class = ["Halfback1", "Halfback2", "Forward", "Goaler"]
    red_pos = [(10.5 * 30, 3.5 * 30), (10.5 * 30, 17.5 * 30), (18.5 * 30, 10.5 * 30), (45, 10.5 * 30)]
    blue_pos = [(20.5 * 30, 3.5 * 30), (20.5 * 30, 17.5 * 30), (12.5 * 30, 10.5 * 30), (29.5 * 30, 10.5 * 30)]
    i=3

    def __init__(self, color):
        super(Team, self).__init__()
        self.color = color  # set the color of the team
        self.goal = 0  # count of the team's scores

        self.halfback1 = Halfback1(self.color)  # set 4 players for team
        self.halfback2 = Halfback2(self.color)
        self.forward = Forward(self.color)
        self.goaler = Goaler(self.color)

        self.list_robots = [self.halfback1, self.halfback2, self.forward, self.goaler]

        self.halfback1.manage()  # add the players to the field
        self.halfback2.manage()
        self.forward.manage()
        self.goaler.manage()

    def calculate_goal(self, ball_X, ball_Y):
        # Calculate team goals
        if self.color == "red":

            if ball_X == 30.5 * 30 and 8.5 * 30 <= ball_Y <= 12.5 * 30:
                # The red team scored a goal
                self.goal += 1
                logging.basicConfig(filename='Robot_footballer.log', level=logging.INFO,
                                    format='%(asctime)s _ %(levelname)s _ %(message)s')
                logging.info('The red team scored a goal')

                for robot in self.list_robots:
                    # Reset the position of the players after the team scores. Based on team color and
                    # (Halfback1,Halfback2,Forward,Goaler)
                    for type, red,blue in zip(self.tyep_class, self.red_pos, self.blue_pos):
                        sleep(self.i)
                        if robot.__dir__() == type and robot.color == "red":
                            try:
                                robot.new_pos = (45, 10.5 * 30)
                                index = self.full_pos.index(robot.pos)
                                self.full_pos.insert(index, red)

                            except ValueError:
                                self.full_pos.append(red)

                        elif robot.__dir__() == type and robot.color == "blue":
                            try:
                                index = self.full_pos.index(robot.pos)
                                self.full_pos.insert(index, blue)

                            except ValueError:
                                self.full_pos.append(blue)
                        self.i-=0.5

                    return True

                else:
                    return False
        if self.color == "blue":
            if ball_X == 15.5 * 30 and 8.5 * 30 < ball_Y <= 12.5 * 30:
                # The blue team scored a goal
                logging.basicConfig(filename='Robot_footballer.log', level=logging.INFO,
                                    format='%(asctime)s _ %(levelname)s _ %(message)s')
                logging.info('The blue team scored a goal')
                self.goal += 1
                for robot in self.list_robots:
                    # Reset the position of the players after the team scores. Based on team color and(Halfback1,Halfback2,Forward,Goaler)
                    for type, red, blue in zip(self.tyep_class, self.red_pos, self.blue_pos):
                        if robot.__dir__() == type and robot.color == "red":
                            try:
                                robot.new_pos = (45, 10.5 * 30)
                                index = self.full_pos.index(robot.pos)
                                self.full_pos.insert(index, red)

                            except ValueError:
                                self.full_pos.append(red)

                        elif robot.__dir__() == type and robot.color == "blue":
                            try:
                                index = self.full_pos.index(robot.pos)
                                self.full_pos.insert(index, blue)

                            except ValueError:
                                self.full_pos.append(blue)


                return True
            else:
                return False
