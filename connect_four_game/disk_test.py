# Fuen Cui GitHub:
# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-FuenCui.git

from disk import Disk


def test_control_press():
    '''test dick drop method'''
    width = 700
    length = 700
    size = 6
    dk = Disk(width, length, size)
    assert dk.check_color is True
    assert dk.control_press(50, 50) == [50, 150, 250, 350, 450, 550, 650]
    dk.control_up()
    assert dk.check_color is False
    assert dk.control_press(50, 50) == [50, 150, 250, 350, 450, 550, 650]
    assert dk.check_color is False
    assert dk.color_switch == [1]
