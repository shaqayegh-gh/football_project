import logging

from robots import *


class Team(Ball, Robot,Field):
    tyep_class = ["Halfback1", "Halfback2", "Forward"]
    red_pos = [(10.5 * 30, 3.5 * 30), (10.5 * 30, 17.5 * 30), (18.5 * 30, 10.5 * 30)]
    blue_pos = [(20.5 * 30, 3.5 * 30), (20.5 * 30, 17.5 * 30), (12.5 * 30, 10.5 * 30)]

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
                print("golered")
                for robot in self.list_robots:
                    if robot.__dir__()=="Goaler":
                        self.list_robots.remove(robot)
                logging.basicConfig(filename='Robot_footballer.log', level=logging.INFO,
                                    format='%(asctime)s _ %(levelname)s _ %(message)s')
                logging.info('The red team scored a goal')

                for robot in self.list_robots:
                    # Reset the position of the players after the team scores. Based on team color and
                    # (Halfback1,Halfback2,Forward,Goaler)
                    for type, red_position,blue_position in zip(Team.tyep_class, Team.red_pos, Team.blue_pos):
                        if robot.__dir__() == type and robot.color == "red":
                            try:
                                robot.move_robot(red_position[0],red_position[1])
                                # index = self.full_pos.index(robot.pos)
                                # self.full_pos.insert(index, red_position)
                                # robot.pos=red_position
                                # robot.move(red_position[0],red_position[1])
                                print("1",robot.pos)


                            except ValueError:

                                # self.full_pos.append(red_position)
                                # robot.pos = red_position
                                robot.move_robot(red_position[0], red_position[1])
                                print("2",robot.pos)



                        elif robot.__dir__() == type and robot.color == "blue":
                            try:
                                # index = self.full_pos.index(robot.pos)
                                # self.full_pos.insert(index, blue_position)
                                # robot.pos=blue_position
                                robot.move_robot(blue_position[0], blue_position[1])
                                print("3",robot.pos)



                            except ValueError:
                                # self.full_pos.append(blue_position)
                                # robot.pos = blue_position
                                robot.move_robot(blue_position[0], blue_position[1])
                                print("4",robot.pos)

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
                    for type, red_position, blue_position in zip(Team.tyep_class, Team.red_pos, Team.blue_pos):
                        if robot.__dir__() == type and robot.color == "red":
                            try:
                                # index = self.full_pos.index(robot.pos)
                                # self.full_pos.insert(index, red_position)
                                # robot.pos = red_position
                                robot.move_robot(red_position[0], red_position[1])
                                print("5",robot.pos)

                            except ValueError:
                                # self.full_pos.append(red_position)
                                # robot.pos = red_position
                                robot.move_robot(red_position[0],red_position[1])
                                print("6",robot.pos)

                        elif robot.__dir__() == type and robot.color == "blue":
                            try:
                                # index = self.full_pos.index(robot.pos)
                                # self.full_pos.insert(index, blue_position)
                                # robot.pos = blue_position
                                robot.move_robot(blue_position[0], blue_position[1])
                                print("7",robot.pos)

                            except ValueError:
                                # self.full_pos.append(blue_position)
                                # robot.pos = blue_position
                                robot.move_robot(blue_position[0], blue_position[1])
                                print("8",robot.pos)

                return True
            else:
                return False
