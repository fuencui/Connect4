# Fuen Cui GitHub:
# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-FuenCui.git

class Animate:
    '''Animate of disk droping'''
    def __init__(self, start_y, end_y, start_x, rad, color, length):
        self.length = length
        self.X = start_x
        self.Y = start_y
        self.end_y = self.length - end_y
        self.color = color
        self.rad = rad

    def draw(self):
        '''drawing method'''
        if self.Y < self.end_y:
            self.Y += 10
        if self.color is True:
            self.draw_circle_red()
        else:
            self.draw_circle_yellow()

    def draw_circle_yellow(self):
        '''a yellow circle'''
        fill(255, 0, 0)
        noStroke()
        circle(self.X, self.Y, self.rad)

    def draw_circle_red(self):
        '''a red circle'''
        fill(255, 255, 0)
        noStroke()
        circle(self.X, self.Y, self.rad)
