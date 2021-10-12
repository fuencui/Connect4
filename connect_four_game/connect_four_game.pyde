from game_controller import GameController
# Fuen Cui GitHub:
# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-FuenCui.git


SPACE = {"w": 700, "h": 700}
# w is width h is length
Space_on_row = 6
# space_on_row is how many space on a row
gc = GameController(Space_on_row, SPACE["w"], SPACE["h"])


def setup():
    '''prossesing background setup'''
    size(SPACE["w"], SPACE["h"])
    noStroke()
    background(200, 200, 200)


def draw():
    '''prossesing drawing'''
    background(200, 200, 200)
    gc.update()
    if mousePressed:
        gc.control_mouse_press(mouseX, mouseY)


def mousePressed():
    '''mousePressed'''
    gc.control_mouse_press(mouseX, mouseY)


def mouseReleased():
    '''mouseReleased'''
    gc.control_mouse_up()
