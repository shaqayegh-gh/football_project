from team import *
from ball import *
from field import *
from math import hypot, sqrt


class Game():
    def __init__(self):
        self.game_field = Field()  # making the field of the game
        self.game_ball = Ball()  # making the ball of the game
        self.game_ball.manage()  # add tha ball to the field

        self.blue_team = Team("blue")  # making blue team
        self.red_team = Team("red")  # making red team

        self.game_field.start_game_sign()  # show the start message

    def check_charges(self):  #check the charge of all robots to specify the end of the game
        if self.blue_team.halfback1.charge > 0 or self.blue_team.halfback2.charge > 0 or \
                self.blue_team.forward.charge > 0 or self.red_team.halfback1.charge > 0 or \
                self.red_team.halfback2.charge > 0 or self.red_team.forward.charge > 0:
            return True
        else:
            return False

    @staticmethod
    def delay(num_of_players):    # set dalay for game
        time.sleep(float(8 / num_of_players / 50))


    def start_game(self):
        self.game_field.show_goals(45, "red", self.red_team.goal)  # show the number of the goals for red team
        self.game_field.show_goals(29.5 * 30, "blue", self.blue_team.goal)  # show the number of the goals for blue team
        self.num_of_players = 8     # counts the the number of uncharged robots

        while self.check_charges() :   # the game will end with all robots uncharging except the goalers
            for team in [self.blue_team,self.red_team]:
                for robot in team.list_robots:
                    if robot is not (self.blue_team.goaler and  self.red_team.goaler):
                        robot.move_robot()  # move the robot in game

                        if robot.charge <= 0:  # check the charge of the robot
                            robot.move_robot()
                            team.list_robots.remove(robot)
                            self.num_of_players-=1
                            logging.basicConfig(filename='Robot_footballer.log', level=logging.INFO,
                                                format='%(asctime)s _ %(levelname)s _ %(message)s')
                            logging.info('A robot was removed')

                        # check the distance of the robot and ball on x line
                        if abs(robot.pos[0] - self.game_ball.ball_pos[0]) == 30 and robot.pos[1] == self.game_ball.ball_pos[1]:
                            self.delay(self.num_of_players)
                            (x,y)=robot.shoot()    # shoot the ball
                            while (self.game_ball.ball_pos[0]+ x < 15 or self.game_ball.ball_pos[0]+ x > 30.5*30 ) :
                                (x,y)=robot.shoot()
                            ball_pos=self.game_ball.move_ball(x,y)    # change pos of ball based on shoot

                            if self.blue_team.calculate_goal(ball_pos[0],ball_pos[1],self.blue_team.list_robots):
                                self.red_team.red_reset_arrenge(self.red_team.list_robots)
                                self.game_ball.ball_reset()
                                self.game_field.remove_gaols_showing("blue")
                                self.game_field.show_goals(29.5*30,"blue",self.blue_team.goal)
                            elif self.red_team.calculate_goal(ball_pos[0],ball_pos[1],self.red_team.list_robots):
                                self.blue_team.blue_reset_arrenge(self.blue_team.list_robots)
                                self.game_ball.ball_reset()
                                self.game_field.remove_gaols_showing("red")
                                self.game_field.show_goals(45,"red",self.red_team.goal)

                        # check the distance of the robot and ball on y line
                        elif abs(robot.pos[1] - self.game_ball.ball_pos[1]) == 30 and robot.pos[0] == self.game_ball.ball_pos[0]:
                            self.delay(self.num_of_players)
                            (x, y) = robot.shoot()  #  shoot the ball
                            while (self.game_ball.ball_pos[0] + x < 15 or self.game_ball.ball_pos[0] + x > 30.5 * 30):
                                (x, y) = robot.shoot()
                            ball_pos = self.game_ball.move_ball(x, y)  # change pos of ball based on shoot

                            if self.blue_team.calculate_goal(ball_pos[0], ball_pos[1], self.blue_team.list_robots):
                                self.red_team.red_reset_arrenge(self.red_team.list_robots)
                                self.game_ball.ball_reset()
                                self.game_field.remove_gaols_showing("blue")
                                self.game_field.show_goals(29.5 * 30, "blue", self.blue_team.goal)
                                time.sleep(2)
                            elif self.red_team.calculate_goal(ball_pos[0], ball_pos[1], self.red_team.list_robots):
                                self.blue_team.blue_reset_arrenge(self.blue_team.list_robots)
                                self.game_ball.ball_reset()
                                self.game_field.remove_gaols_showing("red")
                                self.game_field.show_goals(45, "red", self.red_team.goal)
                                time.sleep(2)

                        # check the distance of the robot and ball on both x and y line
                        elif hypot(robot.pos[0] - self.game_ball.ball_pos[0], robot.pos[1] - self.game_ball.ball_pos[1]) == sqrt(2) * 30:
                            self.delay(self.num_of_players)
                            (x, y) = robot.shoot()  # shoot the ball
                            while (self.game_ball.ball_pos[0] + x < 15 or self.game_ball.ball_pos[0] + x > 30.5 * 30):
                                (x, y) = robot.shoot()
                            ball_pos = self.game_ball.move_ball(x, y)  # change pos of ball based on shoot

                            if self.blue_team.calculate_goal(ball_pos[0], ball_pos[1], self.blue_team.list_robots):
                                self.red_team.red_reset_arrenge(self.red_team.list_robots)
                                self.game_ball.ball_reset()
                                self.game_field.remove_gaols_showing("blue")
                                self.game_field.show_goals(29.5 * 30, "blue", self.blue_team.goal)
                                time.sleep(2)
                            elif self.red_team.calculate_goal(ball_pos[0], ball_pos[1], self.red_team.list_robots):
                                self.blue_team.blue_reset_arrenge(self.blue_team.list_robots)
                                self.game_ball.ball_reset()
                                self.game_field.remove_gaols_showing("red")
                                self.game_field.show_goals(45, "red", self.red_team.goal)
                                time.sleep(2)

                        else:
                            self.delay(self.num_of_players)
                    else:
                        robot.move_robot()
                        # check the distance of the robot and ball on x line
                        if abs(robot.pos[0] - self.game_ball.ball_pos[0]) == 30 and robot.pos[1] == \
                                self.game_ball.ball_pos[1]:
                            self.delay(self.num_of_players)
                            (x, y) = robot.shoot()  # shoot the ball
                            while (self.game_ball.ball_pos[0] + x < 15 or self.game_ball.ball_pos[0] + x > 30.5 * 30):
                                (x, y) = robot.shoot()
                            self.game_ball.move_ball(x, y)  # change pos of ball based on shoot


        # print game's result
        self.game_field.end_message(self.red_team.goal,self.blue_team.goal)




if __name__ == '__main__':
    game1 = Game()
    game1.start_game()
