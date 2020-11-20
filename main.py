from team import *
from ball import *
from field import *
from math import hypot, sqrt



class Game:
    def __init__(self):
        self.game_field = Field()  # create the field of the game
        self.game_ball = Ball()  # create the ball of the game
        self.game_ball.manage()  # add tha ball to the field
        self.blue_team = Team("blue")  # create the blue team of the game
        self.red_team = Team("red")  # create the red team of the game
        # start the game
        self.game_field.start_game_sign()
        time.sleep(1)

    # check if there is any player with charge > 0
    def check_charges(self):
        if self.blue_team.halfback1.charge > 0 or self.blue_team.halfback2.charge > 0 or \
                self.blue_team.forward.charge > 0 or self.red_team.halfback1.charge > 0 or \
                self.red_team.halfback2.charge > 0 or self.red_team.forward.charge > 0:
            return True
        else:
            return False


game1 = Game()
# continue the game until all players' charge finishes
while game1.check_charges():
    num_of_players = 6
    for team in [game1.blue_team, game1.red_team]:
        for goaler in [game1.red_team.goaler,game1.blue_team.goaler]:
            goaler.move_robot()
            time.sleep(float(6 / num_of_players / 50))
            goaler.move_robot()

        for player in team.list_robots:   # move each player of teams

            player.move_robot()
            # remove player with charge < 0 from team
            if player.charge <= 0:  # check the charge of the robot
                player.move_robot()
                team.list_robots.remove(player)
                num_of_players -= 1
                logging.basicConfig(filename='Robot_footballer.log', level=logging.INFO,
                                    format='%(asctime)s _ %(levelname)s _ %(message)s')
                logging.info('A robot was removed')

            # check if player can shot the ball
            if abs(player.pos[0] - game1.game_ball.ball_pos[0]) == 30 and player.pos[1] == game1.game_ball.ball_pos[1]:
                time.sleep(float(6/num_of_players/50))

                (x, y) = player.shoot()         #check the ball pos and not going out of field
                while (game1.game_ball.ball_pos[0] + x < 15 or game1.game_ball.ball_pos[0] + x > 30.5 * 30):
                    (x, y) = player.shoot()
                game1.game_ball.move_ball(x, y)  # shoot and move the ball
                game1.red_team.calculate_goal()  # check if it's a goal
                game1.blue_team.calculate_goal()

            elif abs(player.pos[1] - game1.game_ball.ball_pos[1]) == 30 and player.pos[0] == \
                    game1.game_ball.ball_pos[0]:
                time.sleep(float(6/num_of_players/50))
                (x, y) = player.shoot() #check the ball pos and not going out of field
                while (game1.game_ball.ball_pos[0] + x < 15 or game1.game_ball.ball_pos[0] + x > 30.5 * 30):
                    (x, y) = player.shoot()
                game1.game_ball.move_ball(x, y)  # shoot and move the ball
                game1.red_team.calculate_goal()   # check if it's a goal
                game1.blue_team.calculate_goal()

            elif hypot(player.pos[0] - game1.game_ball.ball_pos[0],
                       player.pos[1] - game1.game_ball.ball_pos[1]) == sqrt(2) * 30:
                time.sleep(float(6 / num_of_players / 50))
                (x, y) = player.shoot() #check the ball pos and not going out of field
                while (game1.game_ball.ball_pos[0] + x < 15 or game1.game_ball.ball_pos[0] + x > 30.5 * 30):
                    (x, y) = player.shoot()
                game1.game_ball.move_ball(x, y)  # shoot and move the ball
                game1.red_team.calculate_goal()   # check if it's a goal
                game1.blue_team.calculate_goal()

            else :
                time.sleep(float(6 / num_of_players / 50))


# print game's result
msg = Text(Point(15.5*30, 21.5*30), "Red Team {0} - {1} Blue Team".format(game1.red_team.goal, game1.blue_team.goal))
msg.draw(game1.game_field.win)
try:
    game1.game_field.win.getMouse()
    game1.game_field.win.close()
except GraphicsError:
    print("tha game ended")