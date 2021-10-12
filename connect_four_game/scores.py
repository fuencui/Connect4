# Fuen Cui GitHub:
# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-FuenCui.git

class Scores:
    def __init__(self):
        self.dalay = 100
        self.start = 0
        self.player_dict = {}

    def count(self, win=True):
        self.win = win
        if self.start < self.dalay:
            self.start += 1
        if self.start == self.dalay:
            self.name_scores(self.win)
            self.start += 1

    def name_scores(self, temp):
        self.temp = temp
        answer = self.input('enter your name')
        if answer:
            if self.temp is True:
                print('hi ' + answer)
                self.read_txt(answer)
                self.write_txt()
            elif self.temp is False:
                print('hi ' + answer)
                print('not be counted')
        elif answer == '':
            print('[empty string]')
        else:
            print(answer)  # Canceled dialog will print None

    def read_txt(self, name):
        self.name = name
        self.name = self.name.capitalize()
        try:
            f = open("scores.txt", "r")
        except IOError:
            self.player_dict[self.name] = 1
            return

        info = f.read()
        self.line = info.split()
        if len(self.line) != 0:
            for _i in range(len(self.line)):
                if _i % 2 == 0:
                    self.player_dict[self.line[_i]] = int(self.line[(_i + 1)])
        if self.name in self.player_dict.keys():
            self.player_dict[self.name] = self.player_dict[self.name] + 1
        else:
            self.player_dict[self.name] = 1
        return self.player_dict

    def write_txt(self):
        try:
            out = open("scores.txt", "w")
        except OSError as e:
            print("Unable to open reprot.txt for writing")
            return
        self.player_dict = sorted(
            self.player_dict.items(),
            key=lambda x: x[1],
            reverse=True
        )

        for item in self.player_dict:
            out.write(item[0] + ' ' + str(item[1]) + '\n')

    def input(self, message=''):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)
