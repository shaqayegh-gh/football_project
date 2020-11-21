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

        for robot in self.list_robots:  # add the players to the field
            robot.manage(robot.pos[0],robot.pos[1])


    def red_reset_arrenge(self,remain_robot_list):  # after a goal for red team ,the team arrenge resets
        for robot in remain_robot_list:
            if robot is self.halfback1:
                robot.move_robot2first(10.30*30,3.5*30)
            if robot is self.halfback2:
                robot.move_robot2first(10.5 * 30, 17.5 * 30)
            if robot is self.forward:
                robot.move_robot2first(18.5 * 30, 10.5 * 30)
            if robot is self.goaler:
                robot.move_robot2first(45, 10.5 * 30)


    def blue_reset_arrenge(self,remain_robot_list):   # after a goal for blue team ,the team arrenge resets
        for robot in remain_robot_list:
            if robot is self.halfback1:
                robot.move_robot2first(20.5 * 30, 3.5 * 30)
            if robot is self.halfback2:
                robot.move_robot2first(20.5 * 30, 17.5 * 30)
            if robot is self.forward:
                robot.move_robot2first(12.5 * 30, 10.5 * 30)
            if robot is self.goaler:
                robot.move_robot2first(29.5 * 30, 10.5 * 30)




    # Calculate team goals
    def calculate_goal(self,ball_x,ball_y,remain):

        if self.color == "red":
            if  ball_x ==30.5*30 and 8.5*30 <= ball_y <= 12.5*30:   # the position of ball for goal
                self.goal += 1

                logging.basicConfig(filename='Robot_footballer.log', level=logging.INFO,
                                    format='%(asctime)s _ %(levelname)s _ %(message)s')
                logging.info('The red team scored a goal')

                self.scored_message(self.color)    #show the gaol message
                self.red_reset_arrenge(remain)

                return True
            else:
                return False

        elif self.color == "blue":
            if ball_x == 15 and 8.5 * 30 <= ball_y <= 12.5 * 30:   # the position of ball for goal
                self.goal += 1

                logging.basicConfig(filename='Robot_footballer.log', level=logging.INFO,
                                    format='%(asctime)s _ %(levelname)s _ %(message)s')
                logging.info('The blue team scored a goal')

                self.scored_message(self.color)    #show the gaol message
                self.blue_reset_arrenge(remain)

                return True
            else:
                return False



