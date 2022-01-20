#!/usr/bin/python3

import sys

from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import (QApplication,
                             QWidget, QDesktopWidget, QPushButton,
                             QGridLayout, QHBoxLayout, QVBoxLayout)

#####=====----- Классы -----=====#####

class OwenWindow(QWidget):
    ''' Основное окно
    '''
    def __init__(self):
        super().__init__()
        self.setup_main_win()

    def setup_geom(self):
        ''' Задаёт размер и центрирует окно
        '''
        self.resize(800, 800)
        win_geom_ = self.frameGeometry()
        win_center_ = QDesktopWidget().availableGeometry().center()
        win_geom_.moveCenter(win_center_)
        self.move(win_geom_.topLeft())

    def setup_main_win(self):
        self.setWindowTitle('OWEN')
        self.setup_geom()

        button_dude_ = QPushButton(u'Начинает\nигрок (X)')
        button_dude_.setToolTip(u'Первый ход за игроком')
        button_comp_ = QPushButton(u'Начинает\nкомпьютер (0)')
        button_comp_.setToolTip(u'Первый ход за компьютером')
        button_exit_ = QPushButton(u'Выход')
        button_exit_.setToolTip(u'Выход из программы')
        button_exit_.clicked.connect(QCoreApplication.instance().quit)

        toolbar_layout_ = QHBoxLayout()
        toolbar_layout_.addWidget(button_dude_)
        toolbar_layout_.addWidget(button_comp_)
        toolbar_layout_.addWidget(button_exit_)

        butt_array_ = [(x, y) for x in range(5) for y in range(5)]
        butt_unit_ = QPushButton('X')
        gamefield_layout_ = QGridLayout()
        gamefield_layout_.addWidget(QPushButton(''), 0, 0)
        gamefield_layout_.addWidget(QPushButton(''), 0, 1)
        gamefield_layout_.addWidget(QPushButton(''), 0, 2)
        gamefield_layout_.addWidget(QPushButton(''), 0, 3)
        gamefield_layout_.addWidget(QPushButton(''), 0, 4)
        gamefield_layout_.addWidget(QPushButton(''), 0, 5)
        gamefield_layout_.addWidget(QPushButton(''), 0, 6)
        gamefield_layout_.addWidget(QPushButton(''), 0, 7)
        gamefield_layout_.addWidget(QPushButton(''), 0, 8)
        gamefield_layout_.addWidget(QPushButton(''), 0, 9)
        gamefield_layout_.addWidget(QPushButton(''), 1, 0)
        gamefield_layout_.addWidget(QPushButton(''), 1, 1)
        gamefield_layout_.addWidget(QPushButton(''), 1, 2)
        gamefield_layout_.addWidget(QPushButton(''), 1, 3)
        gamefield_layout_.addWidget(QPushButton(''), 1, 4)
        gamefield_layout_.addWidget(QPushButton(''), 1, 5)
        gamefield_layout_.addWidget(QPushButton(''), 1, 6)
        gamefield_layout_.addWidget(QPushButton(''), 1, 7)
        gamefield_layout_.addWidget(QPushButton(''), 1, 8)
        gamefield_layout_.addWidget(QPushButton(''), 1, 9)
        gamefield_layout_.addWidget(QPushButton(''), 2, 0)
        gamefield_layout_.addWidget(QPushButton(''), 2, 1)
        gamefield_layout_.addWidget(QPushButton(''), 2, 2)
        gamefield_layout_.addWidget(QPushButton(''), 2, 3)
        gamefield_layout_.addWidget(QPushButton(''), 2, 4)
        gamefield_layout_.addWidget(QPushButton(''), 2, 5)
        gamefield_layout_.addWidget(QPushButton(''), 2, 6)
        gamefield_layout_.addWidget(QPushButton(''), 2, 7)
        gamefield_layout_.addWidget(QPushButton(''), 2, 8)
        gamefield_layout_.addWidget(QPushButton(''), 2, 9)

        main_layout_ = QVBoxLayout()
        main_layout_.addLayout(toolbar_layout_)
        main_layout_.addLayout(gamefield_layout_)
        self.setLayout(main_layout_)


#####=====----- Функции -----=====#####

#####=====----- Собственно, сама программа -----=====#####

if __name__ == '__main__':
    app_ = QApplication([])
    prog_window_ = OwenWindow()
    prog_window_.show()
    sys.exit(app_.exec_())

#####=====----- THE END -----=====########################################