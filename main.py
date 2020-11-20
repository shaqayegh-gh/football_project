from team import *
from ball import *
from field import *
from math import hypot,sqrt


class Game():
    def __init__(self):
        self.game_field=Field()    # making the field of the game
        self.game_ball = Ball()    # making the ball of the game
        self.game_ball.manage()    # add tha ball to the field

        self.blue_team = Team("blue")   # making blue team
        self.red_team = Team("red")     # making red team

        self.game_field.start_game_sign()   # show the start message


        while True:
            for team in [self.blue_team,self.red_team]:
                for robot in team.list_robots:
                    robot.move_robot()      # move the robot in game

                    if robot.charge <= 0:      # check the charge of the robot
                        robot.move_robot()
                        team.list_robots.remove(robot)
                        logging.basicConfig(filename='footbaler_ball_log.log', filemode='w', format='%(asctime)s %(message)s')
                        logging.info("A robot was removed")

                    # check the distance of the robot and ball
                    if abs(robot.pos[0] - self.game_ball.ball_pos[0])==30 and robot.pos[1] == self.game_ball.ball_pos[1]:
                        time.sleep(.07)
                        self.game_ball.move_ball(robot.shoot()[0], robot.shoot()[1])

                    elif abs(robot.pos[1] - self.game_ball.ball_pos[1]) == 30 and robot.pos[0] == self.game_ball.ball_pos[0]:
                        time.sleep(.07)
                        self.game_ball.move_ball(robot.shoot()[0], robot.shoot()[1])

                    elif hypot(robot.pos[0] - self.game_ball.ball_pos[0], robot.pos[1] - self.game_ball.ball_pos[1]) == sqrt(2) * 30:
                        time.sleep(.07)
                        self.game_ball.move_ball(robot.shoot()[0], robot.shoot()[1])

                    else:
                        time.sleep(.07)

        self.game_field.win.getMouse()


game1=Game()


