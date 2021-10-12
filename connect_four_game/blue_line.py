# Fuen Cui GitHub:
# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-FuenCui.git

class Blueline:
    '''
    The blue border backboard for connect four game
    Every line from follow method change with background change
    '''
    def __init__(self, size):
        self.size = size

    def horizontal_line(self, width, temp):
        '''one single horizontal blue line'''
        BLUE = (0, 0, 255)
        STROKE_WEIGHT = 20
        stroke(*BLUE)
        strokeWeight(STROKE_WEIGHT)
        line(0, temp, width, temp)

    def vertical_line(self, temp, length):
        '''one single vertical blue line'''
        BLUE = (0, 0, 255)
        STROKE_WEIGHT = 20
        hori_start = length/(self.size + 1)
        stroke(*BLUE)
        strokeWeight(STROKE_WEIGHT)
        line(temp, hori_start, temp, length)

    def surround(self, width, length):
        '''surround frame'''
        BLUE = (0, 0, 255)
        STROKE_WEIGHT = 10
        stroke(*BLUE)
        strokeWeight(STROKE_WEIGHT)
        FIRSTX = 0
        FIRSTY = length/(self.size + 1)
        FIRSTENDX = 0
        FIRSTENDY = length
        SENENDX = width
        SENENDY = length
        THIENDX = width
        THIENDY = length/(self.size + 1)
        line(FIRSTX, FIRSTY, FIRSTENDX, FIRSTENDY)
        line(FIRSTENDX, FIRSTENDY, THIENDX, FIRSTENDY)
        line(THIENDX, FIRSTENDY, THIENDX, THIENDY)
