#!/usr/bin/python3

import sys

from PyQt5.QtCore import QCoreApplication, Qt, QSize
from PyQt5.QtWidgets import (QApplication,
                             QWidget, QDesktopWidget, QPushButton,
                             QGridLayout, QHBoxLayout, QVBoxLayout)


#####=====----- Variables -----=====#####

FIELD_ROWS = 10
FIELD_COLS = 10


#####=====----- Classes -----=====#####

class OwenWindow(QWidget):
    ''' Основное окно
    '''
    def __init__(self):
        super().__init__()
        self.setup_main_win()

    def setup_geom(self):
        ''' Задаёт размер и центрирует окно
        '''
        self.resize(400, 400)
        win_geom_ = self.frameGeometry()
        win_center_ = QDesktopWidget().availableGeometry().center()
        win_geom_.moveCenter(win_center_)
        self.move(win_geom_.topLeft())

    def put_cross(self, bobj_, tup_):
        bobj_.setText('X')

    def setup_gamefield(self, rows_, cols_):
        butt_array_ = [(r_, c_) for r_ in range(rows_) for c_ in range(cols_)]
        for butt_ in butt_array_:
            b_ = QPushButton('')
            b_.setFixedSize(QSize(30, 30))
            #####b_.clicked.connect(lambda: b_.setText('X'))
            b_.clicked.connect(lambda: self.put_cross(b_, butt_))
            self.gamefield_layout_.addWidget(b_, *butt_)

    def setup_main_win(self):
        self.setWindowTitle('OWEN')
        self.setup_geom()

        button_dude_ = QPushButton(u'Начинает\nигрок (X)')
        button_dude_.setToolTip(u'Первый ход за игроком')
        button_comp_ = QPushButton(u'Начинает\nкомпьютер (0)')
        button_comp_.setToolTip(u'Первый ход за компьютером')
        #####button_exit_ = QPushButton(u'Выход')
        #####button_exit_.setToolTip(u'Выход из программы')
        #####button_exit_.clicked.connect(QCoreApplication.instance().quit)

        toolbar_layout_ = QHBoxLayout()
        toolbar_layout_.addWidget(button_dude_)
        toolbar_layout_.addWidget(button_comp_)
        #####toolbar_layout_.addWidget(button_exit_)

        butt_array_ = [(x, y) for x in range(5) for y in range(5)]
        butt_unit_ = QPushButton('X')
        self.gamefield_layout_ = QGridLayout()
        self.gamefield_layout_.setSpacing(0)
        self.setup_gamefield(FIELD_ROWS, FIELD_COLS)

        main_layout_ = QVBoxLayout()
        main_layout_.addLayout(toolbar_layout_)
        main_layout_.addLayout(self.gamefield_layout_)
        self.setLayout(main_layout_)


#####=====----- Функции -----=====#####

#####=====----- MAIN -----=====#####

if __name__ == '__main__':
    app_ = QApplication([])
    prog_window_ = OwenWindow()
    prog_window_.show()
    sys.exit(app_.exec_())

#####=====----- THE END -----=====########################################