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
        self.game_ball.manage()

        self.blue_team = Team("blue")
        self.red_team = Team("red")

        self.game_field.start_game_sign()

        # # print(self.blue_team.forward.pos)
        #
        # self.blue_team.forward.move_robot()
        # print(self.blue_team.forward.pos)
        # time.sleep(3)
        # self.blue_team.forward.move_robot()
        # print(self.blue_team.forward.pos)
        #
        # time.sleep(3)
        # self.blue_team.forward.move_robot()
        # print(self.blue_team.forward.pos)
        #
        # time.sleep(3)
        # self.blue_team.forward.move_robot()
        # print(self.blue_team.forward.pos)
        #
        # time.sleep(3)

        for i in range(100):
            for t in [self.blue_team,self.red_team]:
                t.team_move()



        self.game_field.win.getMouse()


game1=Game()


