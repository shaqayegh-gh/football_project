from graphics import *

class Field:
    full_pos = [(10.5 * 30, 3.5 * 30), (20.5 * 30, 3.5 * 30), (10.5 * 30, 17.5 * 30), (20.5 * 30, 17.5 * 30),
                (18.5 * 30, 10.5 * 30), (12.5 * 30, 10.5 * 30), (45, 10.5 * 30),
                (29.5 * 30, 10.5 * 30),(465,315)]  # newest positions of the players in the field

    win = GraphWin("Soccer Game", 930,
                   660)  # open a drawing window named Soccer Game with a width of 930 and length of 630
    win.setBackground(color="green")

    def __init__(self):
        for i in range(0, 930,
                       30):  # drawing a checkered page (930=31*30) --> 31:block in width of field   30: the width of each block
            for j in range(0, 630, 30):  # (630=21*30) --> 21:block in length of the field  30 :the width of each block
                rectangle = Rectangle(Point(i, j), Point(i + 30, j + 30))
                rectangle.setOutline(color="black")
                rectangle.setWidth(1.4)
                rectangle.draw(self.win)

        gate1 = Rectangle(Point(0, 240), Point(30, 390))  # drawing two rectangle for the gates
        gate1.setFill(color="red")
        gate2 = Rectangle(Point(900, 240), Point(930, 390))
        gate2.setFill(color="blue")
        gate1.draw(self.win)
        gate2.draw(self.win)



    @classmethod
    def add_item(cls, func):  # add new object like the players sign(circle) into the drawing window(win)
        cls.win.addItem(func)


    def start_game_sign(self):      # count from 3 to 1 and show the start message
        for i in range(3,0,-1):
            message=Text(Point(15.5*30,21.5*30), i )
            message.setSize(18)
            message.draw(self.win)
            time.sleep(0.8)
            message.undraw()
        message=Text(Point(15.5*30,21.5*30),"START")
        message.setSize(18)
        message.draw(self.win)
        time.sleep(1)
        message.undraw()

    def show_goals(self, x, color, goal):      #showing number of a team's score bottom of window
        if color == "red":
            self.red_goal_message = Text(Point(x, 21.5 * 30), "RED : {}".format(goal))
            self.red_goal_message.setSize(16)
            self.red_goal_message.draw(self.win)
        elif color == "blue":
            self.blue_goal_message = Text(Point(x, 21.5 * 30), "{} : BLUE".format(goal))
            self.blue_goal_message.setSize(16)
            self.blue_goal_message.draw(self.win)

    def remove_gaols_showing(self,color):
        if color == "red":
            self.red_goal_message.undraw()
        elif color == "blue":
            self.blue_goal_message.undraw()

    def scored_message(self,color):    # show a message when one team get new score
        msg = Text(Point(15.5 * 30, 21.5 * 30), "{} team scored. Goaaaaaal!".format(color))
        msg.setSize(16)
        msg.draw(self.win)
        time.sleep(2)
        msg.undraw()


    def end_message(self,red_team_goal,blue_team_goal):   # print game's result
        end_msg = Text(Point(15.5 * 30, 21.5 * 30),
                   "RED Team: {0} - {1} :BLUE Team".format(red_team_goal, blue_team_goal))
        end_msg.setSize(16)
        end_msg.draw(self.win)
        try:
            self.win.getMouse()  # the game window closing with mouse click
            self.win.close()
        except GraphicsError:
            print("tha game ended")





