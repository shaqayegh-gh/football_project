def Calculate_goal(self, ball_position):
    # Calculate team goals
    if self.color == "red":
        if 900 <= ball_position[0] <= 930 & 240 <= ball_position[1] <= 390:
            self.goal += 1
            logging.basicConfig(filename='footbaler_robot_log.log', format='%(asctime)s %(message)s')
            logging.info('The red team scored a goal')
            self.full_pos = [(10.5 * 30, 3.5 * 30), (20.5 * 30, 3.5 * 30), (10.5 * 30, 17.5 * 30),
                             (20.5 * 30, 17.5 * 30),
                             (18.5 * 30, 10.5 * 30), (12.5 * 30, 10.5 * 30), (45, 10.5 * 30),
                             (29.5 * 30, 10.5 * 30)]

    if self.color == "blue":
        if 0 <= ball_position[0] <= 30 & 240 <= ball_position[1] <= 390:
            self.goal += 1
            logging.basicConfig(filename='footbaler_robot_log.log', filemode='w', format='%(asctime)s %(message)s')
            logging.info("The blue team scored a goal")
            self.full_pos = [(10.5 * 30, 3.5 * 30), (20.5 * 30, 3.5 * 30), (10.5 * 30, 17.5 * 30),
                             (20.5 * 30, 17.5 * 30),
                             (18.5 * 30, 10.5 * 30), (12.5 * 30, 10.5 * 30), (45, 10.5 * 30),
                             (29.5 * 30, 10.5 * 30)]