# Fuen Cui GitHub:
# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-FuenCui.git

from blue_line import Blueline
from disk import Disk
from animate import Animate
from scores import Scores
import random


class GameController:
    '''connect four game controller'''
    def __init__(self, size, width, length):
        self.size = size
        self.width = width
        self.length = length
        self.blueline = Blueline(self.size)
        self.dk = Disk(self.width, self.length, self.size)
        self.drop_list = []
        self.x_list = []
        self.animate = []
        self.speed = True
        self.game_stop = False
        self.player_wins = False
        self.sc = Scores()
        self.who_win = 0

    def update(self):
        '''The content to be drawn in each frame'''
        self.computer_draw = False
        self.inspection_speed()
        if self.speed is True:
            fill(0, 0, 0)
            textSize(20)
            text("Player turn", 20, 20)
        elif self.speed is False:
            fill(0, 0, 0)
            textSize(20)
            text("Computer turn", 20, 20)
        if self.game_stop is False:
            self.dk.draw_me()
        for _ani in self.animate:
            _ani.draw()
        if self.dk.check_color is False:
            self.computer_AI_3()
            if self.computer_draw is True:
                self.control_mouse_up()
            elif self.computer_draw is False:
                self.computer_AI_2()
                if self.computer_draw is True:
                    self.control_mouse_up()

        self.blueline.surround(self.width, self.length)
        self.number_horizontal_line()
        self.number_vertical_line()
        self.inspection_game()

        if self.game_stop is True:
            self.print_result()
            if self.player_wins is True:
                self.sc.count()
            if self.player_wins is False:
                self.sc.count(win=False)

    def number_horizontal_line(self):
        '''Calculate how much horizontal line needed'''
        coefficient = self.length / (self.size + 1)
        for _x in range(self.size):
            temp = (_x + 1) * coefficient
            self.blueline.horizontal_line(self.width, temp)

    def number_vertical_line(self):
        '''Calculate how much vertical line needed'''
        coefficient = self.width / (self.size + 1)
        coef_2 = self.width / self.size
        # self.size == 2 It's the only special case
        if self.size == 2:
            self.spaces = 1
            for _y in range(self.spaces):
                temp = (_y + 1) * coef_2
                self.blueline.vertical_line(temp, self.length)
        else:
            self.spaces = self.size
            for _y in range(self.spaces):
                temp = (_y + 1) * coefficient
                self.blueline.vertical_line(temp, self.length)

    def inspection_speed(self):
        '''
        Ensure that no other disk can be added
        until a piece is droping in the position
        '''
        if len(self.animate) != 0:
            if self.animate[-1].Y != self.animate[-1].end_y:
                self.speed = False
            else:
                self.speed = True

    def print_result(self):
        '''print the winner'''
        cond1 = 1
        red_win = 2
        y_win = 3
        if self.who_win == cond1:
            fill(0, 255, 255)
            textSize(60)
            text("The Game Is Over!!!", self.width/4.5, self.length/2)
        elif self.who_win == red_win:
            fill(0, 255, 255)
            textSize(60)
            text("RED  WINS!!!", self.width/4.5, self.length/2)
        elif self.who_win == y_win:
            fill(0, 255, 255)
            textSize(60)
            text("YELLOW  WINS!!!", self.width/4.5, self.length/2)

    def inspection_game(self):
        '''check if game is needed to stop'''
        # if there's a win the end or no more space
        self.Xs = self.size + 1
        if self.size == 2:
            self.Xs = self.size
        self.Ys = self.size
        self.check_temp = self.Xs * self.Ys
        if self.check_temp == len(self.drop_list):
            self.who_win = 1
            self.game_stop = True
        self.player_list = []
        self.AI_list = []
        self.y_coef = self.length / (self.size + 1)
        if self.size == 2:
            self.x_coef = self.width / ((self.size) * 2)
        else:
            self.x_coef = self.width / ((self.size + 1) * 2)

        for temp in self.drop_list:
            if temp[2] is False:
                self.player_list.append([temp[0], temp[1]])
            elif temp[2] is True:
                self.AI_list.append([temp[0], temp[1]])

        for item in self.player_list:
            self._x = item[0]
            self._y = item[1]
            self.y_2 = self._y + self.y_coef
            self.y_3 = self._y + 2 * self.y_coef
            self.y_4 = self._y + 3 * self.y_coef
            self.x_2 = self._x + 2 * self.x_coef
            self.x_3 = self._x + 4 * self.x_coef
            self.x_4 = self._x + 6 * self.x_coef
            self.y_m2 = self._y - 2 * self.x_coef
            self.y_m3 = self._y - 4 * self.x_coef
            self.y_m4 = self._y - 6 * self.x_coef

            if (([self._x, self._y] in self.player_list)
                and
               ([self._x, self.y_2] in self.player_list)):
                if (([self._x, self.y_3] in self.player_list)
                    and
                   ([self._x, self.y_4] in self.player_list)):
                    self.who_win = 2
                    self.game_stop = True
                    self.player_wins = True
            if (([self._x, self._y] in self.player_list)
                and
               ([self.x_2, self._y] in self.player_list)):
                if (([self.x_3, self._y] in self.player_list)
                    and
                   ([self.x_4, self._y] in self.player_list)):
                    self.who_win = 2
                    self.game_stop = True
                    self.player_wins = True
            if (([self._x, self._y] in self.player_list)
                and
               ([self.x_2, self.y_2] in self.player_list)):
                if (([self.x_3, self.y_3] in self.player_list)
                    and
                   ([self.x_4, self.y_4] in self.player_list)):
                    self.who_win = 2
                    self.game_stop = True
                    self.player_wins = True
            if (([self._x, self._y] in self.player_list)
                and
               ([self.x_2, self.y_m2] in self.player_list)):
                if (([self.x_3, self.y_m3] in self.player_list)
                    and
                   ([self.x_4, self.y_m4] in self.player_list)):
                    self.who_win = 2
                    self.game_stop = True
                    self.player_wins = True

        for ai_item in self.AI_list:
            self.ai_x = ai_item[0]
            self.ai_y = ai_item[1]
            self.ai_y_2 = self.ai_y + self.y_coef
            self.ai_y_3 = self.ai_y + 2 * self.y_coef
            self.ai_y_4 = self.ai_y + 3 * self.y_coef
            self.ai_x_2 = self.ai_x + 2 * self.x_coef
            self.ai_x_3 = self.ai_x + 4 * self.x_coef
            self.ai_x_4 = self.ai_x + 6 * self.x_coef
            self.ai_y_m2 = self.ai_y - 2 * self.x_coef
            self.ai_y_m3 = self.ai_y - 4 * self.x_coef
            self.ai_y_m4 = self.ai_y - 6 * self.x_coef

            if (([self.ai_x, self.ai_y] in self.AI_list)
                and
               ([self.ai_x, self.ai_y_2] in self.AI_list)):
                if (([self.ai_x, self.ai_y_3] in self.AI_list)
                    and
                   ([self.ai_x, self.ai_y_4] in self.AI_list)):
                    self.who_win = 3
                    self.game_stop = True
            if (([self.ai_x, self.ai_y] in self.AI_list)
                and
               ([self.ai_x_2, self.ai_y] in self.AI_list)):
                if (([self.ai_x_3, self.ai_y] in self.AI_list)
                    and
                   ([self.ai_x_4, self.ai_y] in self.AI_list)):
                    self.who_win = 3
                    self.game_stop = True
            if (([self.ai_x, self.ai_y] in self.AI_list)
                and
               ([self.ai_x_2, self.ai_y_2] in self.AI_list)):
                if (([self.ai_x_3, self.ai_y_3] in self.AI_list)
                    and
                   ([self.ai_x_4, self.ai_y_4] in self.AI_list)):
                    self.who_win = 3
                    self.game_stop = True
            if (([self.ai_x, self.ai_y] in self.AI_list)
                and
               ([self.ai_x_2, self.ai_y_m2] in self.AI_list)):
                if (([self.ai_x_3, self.ai_y_m3] in self.AI_list)
                    and
                   ([self.ai_x_4, self.ai_y_m4] in self.AI_list)):
                    self.who_win = 3
                    self.game_stop = True

    def computer_AI_3(self):
        '''
        Computer AI dealing with 3 disk on a row
        Contains AI defensive and offensive ideas
        '''
        self.y_coef = self.length / (self.size + 1)
        self.y_start = self.y_coef / 2
        self.player_list = []
        self.AI_list = []
        if self.size == 2:
            self.x_coef = self.width / ((self.size) * 2)
        else:
            self.x_coef = self.width / ((self.size + 1) * 2)
        self.x_start = self.x_coef
        self.x_end = self.width - ((2 * 2 + 1) * self.x_coef)
        self.x_start_two = self.x_coef + 2 * self.x_coef
        self.x_end_two = self.width - ((1 * 2 + 1) * self.x_coef)
        self.max = self.length - (1.5 * self.y_coef)

        if len(self.drop_list) == 1:
            self.frist_x = self.drop_list[0][0]
            self.frist_y = (self.drop_list[0][1] + self.y_coef)
            self.computer_draw = True
            return self.control_mouse_press(self.frist_x, self.frist_y)

        for temp in self.drop_list:
            if temp[2] is False:
                self.player_list.append([temp[0], temp[1]])
            elif temp[2] is True:
                self.AI_list.append([temp[0], temp[1]])

        for ai_item in self.AI_list:
            self.ai_x = ai_item[0]
            self.ai_y = ai_item[1]
            self.ai_top = self.ai_y + 2 * self.y_coef
            self.ai_mid = self.ai_y + 1 * self.y_coef
            self.ai_add = self.ai_y + 3 * self.y_coef
            self.ai_sencond = self.ai_x + 2 * self.x_coef
            self.ai_third = self.ai_x + 4 * self.x_coef
            self.ai_h_add = self.ai_x + 6 * self.x_coef
            self.ai_h_red = self.ai_x - 2 * self.x_coef
            self.ai_y_check = self.x_coef * 2

            if (([self.ai_x, self.ai_y] in self.AI_list)
                and
               ([self.ai_x, self.ai_mid] in self.AI_list)):
                if [self.ai_x, self.ai_top] in self.AI_list:
                    if([self.ai_x, self.ai_add] not in self.player_list
                        and
                        [self.ai_x, self.ai_add] not in self.AI_list
                       ):
                        if ([self.ai_x, self.max] not in self.AI_list
                           and
                           [self.ai_x, self.max] not in self.player_list):
                            self.computer_draw = True
                            return self.control_mouse_press(self.ai_x,
                                                            self.ai_y)

            if (([self.ai_x, self.ai_y] in self.AI_list)
               and
               ([self.ai_sencond, self.ai_y] in self.AI_list)):
                if [self.ai_third, self.ai_y] in self.AI_list:
                    if self.ai_x == self.x_start:
                        if [self.ai_h_add, self.ai_y] not in self.player_list:
                            if ((self.ai_y == self.x_coef)
                                or
                                ([self.ai_h_add, self.ai_y - self.ai_y_check]
                                 in (self.AI_list or self.player_list))):
                                self.computer_draw = True
                                return self.control_mouse_press(self.ai_h_add,
                                                                0)
                    elif self.ai_x == self.x_end:
                        if [self.ai_h_red, self.ai_y] not in self.player_list:
                            if ((self.ai_y == self.x_coef)
                                or
                                ([self.ai_h_red, self.ai_y - self.ai_y_check]
                                 in (self.AI_list or self.player_list))):
                                self.computer_draw = True
                                return self.control_mouse_press(self.ai_h_red,
                                                                0)

                    elif [self.ai_h_add, self.ai_y] not in self.player_list:
                        if ((self.ai_y == self.x_coef)
                            or
                            ([self.ai_h_add, self.ai_y - self.ai_y_check]
                             in (self.AI_list or self.player_list))):
                            self.computer_draw = True
                            return self.control_mouse_press(self.ai_h_add, 0)
                    elif [self.ai_h_red, self.ai_y] not in self.player_list:
                        if ((self.ai_y == self.x_coef)
                            or
                            ([self.ai_h_red, self.ai_y - self.ai_y_check]
                             in (self.AI_list or self.player_list))):
                            self.computer_draw = True
                            return self.control_mouse_press(self.ai_h_red, 0)
            if (([self.ai_x, self.ai_y] in self.AI_list)
                and
               ([self.ai_sencond, self.ai_y] in self.AI_list)):
                if [self.ai_h_add, self.ai_y] in self.AI_list:
                    if [self.ai_third, self.ai_y] not in self.player_list:
                        if ((self.ai_y == self.x_coef)
                            or
                            ([self.ai_third, self.ai_y - self.ai_y_check]
                             in (self.AI_list or self.player_list))):
                            self.computer_draw = True
                            return self.control_mouse_press(self.ai_third, 0)
            if (([self.ai_third, self.ai_y] in self.AI_list)
                and
               ([self.ai_h_add, self.ai_y] in self.AI_list)):
                if [self.ai_sencond, self.ai_y] in self.AI_list:
                    if [self.ai_third, self.ai_y] not in self.player_list:
                        if ((self.ai_y == self.x_coef)
                            or
                            ([self.ai_sencond, self.ai_y - self.ai_y_check]
                             in (self.AI_list or self.player_list))):
                            self.computer_draw = True
                            return self.control_mouse_press(self.ai_sencond, 0)

        for item in self.player_list:
            self._x = item[0]
            self._y = item[1]
            self.top = self._y + 2 * self.y_coef
            self.mid = self._y + 1 * self.y_coef
            self.add = self._y + 3 * self.y_coef
            self.sencond = self._x + 2 * self.x_coef
            self.third = self._x + 4 * self.x_coef
            self.h_add = self._x + 6 * self.x_coef
            self.h_red = self._x - 2 * self.x_coef
            self.y_check = self.x_coef * 2

            if (([self._x, self._y] in self.player_list)
               and
               ([self._x, self.mid] in self.player_list)):
                if [self._x, self.top] in self.player_list:
                    if([self._x, self.add] not in self.AI_list
                        and
                       [self._x, self.add] not in self.player_list
                       ):
                        if ([self._x, self.max] not in self.AI_list
                           and
                           [self._x, self.max] not in self.player_list):
                            self.computer_draw = True
                            return self.control_mouse_press(self._x,
                                                            self._y)

            if (([self._x, self._y] in self.player_list)
                and
               ([self.sencond, self._y] in self.player_list)):
                if [self.third, self._y] in self.player_list:
                    if self._x == self.x_start:
                        if [self.h_add, self._y] not in self.AI_list:
                            if ((self._y == self.x_coef)
                                or
                                ([self.h_add, self._y - self.y_check]
                                 in (self.player_list or self.AI_list))):
                                self.computer_draw = True
                                return self.control_mouse_press(self.h_add, 0)
                    elif self._x == self.x_end:
                        if [self.h_red, self._y] not in self.AI_list:
                            if ((self._y == self.x_coef)
                                or
                                ([self.h_red, self._y - self.y_check]
                                 in (self.player_list or self.AI_list))):
                                self.computer_draw = True
                                return self.control_mouse_press(self.h_red, 0)
                    elif [self.h_add, self._y] not in self.AI_list:
                        if ((self._y == self.x_coef)
                            or
                            ([self.h_add, self._y - self.y_check]
                             in (self.player_list or self.AI_list))):
                            self.computer_draw = True
                            return self.control_mouse_press(self.h_add, 0)
                    elif [self.h_red, self._y] not in self.AI_list:
                        if ((self._y == self.x_coef)
                            or
                            ([self.h_red, self._y - self.y_check]
                             in (self.player_list or self.AI_list))):
                            if (([self.h_red, self.max] not in self.AI_list)
                                and
                                ([self.h_red,
                                  self.max] not in self.player_list)):
                                self.computer_draw = True
                                return self.control_mouse_press(self.h_red, 0)

    def computer_AI_2(self):
        '''
        Computer AI dealing with 2 disk on a row
        Contains AI defensive and offensive ideas
        '''
        self.y_coef = self.length / (self.size + 1)
        self.y_start = self.y_coef / 2
        self.player_list = []
        self.AI_list = []
        if self.size == 2:
            self.x_coef = self.width / ((self.size) * 2)
        else:
            self.x_coef = self.width / ((self.size + 1) * 2)
        self.x_start = self.x_coef
        self.x_end = self.width - ((2 * 2 + 1) * self.x_coef)
        self.x_start_two = self.x_coef + 2 * self.x_coef
        self.x_end_two = self.width - ((1 * 2 + 1) * self.x_coef)
        self.max = self.length - (1.5 * self.y_coef)

        for temp in self.drop_list:
            if temp[2] is False:
                self.player_list.append([temp[0], temp[1]])
            elif temp[2] is True:
                self.AI_list.append([temp[0], temp[1]])

        for item in self.player_list:
            self._x = item[0]
            self._y = item[1]
            self.top = self._y + 2 * self.y_coef
            self.mid = self._y + 1 * self.y_coef
            self.add = self._y + 3 * self.y_coef
            self.sencond = self._x + 2 * self.x_coef
            self.third = self._x + 4 * self.x_coef
            self.h_add = self._x + 6 * self.x_coef
            self.h_red = self._x - 2 * self.x_coef
            self.y_check = self.x_coef * 2

            if (([self._x, self._y] in self.player_list)
                and
               ([self._x, self.mid] in self.player_list)):
                if [self._x, self.top] not in self.player_list:
                    if([self._x, self.top] not in self.AI_list
                        and
                        [self._x, self.top] not in self.player_list
                       ):
                        if ([self._x, self.max] not in self.AI_list
                           and
                           [self._x, self.max] not in self.player_list):
                            self.computer_draw = True
                            return self.control_mouse_press(self._x, 0)

            if (([self._x, self._y] in self.player_list)
                and
               ([self.sencond, self._y] in self.player_list)):
                if self._x == self.x_coef:
                    if [self.third, self._y] not in self.AI_list:
                        if [self.third, self._y] not in self.player_list:
                            if ((self._y == self.x_coef)
                                or
                                ([self.third, self._y - self.y_check]
                                 in (self.player_list or self.AI_list))):
                                self.computer_draw = True
                                return self.control_mouse_press(self.third, 0)
                elif self._x == self.x_end_two:
                    if [self.h_red, self._y] not in self.AI_list:
                        if [self.h_red, self._y] not in self.player_list:
                            if ((self._y == self.x_coef)
                                or
                                ([self.h_red, self._y - self.y_check]
                                 in (self.player_list or self.AI_list))):
                                self.computer_draw = True
                                return self.control_mouse_press(self.h_red, 0)
                elif [self.third, self._y] not in self.AI_list:
                    if [self.third, self._y] not in self.player_list:
                        if ((self._y == self.x_coef)
                            or
                            ([self.third, self._y - self.y_check]
                             in (self.player_list or self.AI_list))):
                            self.computer_draw = True
                            return self.control_mouse_press(self.third, 0)
                elif [self.h_red, self._y] not in self.AI_list:
                    if self._x != self.x_coef:
                        if [self.h_red, self._y] not in self.player_list:
                            if ((self._y == self.x_coef)
                                or
                                ([self.h_red, self._y - self.y_check]
                                 in (self.player_list or self.AI_list))):
                                self.computer_draw = True
                                return self.control_mouse_press(self.h_red, 0)

            if (([self._x, self._y] in self.player_list)
                and
               ([self.third, self._y] in self.player_list)):
                if [self.sencond, self._y] not in self.player_list:
                    if [self.sencond, self._y] not in self.AI_list:
                        if ((self._y == self.x_coef)
                            or
                            ([self.sencond, self._y - self.y_check]
                             in (self.player_list or self.AI_list))):
                            self.computer_draw = True
                            return self.control_mouse_press(self.sencond, 0)

        for ai_item in self.AI_list:
            self.ai_x = ai_item[0]
            self.ai_y = ai_item[1]
            self.ai_top = self.ai_y + 2 * self.y_coef
            self.ai_mid = self.ai_y + 1 * self.y_coef
            self.ai_add = self.ai_y + 3 * self.y_coef
            self.ai_sencond = self.ai_x + 2 * self.x_coef
            self.ai_third = self.ai_x + 4 * self.x_coef
            self.ai_y_check = self.x_coef * 2

            if (([self.ai_x, self.ai_y] in self.AI_list)
                and
               ([self.ai_third, self.ai_y] in self.AI_list)):
                if [self.ai_sencond, self.ai_y] not in self.AI_list:
                    if [self.ai_sencond, self.ai_y] not in self.player_list:
                        if ((self.ai_y == self.x_coef)
                            or
                            ([self.sencond, self.ai_y - self.ai_y_check]
                             in (self.player_list or self.AI_list))):
                            self.computer_draw = True
                            return self.control_mouse_press(self.ai_sencond, 0)
            # 2 ai check h
            if (([self.ai_x, self.ai_y] in self.AI_list)
                and
               ([self.ai_x, self.ai_mid] in self.AI_list)):
                if [self.ai_x, self.ai_top] not in self.AI_list:
                    if(([self.ai_x, self.ai_top] not in self.player_list)
                        and
                       ([self.ai_x, self.ai_top] not in self.AI_list)):
                        if ([self.ai_x, self.max] not in self.AI_list
                           and
                           [self.ai_x, self.max] not in self.player_list):
                            self.computer_draw = True
                            return self.control_mouse_press(self.ai_x, 0)

        self.randm_pick = random.choice(self.dk.x_list)
        self.randm_counter = 0
        for _temp in self.drop_list:
            if _temp[0] == self.randm_pick:
                self.randm_counter += 1
        if self.randm_counter < self.size:
            self.computer_draw = True
            return self.control_mouse_press(self.randm_pick, 0)
        else:
            self.computer_AI_2()

    def control_mouse_press(self, mouseX, mouseY):
        '''control mouse press'''
        if self.speed is True and self.game_stop is False:
            self.dk.control_press(mouseX, mouseY)

    def control_mouse_up(self):
        '''control mouse release'''
        if self.speed is True and self.game_stop is False:
            self.dk.control_up()
            self.drop_control()

    def drop_control(self):
        '''
        calculates where the position is disk should be
        save the data for each piece
        so that the AI can decide to move
        '''
        self.check_color = self.dk.check_color
        self.X = self.dk.X
        self.Y = self.dk.Y
        self.rad = self.dk.rad
        self.x_list = self.dk.x_list
        self.y_coef = self.length / (2 * (self.size + 1))
        self.start_y = self.y_coef
        if self.size == 2:
            self.x_list = self.dk.x_list[:-1]
        YSPACE = self.size
        self.counter = 0

        if len(self.drop_list) == 0:
            Y = self.y_coef
            self.drop_list.append([self.X, Y, self.check_color])
            self.animate.append(Animate(self.start_y, Y, self.X,
                                        self.rad, self.check_color,
                                        self.length))
        elif (j[0] == self.X for j in self.drop_list):
            for i in self.drop_list:
                if i[0] == self.X:
                    self.counter += 1
            if self.counter < self.size:
                Y = self.y_coef * (1 + 2 * self.counter)
                self.drop_list.append([self.X, Y, self.check_color])
                self.animate.append(Animate(self.start_y, Y, self.X,
                                            self.rad, self.check_color,
                                            self.length))
        else:
            Y = self.y_coef
            self.drop_list.append([self.X, Y, self.check_color])
            self.animate.append(Animate(self.start_y, Y, self.X,
                                        self.rad, self.check_color,
                                        self.length))
