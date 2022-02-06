#!/usr/bin/python3

import sys

from PyQt5.QtCore import QCoreApplication, Qt, QSize
from PyQt5.QtWidgets import (QApplication,
                             QWidget, QDesktopWidget, QPushButton, QLabel,
                             QGridLayout, QHBoxLayout, QVBoxLayout)

##### Импорт игровой логики из консольного варианта игры
import cli_mode as gl_


#####=====----- Variables -----=====#####

FIELD_ROWS = 10
FIELD_COLS = 10


#####=====----- Classes -----=====#####

class GameCell():
    ''' Одиночная игровая клетка
    '''
    def __init__(self):
        b_ = QPushButton('')
        b_.setFixedSize(QSize(30, 30))
        self.cell_dict = {
            'butt': b_,
            'pos': tuple(),
            'xo': '',
            'weight': 0,
        }


class GameField():
    ''' Весь массив клеток игрового поля
    '''
    def __init__(self):
        self.field = [[GameCell().cell_dict for col_ in range(FIELD_COLS)] for row_ in range(FIELD_ROWS)]
        for pos_ in POS_LIST:
            self.field[pos_[0]][pos_[1]]['pos'] = pos_
            #####self.field[pos_[0]][pos_[1]]['butt'].clicked.connect(lambda: self.butt_clicked(pos_))

    def butt_clicked(self, tup_):
        self.field[tup_[0]][tup_[1]]['butt'].setText('X')
        print(tup_)


class OwenWindow(QWidget):
    ''' Основное окно
    '''
    def __init__(self):
        super().__init__()
        self.gamefield = GameField()
        self.setup_main_win()

    def setup_geom(self):
        ''' Задаёт размер и центрирует окно
        '''
        self.resize(330, 400)
        win_geom_ = self.frameGeometry()
        win_center_ = QDesktopWidget().availableGeometry().center()
        win_geom_.moveCenter(win_center_)
        self.move(win_geom_.topLeft())

    def put_cross(self, bu_, pos_):
        #####self.gamefield.field[pos_[0]][pos_[1]]['butt'].setText('X')
        bu_.setText('X')

    def setup_main_win(self):
        self.setWindowTitle('Reversed Tic-Tac-Toe')
        self.setup_geom()

        button_dude_ = QPushButton(u'Начинает\nигрок (X)')
        button_dude_.setToolTip(u'Первый ход за игроком')
        button_comp_ = QPushButton(u'Начинает\nкомпьютер (0)')
        button_comp_.setToolTip(u'Первый ход за компьютером')
        button_exit_ = QPushButton(u'Выход')
        button_exit_.setFixedSize(60, 30)
        button_exit_.setToolTip(u'Выход из программы')
        button_exit_.clicked.connect(QCoreApplication.instance().quit)

        self.toolbar_layout_ = QHBoxLayout()
        self.toolbar_layout_.addWidget(button_dude_)
        self.toolbar_layout_.addWidget(button_comp_)

        self.gamefield_layout_ = QGridLayout()
        self.gamefield_layout_.setSpacing(0)
        for pos_ in POS_LIST:
            bu_ = self.gamefield.field[pos_[0]][pos_[1]]['butt']
            bu_.clicked.connect(lambda: self.put_cross(bu_, pos_))
            self.gamefield_layout_.addWidget(bu_, *pos_)

        status_line_ = QLabel()
        status_line_.setText('Ready to play. Choose who first.')
        self.bottom_layout_ = QHBoxLayout()
        self.bottom_layout_.addWidget(status_line_)
        self.bottom_layout_.addWidget(button_exit_)

        main_layout_ = QVBoxLayout()
        main_layout_.addLayout(self.toolbar_layout_)
        main_layout_.addLayout(self.gamefield_layout_)
        main_layout_.addLayout(self.bottom_layout_)
        self.setLayout(main_layout_)


#####=====----- Функции -----=====#####

#####=====----- MAIN -----=====#####

if __name__ == '__main__':
    POS_LIST = [(row_, col_) for row_ in range(FIELD_ROWS) for col_ in range(FIELD_COLS)]
    app_ = QApplication([])
    prog_window_ = OwenWindow()
    prog_window_.show()
    sys.exit(app_.exec_())

#####=====----- THE END -----=====########################################