from team import *
from ball import *
from field import *

# print(red_team.forward.charge)
#
# red_team.forward.move_robot()
#
# time.sleep(1)
# print(red_team.forward.charge)
#
# red_team.forward.move_robot()
# print(red_team.forward.charge)
#
# red_team.forward.move_robot()
#
# game_field.win.getMouse()

class Game():
    def __init__(self):
        self.game_field=Field()    # making the field of the game
        self.game_ball = Ball()

        self.blue_team = Team("blue")
        self.red_team = Team("red")

        self.game_field.start_game_sign()
        time.sleep(1)
        self.red_team.halfback1.move_robot()
        time.sleep(1)
        self.blue_team.halfback1.move_robot()


        self.game_field.win.getMouse()


game1=Game()


