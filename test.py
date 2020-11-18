from robots import *
from graphics import *


game=Field()
halfback1_1=Halfback1_1()
halfback1_2=Halfback1_2()
halfback2_1=Halfback2_1()
halfback2_2=Halfback2_2()
forward1=Forward_1()
forward2=Forward_2()
goaler1=Goaler_1()
goaler2=Goaler_2()

halfback1_1.manage()
halfback1_2.manage()
halfback2_1.manage()
halfback2_2.manage()
forward1.manage()
forward2.manage()
goaler1.manage()
goaler2.manage()

print(game.full_pos)
halfback1_1.move_robot()


print(game.full_pos)
halfback1_2.move_robot()

print(game.full_pos)
halfback2_1.move_robot()

print(game.full_pos)
halfback2_2.move_robot()

print(game.full_pos)
forward1.move_robot()

print(game.full_pos)
forward2.move_robot()

print(game.full_pos)
goaler1.move_robot()

print(game.full_pos)
goaler2.move_robot()
