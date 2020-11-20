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


        self.show_goals(45,"red",self.goal)  # show the number of the goals for red team
        self.show_goals(29.5*30,"blue",self.goal)  # show the number of the goals for blue team

    def calculate_goal(self):
        # Calculate team goals
        if self.color == "red":
            if  self.ball_pos==(30.5*30,10.5*30) :
                self.goal += 1
                self.remove_gaols_showing(self.color)
                self.show_goals(45,self.color,self.goal)
                logging.basicConfig(filename='Robot_footballer.log', level=logging.INFO,
                                    format='%(asctime)s _ %(levelname)s _ %(message)s')
                logging.info('The red team scored a goal')
                for robot in self.list_robots:
                    if isinstance(robot, Halfback1):
                        if robot.color == "red":
                            robot.new_pos = (10.5 * 30, 3.5 * 30)
                        if robot.color == "blue":
                            robot.new_pos = (20.5 * 30, 3.5 * 30)
                    elif isinstance(robot, Halfback2):
                        if robot.color == "red":
                            robot.new_pos = (10.5 * 30, 17.5 * 30)
                        if robot.color == "blue":
                            robot.new_pos = (20.5 * 30, 17.5 * 30)
                    elif isinstance(robot, Forward):
                        if robot.color == "red":
                            robot.new_pos = (18.5 * 30, 10.5 * 30)
                        if robot.color == "blue":
                            robot.new_pos = (12.5 * 30, 10.5 * 30)
                    elif isinstance(robot, Goaler):
                        if robot.color == "red":
                            robot.new_pos = (45, 10.5 * 30)
                        if robot.color == "blue":
                            robot.new_pos = (12.5 * 30, 10.5 * 30)

                self.scored_message(self.color)    #show the gaol message

                return True
            else:
                return False



        if self.color == "blue":
            if self.ball_pos==(15,10.5*30):
                self.goal += 1
                self.remove_gaols_showing(self.color)
                self.show_goals(29.5 * 30, self.color, self.goal)
                logging.basicConfig(filename='Robot_footballer.log', level=logging.INFO,
                                    format='%(asctime)s _ %(levelname)s _ %(message)s')
                logging.info('The blue team scored a goal')
                for robot in self.list_robots:
                    if isinstance(robot, Halfback1):
                        if robot.color == "red":
                            robot.new_pos = (10.5 * 30, 3.5 * 30)
                        if robot.color == "blue":
                            robot.new_pos = (20.5 * 30, 3.5 * 30)
                    elif isinstance(robot, Halfback2):
                        if robot.color == "red":
                            robot.new_pos = (10.5 * 30, 17.5 * 30)
                        if robot.color == "blue":
                            robot.new_pos = (20.5 * 30, 17.5 * 30)
                    elif isinstance(robot, Forward):
                        if robot.color == "red":
                            robot.new_pos = (18.5 * 30, 10.5 * 30)
                        if robot.color == "blue":
                            robot.new_pos = (12.5 * 30, 10.5 * 30)
                    elif isinstance(robot, Goaler):
                        if robot.color == "red":
                            robot.new_pos = (45, 10.5 * 30)
                        if robot.color == "blue":
                            robot.new_pos = (12.5 * 30, 10.5 * 30)

                self.scored_message(self.color)    #show the gaol message

                return True
            else:
                return False






