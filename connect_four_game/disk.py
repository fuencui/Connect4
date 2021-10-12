# Fuen Cui GitHub:
# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-FuenCui.git

class Disk:
    '''A Yellow Disk or a Red Disk'''
    def __init__(self, width, length, size):
        self.width = width
        self.length = length
        self.size = size
        self.check_color = True
        self.check_draw = False
        self.X = 0
        self.Y = 0
        self.rad = 0
        self.color_switch = []
        self.x_list = []

    def draw_me(self):
        '''drawing method called by game_controller.py'''
        if self.check_draw is True:
            if self.check_color is True:
                fill(255, 0, 0)
                noStroke()
                circle(self.X, self.Y, self.rad)
            if self.check_color is False:
                fill(255, 255, 0)
                noStroke()
                circle(self.X, self.Y, self.rad)

    def control_press(self, mouseX, mouseY):
        '''the information of Disk when user press mouse'''
        range_mouseY = self.length / (self.size + 1)
        if self.size == 2:
            half_space = self.width / ((self.size) * 2)
        else:
            half_space = self.width / ((self.size + 1) * 2)
        self.x_list = [half_space]
        temp = half_space
        for i in range(self.size):
            temp += 2 * half_space
            self.x_list.append(temp)
        if self.size == 2:
            self.rad = self.width / self.size
        else:
            self.rad = self.width / (self.size + 1)
            self.X = min(self.x_list, key=lambda x: (abs(x - mouseX)))
            self.Y = range_mouseY / 2
            self.check_draw = True
            return self.x_list

    def control_up(self):
        '''the information of Disk when user release mouse'''
        self.check_draw = False
        if (len(self.color_switch) % 2) == 0:
            self.check_color = False
            self.color_switch.append(1)
        else:
            self.check_color = True
            self.color_switch.append(1)
