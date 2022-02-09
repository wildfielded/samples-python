#!/usr/bin/python3

import sys
from random import choice

from PyQt5.QtCore import QCoreApplication, Qt, QSize
from PyQt5.QtWidgets import (QApplication,
                             QWidget, QDesktopWidget, QPushButton, QLabel,
                             QGridLayout, QHBoxLayout, QVBoxLayout)


#####=====----- Variables -----=====#####

FIELD_ROWS = 10
FIELD_COLS = 10
POS_LIST = [(row, col) for row in range(FIELD_ROWS) for col in range(FIELD_COLS)]
DUDE_WEIGHTS = (10, 8, 6, 4, 2)
COMP_WEIGHTS = (5, 4, 3, 2, 1)


#####=====----- Classes -----=====#####

class GameCell():
    ''' Объект одной клетки игрового поля в виде кнопки (butt) и с атрибутами
        координаты (pos), контента пусто/крестик/нолик (xo), весом для
        алгоритма выбора следующего хода (weight).
    '''
    def __init__(self):
        b_ = QPushButton('')
        b_.setFixedSize(QSize(30, 30))
        self.cell_dict = {
            'butt': b_,
            'pos': (0, 0),
            'xo': '.',
            'weight': 0,
        }


class GameField():
    ''' Весь массив клеток игрового поля
    '''
    def __init__(self):
        self.field_array = [[GameCell().cell_dict.copy() for col_ in range(FIELD_COLS)] \
                                                         for row_ in range(FIELD_ROWS)]
        for pos_ in POS_LIST:
            self.field_array[pos_[0]][pos_[1]]['pos'] = pos_


class OwenWindow(QWidget):
    ''' Основное окно игры
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

    def write_weights(self, row_, col_, xo_):
        ''' Запись весовых коэффициентов в атрибут ['xo'] объектов клеток поля.
        '''
        if xo_ == 'X':
            weights_tuple_ = DUDE_WEIGHTS
        else:
            weights_tuple_ = COMP_WEIGHTS
        self.gamefield.field_array[row_][col_]['weight'] += weights_tuple_[0]
        for s_ in range(1, 5):
            if col_ + s_ in range(FIELD_COLS):
                self.gamefield.field_array[row_][col_ + s_]['weight'] += weights_tuple_[s_]
            if col_ - s_ in range(FIELD_COLS):
                self.gamefield.field_array[row_][col_ - s_]['weight'] += weights_tuple_[s_]
            if row_ + s_ in range(FIELD_ROWS):
                self.gamefield.field_array[row_ + s_][col_]['weight'] += weights_tuple_[s_]
            if row_ - s_ in range(FIELD_ROWS):
                self.gamefield.field_array[row_ - s_][col_]['weight'] += weights_tuple_[s_]
            if (row_ + s_ in range(FIELD_ROWS)) and (col_ + s_ in range(FIELD_COLS)):
                self.gamefield.field_array[row_ + s_][col_ + s_]['weight'] += weights_tuple_[s_]
            if (row_ + s_ in range(FIELD_ROWS)) and (col_ - s_ in range(FIELD_COLS)):
                self.gamefield.field_array[row_ + s_][col_ - s_]['weight'] += weights_tuple_[s_]
            if (row_ - s_ in range(FIELD_ROWS)) and (col_ + s_ in range(FIELD_COLS)):
                self.gamefield.field_array[row_ - s_][col_ + s_]['weight'] += weights_tuple_[s_]
            if (row_ - s_ in range(FIELD_ROWS)) and (col_ - s_ in range(FIELD_COLS)):
                self.gamefield.field_array[row_ - s_][col_ - s_]['weight'] += weights_tuple_[s_]

    def check_line(self, row_, col_, xo_):
        ''' Проверяет наличие пяти X или O в линию и выдаёт сообщение в строке
            статуса, если есть.
        '''
        horiz_line_ = ''
        verti_line_ = ''
        risin_line_ = ''
        falln_line_ = ''
        looser_line_ = xo_ * 5
        for s_ in range(-4, 5):
            if col_ + s_ in range(FIELD_COLS):
                horiz_line_ += self.gamefield.field_array[row_][col_ + s_]['xo']
            if row_ + s_ in range(FIELD_ROWS):
                verti_line_ += self.gamefield.field_array[row_ + s_][col_]['xo']
            if (row_ - s_ in range(FIELD_ROWS)) and (col_ + s_ in range(FIELD_COLS)):
                risin_line_ += self.gamefield.field_array[row_ - s_][col_ + s_]['xo']
            if (row_ + s_ in range(FIELD_ROWS)) and (col_ + s_ in range(FIELD_COLS)):
                falln_line_ += self.gamefield.field_array[row_ + s_][col_ + s_]['xo']
        if (horiz_line_.find(looser_line_) > -1) or \
           (verti_line_.find(looser_line_) > -1) or \
           (risin_line_.find(looser_line_) > -1) or \
           (falln_line_.find(looser_line_) > -1):
            if xo_ == 'X':
                self.status_line_.setText(u'Вы проиграли! Начните заново.')
            if xo_ == 'O':
                self.status_line_.setText(u'Вы победили! Начните заново.')

    def check_end(self):
        ''' Выдаёт сообщение в строке статуса, когда не осталось свободных клеток.
        '''
        empty_cells_ = 0
        for row_ in self.gamefield.field_array:
            for cell_ in row_:
                if cell_['xo'] == '.':
                    empty_cells_ += 1
        if empty_cells_ == 0:
            self.status_line_.setText(u'Нет свободных клеток. Ничья! Начните заново.')

    def dude_answer(self, row_, col_):
        ''' Отображает ход игрока и проверяет "пять X в линию"
        '''
        self.gamefield.field_array[row_][col_]['butt'].setText('X')
        self.gamefield.field_array[row_][col_]['xo'] = 'X'
        self.write_weights(row_, col_, 'X')
        self.check_line(row_, col_, 'X')

    def comp_answer(self):
        ''' Ход компьютера. Отбирает свободные клетки с минимальным весом и уже
            из них выбирает одну для хода. Заносит данные в матрицу и проверяет
            "пять O в линию".
        '''
        candidates_ = []
        min_weight_ = 1000
        for row_ in self.gamefield.field_array:
            for cell_ in row_:
                if cell_['xo'] == '.':
                    if cell_['weight'] > min_weight_:
                        continue
                    elif cell_['weight'] == min_weight_:
                        candidates_.append(cell_['pos'])
                    else:
                        min_weight_ = cell_['weight']
                        candidates_.clear()
                        candidates_.append(cell_['pos'])
        (r_, c_) = choice(candidates_)
        self.gamefield.field_array[r_][c_]['butt'].setText('O')
        self.gamefield.field_array[r_][c_]['xo'] = 'O'
        self.write_weights(r_, c_, 'O')
        self.check_line(r_, c_, 'O')

    def put_signs(self, row_, col_):
        ''' Принимает ход игрока и делает ход компьютера
        '''
        def inner_function():
            if self.gamefield.field_array[row_][col_]['xo'] == '.':
                self.dude_answer(row_, col_)
                self.check_end()
                self.comp_answer()
                self.check_end()
        return inner_function

    def game_begin(self, who_first_):
        ''' Инициализирует новую игру. Делает первый ход компьютера, если
            выбрана соответствующая кнопка.
        '''
        for row_ in self.gamefield.field_array:
            for cell_ in row_:
                cell_['butt'].setText('')
                cell_['xo'] = '.'
                cell_['weight'] = 0
        self.status_line_.setText(u'Игра в процессе. Удачи!')
        if who_first_ == 2:
            self.comp_answer()

    def setup_main_win(self):
        ''' Создание главного окна программы
        '''
        self.setWindowTitle('Reversed Tic-Tac-Toe')
        self.setup_geom()

        button_dude_ = QPushButton(u'Начинает\nигрок (X)')
        button_dude_.setToolTip(u'Первый ход за игроком')
        button_dude_.clicked.connect(lambda: self.game_begin(1))
        button_comp_ = QPushButton(u'Начинает\nкомпьютер (0)')
        button_comp_.setToolTip(u'Первый ход за компьютером')
        button_comp_.clicked.connect(lambda: self.game_begin(2))
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
            bu_ = self.gamefield.field_array[pos_[0]][pos_[1]]['butt']
            bu_.clicked.connect(self.put_signs(*pos_))
            self.gamefield_layout_.addWidget(bu_, *pos_)

        self.status_line_ = QLabel()
        self.status_line_.setText(u'Вы играете крестиками. Компьютер - ноликами.\nВыберите, кто сделает первый ход.')
        self.bottom_layout_ = QHBoxLayout()
        self.bottom_layout_.addWidget(self.status_line_)
        self.bottom_layout_.addWidget(button_exit_)

        main_layout_ = QVBoxLayout()
        main_layout_.addLayout(self.toolbar_layout_)
        main_layout_.addLayout(self.gamefield_layout_)
        main_layout_.addLayout(self.bottom_layout_)
        self.setLayout(main_layout_)


#####=====----- MAIN -----=====#####

if __name__ == '__main__':
    app_ = QApplication([])
    prog_window_ = OwenWindow()
    prog_window_.show()
    sys.exit(app_.exec_())

#####=====----- THE END -----=====########################################