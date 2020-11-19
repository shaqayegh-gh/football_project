import logging
from robot_980828 import Robot
from ball import Ball


class Team(Robot, Ball):

    """
    Calculate team goals and Move the rebels of a team
    Atribut:list_robot,color, goal number
    """

    def __init__(self, *list_robots, color):
        super(Robot, self).__init__()
        self.list_robots = list_robots
        self.color = color
        self.goal = 0
        if self.color=="red":
            self.direction="left"
        else:
            self.direction="right"
    def Calculate_goal(self):
        # Calculate team goals
        if self.color == "red":
            if 900 <= self.ball_pas[0] <= 930 & 240 <= self.ball_pas[1] <= 390:
                self.goal += 1
                logging.basicConfig(filename='footbaler_robot_log.log', format='%(asctime)s %(message)s')
                logging.info('The red team scored a goal')
                self.full_pos["red"] = [(10.5 * 30, 3.5 * 30), (20.5 * 30, 3.5 * 30), (10.5 * 30, 17.5 * 30),
                                        (20.5 * 30, 17.5 * 30)]

        if self.color == "blue":
            if 0 <= self.ball_pas[0] <= 30 & 240 <= self.ball_pas[1] <= 390:
                self.goal += 1
                logging.basicConfig(filename='footbaler_robot_log.log', filemode='w', format='%(asctime)s %(message)s')
                logging.info("The blue team scored a goal")
                self.full_pos["blue"] = [(18.5 * 30, 10.5 * 30), (12.5 * 30, 10.5 * 30), (45, 10.5 * 30),
                                         (29.5 * 30, 10.5 * 30)]

    def move_team(self):
        # Move the rebels of a team
        for robot in self.list_robots:
            robot.move_robot()
            self.charge -= 40
            if self.charge < 40:
                self.list_robots.remove(robot)
                logging.basicConfig(filename='footbaler_ball_log.log', filemode='w', format='%(asctime)s %(message)s')
                logging.info("A robot was removed")
