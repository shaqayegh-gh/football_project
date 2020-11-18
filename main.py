from team import *

game_field=Field()

blue_team=Team("blue")
red_team=Team("red")

red_team.forward.manage()
blue_team.forward.manage()

red_team.forward.move_robot()
blue_team.forward.move_robot()
