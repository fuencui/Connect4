# Fuen Cui GitHub:
# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-FuenCui.git

from game_controller import GameController
from blue_line import Blueline
from disk import Disk
from animate import Animate
from scores import Scores
import random


def test_drop_control():
    '''test disk drop controller'''
    width = 700
    length = 700
    size = 6
    gc = GameController(size, width, length)
    assert gc.speed is True
    assert gc.game_stop is False
    gc.control_mouse_press(50, 650)
    gc.control_mouse_up()
    assert gc.drop_list == [[50, 50, False]]
    gc.control_mouse_press(50, 650)
    gc.control_mouse_up()
    assert gc.drop_list == [[50, 50, False], [50, 150, True]]
    gc.control_mouse_press(150, 650)
    gc.control_mouse_up()
    assert gc.drop_list == [[50, 50, False], [50, 150, True], [150, 50, False]]


def test_inspection_game():
    '''test inspection game method'''
    width = 700
    length = 700
    size = 6
    gc = GameController(size, width, length)
    gc.drop_list.append([150, 50, False])
    gc.drop_list.append([250, 50, False])
    gc.drop_list.append([350, 50, False])
    gc.drop_list.append([450, 50, False])
    assert gc.game_stop is False
    gc.inspection_game()
    assert gc.game_stop is True

    gc_2 = GameController(size, width, length)
    gc_2.drop_list.append([50, 50, True])
    gc_2.drop_list.append([50, 150, True])
    gc_2.drop_list.append([50, 250, True])
    gc_2.drop_list.append([50, 350, True])
    assert gc_2.game_stop is False
    gc_2.inspection_game()
    assert gc_2.game_stop is True


def test_computer_AI_3():
    '''test computer AI for 3 on a row'''
    width = 700
    length = 700
    size = 6
    gc = GameController(size, width, length)
    gc.drop_list.append([50, 50, True])
    gc.computer_AI_3()
    gc.control_mouse_up()
    assert gc.drop_list == [[50, 50, True], [50, 150, False]]
    gc.drop_list.append([150, 50, True])
    gc.drop_list.append([250, 50, True])
    gc.computer_AI_3()
    gc.control_mouse_up()
    assert gc.drop_list == [[50, 50, True], [50, 150, False],
                            [150, 50, True], [250, 50, True],
                            [350, 50, True]]
    gc.drop_list.pop()
    gc.drop_list.pop()
    gc.drop_list.pop()
    gc.drop_list.append([650, 50, True])
    gc.drop_list.append([550, 50, True])
    gc.drop_list.append([450, 50, True])
    gc.computer_AI_3()
    gc.control_mouse_up()
    assert gc.drop_list == [[50, 50, True], [50, 150, False],
                            [650, 50, True], [550, 50, True],
                            [450, 50, True], [350, 50, False]]


def test_computer_AI_2():
    '''test computer AI for 2 on a row'''
    width = 700
    length = 700
    size = 6
    gc = GameController(size, width, length)
    gc.drop_list.append([150, 50, True])
    gc.drop_list.append([250, 50, False])
    gc.drop_list.append([150, 150, True])
    gc.computer_AI_2()
    gc.control_mouse_up()
    assert gc.drop_list == [[150, 50, True], [250, 50, False],
                            [150, 150, True], [150, 250, False]]

    gc_2 = GameController(size, width, length)
    gc_2.drop_list.append([150, 50, True])
    gc_2.drop_list.append([150, 150, False])
    gc_2.drop_list.append([350, 50, True])
    gc_2.computer_AI_2()
    gc_2.control_mouse_up()
    assert gc_2.drop_list == [[150, 50, True], [150, 150, False],
                              [350, 50, True], [250, 50, False]]
