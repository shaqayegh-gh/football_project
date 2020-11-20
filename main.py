from team import *
from ball import *
from field import *
from math import hypot, sqrt


class Game:
    def __init__(self):
        self.game_field=Field()    # making the field of the game
        self.game_ball = Ball()
        self.game_ball.manage()  # add tha ball to the field
        self.blue_team = Team("blue")
        self.red_team = Team("red")

        self.game_field.start_game_sign()
        time.sleep(1)
        """self.red_team.halfback1.move_robot()
        time.sleep(1)
        self.blue_team.halfback1.move_robot()

"""
        self.game_field.win.getMouse()

    def check_charges(self):
        if self.blue_team.halfback1.charge > 0 or self.blue_team.halfback2.charge > 0 or \
                self.blue_team.forward.charge > 0 or self.red_team.halfback1.charge > 0 or \
                self.red_team.halfback2.charge > 0 or self.red_team.forward.charge > 0:
            return True
        else:
            return False


game1=Game()
while game1.check_charges():
    for team in [game1.blue_team, game1.red_team]:
        for player in team.list_robots:
            player.move_robot()
            time.sleep(0.1)
            if player.charge <= 0:  # check the charge of the robot
                player.move_robot()
                team.list_robots.remove(player)
                logging.basicConfig(filename='footbaler_ball_log.log', filemode='w', format='%(asctime)s %(message)s')
                logging.info("A robot was removed")
            elif abs(player.pos[0] - game1.game_ball.ball_pos[0]) == 30 and player.pos[1] == game1.game_ball.ball_pos[1]:
                time.sleep(.07)
                game1.game_ball.move_ball(player.shoot()[0], player.shoot()[1])
                game1.red_team.Calculate_goal()
                game1.blue_team.Calculate_goal()
            elif abs(player.pos[1] - game1.game_ball.ball_pos[1]) == 30 and player.pos[0] == \
                    game1.game_ball.ball_pos[0]:
                time.sleep(.07)
                game1.game_ball.move_ball(player.shoot()[0], player.shoot()[1])
                game1.red_team.Calculate_goal()
                game1.blue_team.Calculate_goal()
            elif hypot(player.pos[0] - game1.game_ball.ball_pos[0],
                       player.pos[1] - game1.game_ball.ball_pos[1]) == sqrt(2) * 30:
                time.sleep(.07)
                game1.game_ball.move_ball(player.shoot()[0], player.shoot()[1])
                game1.red_team.Calculate_goal()
                game1.blue_team.Calculate_goal()
