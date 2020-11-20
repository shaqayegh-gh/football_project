import logging
from robots import *



class Team (Ball,Robot):
    def __init__(self,color):
        super(Team, self).__init__()
        self.color = color  # set the color of the team
        self.goal = 0   # count of the team's scores

        self.halfback1 = Halfback1(self.color)  # set 4 players for team
        self.halfback2 = Halfback2(self.color)
        self.forward = Forward(self.color)
        self.goaler = Goaler(self.color)

        self.list_robots=[self.halfback1,self.halfback2,self.forward]

        self.halfback1.manage()      # add the players to the field
        self.halfback2.manage()
        self.forward.manage()
        self.goaler.manage()


        self.show_goals(45,"red",self.goal)  # show the number of the goals for red team
        self.show_goals(29.5*30,"blue",self.goal)  # show the number of the goals for blue team

    def calculate_goal(self):
        # Calculate team goals
        if self.color == "red":
            if  self.ball_pos[0] ==30.5*30 and 8.5*30 <= self.ball_pos[1] <= 12.5*30 :
                self.goal += 1
                print("gooooooooal")
                self.remove_gaols_showing(self.color)
                self.show_goals(45,self.color,self.goal)
                logging.basicConfig(filename='Robot_footballer.log', level=logging.INFO,
                                    format='%(asctime)s _ %(levelname)s _ %(message)s')
                logging.info('The red team scored a goal')
                self.full_pos = [(10.5 * 30, 3.5 * 30), (20.5 * 30, 3.5 * 30), (10.5 * 30, 17.5 * 30),
                            (20.5 * 30, 17.5 * 30),
                            (18.5 * 30, 10.5 * 30), (12.5 * 30, 10.5 * 30), (45, 10.5 * 30),
                            (29.5 * 30, 10.5 * 30)]

                self.scored_message(self.color)    #show the gaol message


        if self.color == "blue":
            if self.ball_pos[0] == 15 and 8.5 * 30 <= self.ball_pos[1] <= 12.5 * 30:
                self.goal += 1
                print("gooooooooal")
                self.remove_gaols_showing(self.color)
                self.show_goals(29.5 * 30, self.color, self.goal)
                logging.basicConfig(filename='Robot_footballer.log', level=logging.INFO,
                                    format='%(asctime)s _ %(levelname)s _ %(message)s')
                logging.info('The blue team scored a goal')
                self.full_pos = [(10.5 * 30, 3.5 * 30), (20.5 * 30, 3.5 * 30), (10.5 * 30, 17.5 * 30),
                            (20.5 * 30, 17.5 * 30),
                            (18.5 * 30, 10.5 * 30), (12.5 * 30, 10.5 * 30), (45, 10.5 * 30),
                            (29.5 * 30, 10.5 * 30)]

                self.scored_message(self.color)    #show the gaol message





