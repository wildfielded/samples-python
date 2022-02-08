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
        if self.gamefield.field_array[row_][col_]['xo'] == '.':
            self.dude_answer(row_, col_)
            self.check_end()
            self.comp_answer()
            self.check_end()

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
            #####bu_.clicked.connect(lambda: self.put_signs(bu_, pos_))
            self.gamefield_layout_.addWidget(bu_, *pos_)
        ''' Ниже начинается позорный костыль, потому что не отработались привязки
            событий к слотам в цикле FOR выше (закомментированная строка).
            Пришлось пока захардкодить.
        '''
        bu00_ = self.gamefield.field_array[0][0]['butt']
        bu00_.clicked.connect(lambda: self.put_signs(0, 0))
        bu01_ = self.gamefield.field_array[0][1]['butt']
        bu01_.clicked.connect(lambda: self.put_signs(0, 1))
        bu02_ = self.gamefield.field_array[0][2]['butt']
        bu02_.clicked.connect(lambda: self.put_signs(0, 2))
        bu03_ = self.gamefield.field_array[0][3]['butt']
        bu03_.clicked.connect(lambda: self.put_signs(0, 3))
        bu04_ = self.gamefield.field_array[0][4]['butt']
        bu04_.clicked.connect(lambda: self.put_signs(0, 4))
        bu05_ = self.gamefield.field_array[0][5]['butt']
        bu05_.clicked.connect(lambda: self.put_signs(0, 5))
        bu06_ = self.gamefield.field_array[0][6]['butt']
        bu06_.clicked.connect(lambda: self.put_signs(0, 6))
        bu07_ = self.gamefield.field_array[0][7]['butt']
        bu07_.clicked.connect(lambda: self.put_signs(0, 7))
        bu08_ = self.gamefield.field_array[0][8]['butt']
        bu08_.clicked.connect(lambda: self.put_signs(0, 8))
        bu09_ = self.gamefield.field_array[0][9]['butt']
        bu09_.clicked.connect(lambda: self.put_signs(0, 9))
        bu10_ = self.gamefield.field_array[1][0]['butt']
        bu10_.clicked.connect(lambda: self.put_signs(1, 0))
        bu11_ = self.gamefield.field_array[1][1]['butt']
        bu11_.clicked.connect(lambda: self.put_signs(1, 1))
        bu12_ = self.gamefield.field_array[1][2]['butt']
        bu12_.clicked.connect(lambda: self.put_signs(1, 2))
        bu13_ = self.gamefield.field_array[1][3]['butt']
        bu13_.clicked.connect(lambda: self.put_signs(1, 3))
        bu14_ = self.gamefield.field_array[1][4]['butt']
        bu14_.clicked.connect(lambda: self.put_signs(1, 4))
        bu15_ = self.gamefield.field_array[1][5]['butt']
        bu15_.clicked.connect(lambda: self.put_signs(1, 5))
        bu16_ = self.gamefield.field_array[1][6]['butt']
        bu16_.clicked.connect(lambda: self.put_signs(1, 6))
        bu17_ = self.gamefield.field_array[1][7]['butt']
        bu17_.clicked.connect(lambda: self.put_signs(1, 7))
        bu18_ = self.gamefield.field_array[1][8]['butt']
        bu18_.clicked.connect(lambda: self.put_signs(1, 8))
        bu19_ = self.gamefield.field_array[1][9]['butt']
        bu19_.clicked.connect(lambda: self.put_signs(1, 9))
        bu20_ = self.gamefield.field_array[2][0]['butt']
        bu20_.clicked.connect(lambda: self.put_signs(2, 0))
        bu21_ = self.gamefield.field_array[2][1]['butt']
        bu21_.clicked.connect(lambda: self.put_signs(2, 1))
        bu22_ = self.gamefield.field_array[2][2]['butt']
        bu22_.clicked.connect(lambda: self.put_signs(2, 2))
        bu23_ = self.gamefield.field_array[2][3]['butt']
        bu23_.clicked.connect(lambda: self.put_signs(2, 3))
        bu24_ = self.gamefield.field_array[2][4]['butt']
        bu24_.clicked.connect(lambda: self.put_signs(2, 4))
        bu25_ = self.gamefield.field_array[2][5]['butt']
        bu25_.clicked.connect(lambda: self.put_signs(2, 5))
        bu26_ = self.gamefield.field_array[2][6]['butt']
        bu26_.clicked.connect(lambda: self.put_signs(2, 6))
        bu27_ = self.gamefield.field_array[2][7]['butt']
        bu27_.clicked.connect(lambda: self.put_signs(2, 7))
        bu28_ = self.gamefield.field_array[2][8]['butt']
        bu28_.clicked.connect(lambda: self.put_signs(2, 8))
        bu29_ = self.gamefield.field_array[2][9]['butt']
        bu29_.clicked.connect(lambda: self.put_signs(2, 9))
        bu30_ = self.gamefield.field_array[3][0]['butt']
        bu30_.clicked.connect(lambda: self.put_signs(3, 0))
        bu31_ = self.gamefield.field_array[3][1]['butt']
        bu31_.clicked.connect(lambda: self.put_signs(3, 1))
        bu32_ = self.gamefield.field_array[3][2]['butt']
        bu32_.clicked.connect(lambda: self.put_signs(3, 2))
        bu33_ = self.gamefield.field_array[3][3]['butt']
        bu33_.clicked.connect(lambda: self.put_signs(3, 3))
        bu34_ = self.gamefield.field_array[3][4]['butt']
        bu34_.clicked.connect(lambda: self.put_signs(3, 4))
        bu35_ = self.gamefield.field_array[3][5]['butt']
        bu35_.clicked.connect(lambda: self.put_signs(3, 5))
        bu36_ = self.gamefield.field_array[3][6]['butt']
        bu36_.clicked.connect(lambda: self.put_signs(3, 6))
        bu37_ = self.gamefield.field_array[3][7]['butt']
        bu37_.clicked.connect(lambda: self.put_signs(3, 7))
        bu38_ = self.gamefield.field_array[3][8]['butt']
        bu38_.clicked.connect(lambda: self.put_signs(3, 8))
        bu39_ = self.gamefield.field_array[3][9]['butt']
        bu39_.clicked.connect(lambda: self.put_signs(3, 9))
        bu40_ = self.gamefield.field_array[4][0]['butt']
        bu40_.clicked.connect(lambda: self.put_signs(4, 0))
        bu41_ = self.gamefield.field_array[4][1]['butt']
        bu41_.clicked.connect(lambda: self.put_signs(4, 1))
        bu42_ = self.gamefield.field_array[4][2]['butt']
        bu42_.clicked.connect(lambda: self.put_signs(4, 2))
        bu43_ = self.gamefield.field_array[4][3]['butt']
        bu43_.clicked.connect(lambda: self.put_signs(4, 3))
        bu44_ = self.gamefield.field_array[4][4]['butt']
        bu44_.clicked.connect(lambda: self.put_signs(4, 4))
        bu45_ = self.gamefield.field_array[4][5]['butt']
        bu45_.clicked.connect(lambda: self.put_signs(4, 5))
        bu46_ = self.gamefield.field_array[4][6]['butt']
        bu46_.clicked.connect(lambda: self.put_signs(4, 6))
        bu47_ = self.gamefield.field_array[4][7]['butt']
        bu47_.clicked.connect(lambda: self.put_signs(4, 7))
        bu48_ = self.gamefield.field_array[4][8]['butt']
        bu48_.clicked.connect(lambda: self.put_signs(4, 8))
        bu49_ = self.gamefield.field_array[4][9]['butt']
        bu49_.clicked.connect(lambda: self.put_signs(4, 9))
        bu50_ = self.gamefield.field_array[5][0]['butt']
        bu50_.clicked.connect(lambda: self.put_signs(5, 0))
        bu51_ = self.gamefield.field_array[5][1]['butt']
        bu51_.clicked.connect(lambda: self.put_signs(5, 1))
        bu52_ = self.gamefield.field_array[5][2]['butt']
        bu52_.clicked.connect(lambda: self.put_signs(5, 2))
        bu53_ = self.gamefield.field_array[5][3]['butt']
        bu53_.clicked.connect(lambda: self.put_signs(5, 3))
        bu54_ = self.gamefield.field_array[5][4]['butt']
        bu54_.clicked.connect(lambda: self.put_signs(5, 4))
        bu55_ = self.gamefield.field_array[5][5]['butt']
        bu55_.clicked.connect(lambda: self.put_signs(5, 5))
        bu56_ = self.gamefield.field_array[5][6]['butt']
        bu56_.clicked.connect(lambda: self.put_signs(5, 6))
        bu57_ = self.gamefield.field_array[5][7]['butt']
        bu57_.clicked.connect(lambda: self.put_signs(5, 7))
        bu58_ = self.gamefield.field_array[5][8]['butt']
        bu58_.clicked.connect(lambda: self.put_signs(5, 8))
        bu59_ = self.gamefield.field_array[5][9]['butt']
        bu59_.clicked.connect(lambda: self.put_signs(5, 9))
        bu60_ = self.gamefield.field_array[6][0]['butt']
        bu60_.clicked.connect(lambda: self.put_signs(6, 0))
        bu61_ = self.gamefield.field_array[6][1]['butt']
        bu61_.clicked.connect(lambda: self.put_signs(6, 1))
        bu62_ = self.gamefield.field_array[6][2]['butt']
        bu62_.clicked.connect(lambda: self.put_signs(6, 2))
        bu63_ = self.gamefield.field_array[6][3]['butt']
        bu63_.clicked.connect(lambda: self.put_signs(6, 3))
        bu64_ = self.gamefield.field_array[6][4]['butt']
        bu64_.clicked.connect(lambda: self.put_signs(6, 4))
        bu65_ = self.gamefield.field_array[6][5]['butt']
        bu65_.clicked.connect(lambda: self.put_signs(6, 5))
        bu66_ = self.gamefield.field_array[6][6]['butt']
        bu66_.clicked.connect(lambda: self.put_signs(6, 6))
        bu67_ = self.gamefield.field_array[6][7]['butt']
        bu67_.clicked.connect(lambda: self.put_signs(6, 7))
        bu68_ = self.gamefield.field_array[6][8]['butt']
        bu68_.clicked.connect(lambda: self.put_signs(6, 8))
        bu69_ = self.gamefield.field_array[6][9]['butt']
        bu69_.clicked.connect(lambda: self.put_signs(6, 9))
        bu70_ = self.gamefield.field_array[7][0]['butt']
        bu70_.clicked.connect(lambda: self.put_signs(7, 0))
        bu71_ = self.gamefield.field_array[7][1]['butt']
        bu71_.clicked.connect(lambda: self.put_signs(7, 1))
        bu72_ = self.gamefield.field_array[7][2]['butt']
        bu72_.clicked.connect(lambda: self.put_signs(7, 2))
        bu73_ = self.gamefield.field_array[7][3]['butt']
        bu73_.clicked.connect(lambda: self.put_signs(7, 3))
        bu74_ = self.gamefield.field_array[7][4]['butt']
        bu74_.clicked.connect(lambda: self.put_signs(7, 4))
        bu75_ = self.gamefield.field_array[7][5]['butt']
        bu75_.clicked.connect(lambda: self.put_signs(7, 5))
        bu76_ = self.gamefield.field_array[7][6]['butt']
        bu76_.clicked.connect(lambda: self.put_signs(7, 6))
        bu77_ = self.gamefield.field_array[7][7]['butt']
        bu77_.clicked.connect(lambda: self.put_signs(7, 7))
        bu78_ = self.gamefield.field_array[7][8]['butt']
        bu78_.clicked.connect(lambda: self.put_signs(7, 8))
        bu79_ = self.gamefield.field_array[7][9]['butt']
        bu79_.clicked.connect(lambda: self.put_signs(7, 9))
        bu80_ = self.gamefield.field_array[8][0]['butt']
        bu80_.clicked.connect(lambda: self.put_signs(8, 0))
        bu81_ = self.gamefield.field_array[8][1]['butt']
        bu81_.clicked.connect(lambda: self.put_signs(8, 1))
        bu82_ = self.gamefield.field_array[8][2]['butt']
        bu82_.clicked.connect(lambda: self.put_signs(8, 2))
        bu83_ = self.gamefield.field_array[8][3]['butt']
        bu83_.clicked.connect(lambda: self.put_signs(8, 3))
        bu84_ = self.gamefield.field_array[8][4]['butt']
        bu84_.clicked.connect(lambda: self.put_signs(8, 4))
        bu85_ = self.gamefield.field_array[8][5]['butt']
        bu85_.clicked.connect(lambda: self.put_signs(8, 5))
        bu86_ = self.gamefield.field_array[8][6]['butt']
        bu86_.clicked.connect(lambda: self.put_signs(8, 6))
        bu87_ = self.gamefield.field_array[8][7]['butt']
        bu87_.clicked.connect(lambda: self.put_signs(8, 7))
        bu88_ = self.gamefield.field_array[8][8]['butt']
        bu88_.clicked.connect(lambda: self.put_signs(8, 8))
        bu89_ = self.gamefield.field_array[8][9]['butt']
        bu89_.clicked.connect(lambda: self.put_signs(8, 9))
        bu90_ = self.gamefield.field_array[9][0]['butt']
        bu90_.clicked.connect(lambda: self.put_signs(9, 0))
        bu91_ = self.gamefield.field_array[9][1]['butt']
        bu91_.clicked.connect(lambda: self.put_signs(9, 1))
        bu92_ = self.gamefield.field_array[9][2]['butt']
        bu92_.clicked.connect(lambda: self.put_signs(9, 2))
        bu93_ = self.gamefield.field_array[9][3]['butt']
        bu93_.clicked.connect(lambda: self.put_signs(9, 3))
        bu94_ = self.gamefield.field_array[9][4]['butt']
        bu94_.clicked.connect(lambda: self.put_signs(9, 4))
        bu95_ = self.gamefield.field_array[9][5]['butt']
        bu95_.clicked.connect(lambda: self.put_signs(9, 5))
        bu96_ = self.gamefield.field_array[9][6]['butt']
        bu96_.clicked.connect(lambda: self.put_signs(9, 6))
        bu97_ = self.gamefield.field_array[9][7]['butt']
        bu97_.clicked.connect(lambda: self.put_signs(9, 7))
        bu98_ = self.gamefield.field_array[9][8]['butt']
        bu98_.clicked.connect(lambda: self.put_signs(9, 8))
        bu99_ = self.gamefield.field_array[9][9]['butt']
        bu99_.clicked.connect(lambda: self.put_signs(9, 9))
        ''' Конец позорного костыля
        '''

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