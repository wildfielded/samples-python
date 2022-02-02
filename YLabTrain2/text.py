#!/usr/bin/python3

from random import choice
from sys import exit


#####=====----- Variables -----=====#####

FIELD_ROWS = 10
FIELD_COLS = 10
POS_LIST = [(row, col) for row in range(FIELD_ROWS) for col in range(FIELD_COLS)]
DUDE_WEIGHTS = (10, 8, 6, 4, 2)
COMP_WEIGHTS = (5, 4, 3, 2, 1)


#####=====----- Classes -----=====#####

class GameCell():
    def __init__(self):
        self.cell_dict = {
            'pos': (0, 0),
            'xo': '.',
            'weight': 0
        }


#####=====----- Functions -----=====#####

def print_field(array_):
    str_ = '  '
    for col_ in range(FIELD_COLS):
        str_ += (str(col_) + ' ')
    print(str_)
    rn_ = 0
    for row_ in array_:
        str_ = str(rn_) + ' '
        for cell_ in row_:
            str_ += (cell_['xo'] + ' ')
        rn_ += 1
        print(str_)

'''
def print_weight(array_):
    str_ = '  '
    for col_ in range(FIELD_COLS):
        str_ += (str(col_) + ' ')
    print(str_)
    rn_ = 0
    for row_ in array_:
        str_ = str(rn_) + ' '
        for cell_ in row_:
            str_ += (str(cell_['weight']) + ' ')
        rn_ += 1
        print(str_)
'''

def write_weights(array_, r_, c_, xo_):
    if xo_ == 'X':
        weights_tuple_ = DUDE_WEIGHTS
    else:
        weights_tuple_ = COMP_WEIGHTS
    array_[r_][c_]['weight'] += weights_tuple_[0]
    for s_ in range(1, 5):
        if c_ + s_ in range(FIELD_COLS):
            array_[r_][c_ + s_]['weight'] += weights_tuple_[s_]
        if c_ - s_ in range(FIELD_COLS):
            array_[r_][c_ - s_]['weight'] += weights_tuple_[s_]
        if r_ + s_ in range(FIELD_ROWS):
            array_[r_ + s_][c_]['weight'] += weights_tuple_[s_]
        if r_ - s_ in range(FIELD_ROWS):
            array_[r_ - s_][c_]['weight'] += weights_tuple_[s_]
        if (r_ + s_ in range(FIELD_ROWS)) and (c_ + s_ in range(FIELD_COLS)):
            array_[r_ + s_][c_ + s_]['weight'] += weights_tuple_[s_]
        if (r_ + s_ in range(FIELD_ROWS)) and (c_ - s_ in range(FIELD_COLS)):
            array_[r_ + s_][c_ - s_]['weight'] += weights_tuple_[s_]
        if (r_ - s_ in range(FIELD_ROWS)) and (c_ + s_ in range(FIELD_COLS)):
            array_[r_ - s_][c_ + s_]['weight'] += weights_tuple_[s_]
        if (r_ - s_ in range(FIELD_ROWS)) and (c_ - s_ in range(FIELD_COLS)):
            array_[r_ - s_][c_ - s_]['weight'] += weights_tuple_[s_]

def check_five(array_, row_, col_, xo_):
    horz_ = ''
    vert_ = ''
    rise_ = ''
    fall_ = ''
    looser_line_ = xo_ * 5
    for s_ in range(-4, 5):
        if col_ + s_ in range(FIELD_COLS):
            horz_ += array_[row_][col_ + s_]['xo']
        if row_ + s_ in range(FIELD_ROWS):
            vert_ += array_[row_ + s_][col_]['xo']
        if (row_ - s_ in range(FIELD_ROWS)) and (col_ + s_ in range(FIELD_COLS)):
            rise_ += array_[row_ - s_][col_ + s_]['xo']
        if (row_ + s_ in range(FIELD_ROWS)) and (col_ + s_ in range(FIELD_COLS)):
            fall_ += array_[row_ + s_][col_ + s_]['xo']
    if (horz_.find(looser_line_) > -1) or \
       (vert_.find(looser_line_) > -1) or \
       (rise_.find(looser_line_) > -1) or \
       (fall_.find(looser_line_) > -1):
        if xo_ == 'X':
            print_field(array_)
            print(u'Вы проиграли!')
        if xo_ == 'O':
            print_field(array_)
            print(u'Вы победили!')
        exit()

def check_end(array_):
    empty_cells_ = 0
    for row_ in array_:
        for cell_ in row_:
            if cell_['xo'] == '.':
                empty_cells_ += 1
    if empty_cells_ == 0:
        print(u'Нет свободных клеток. Ничья!')
        exit()

def dude_answer(array_, row_, col_):
    array_[row_][col_]['xo'] = 'X'
    write_weights(array_, row_, col_, 'X')
    check_five(array_, row_, col_, 'X')

def comp_answer(array_):
    candidates_ = []
    min_weight_ = 1000
    for row_ in array_:
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
    array_[r_][c_]['xo'] = 'O'
    write_weights(array_, r_, c_, 'O')
    check_five(array_, r_, c_, 'O')

def put_signs(array_, str_):
    list_ = str_.split('/')
    if list_[0].strip().isdigit() and list_[1].strip().isdigit():
        row_ = int(list_[0])
        col_ = int(list_[1])
        if row_ < FIELD_ROWS and col_ < FIELD_COLS:
            if array_[row_][col_]['xo'] == '.':
                dude_answer(array_, row_, col_)
                check_end(array_)
                comp_answer(array_)
                check_end(array_)
            else:
                print('\n\n\n\n\n\n\n\n\n\n')
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                print(u'ОШИБКА!!! Клетка занята. Поробуйте другую.')
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
        else:
            m_ = input(u'Превышен диапазон. Нажмите любую клавишу и пробуйте ещё раз:')
    else:
        m_ = input(u'Ошибка ввода. Нажмите любую клавишу и пробуйте ещё раз:')

def game_cycle(array_, who_first_):
    coords = ''
    if who_first_ == '2':
        comp_answer(array_)
    while True:
        #####print_weight(array_)#####!!!!! TEMPORAL !!!!!#####
        print_field(array_)
        str1_ = u'Введите [Q|q] для выхода из программы, или\n'
        str2_ = u'Координаты крестика числами в формате "строка/столбец": '
        coords = input(str1_ + str2_)
        if coords in ('Q', 'q'):
            break
        put_signs(array_, coords)


#####=====----- MAIN -----=====#####

if __name__ == '__main__':
    cell_obj = GameCell()
    cell_array = [[cell_obj.cell_dict.copy() for col in range(FIELD_COLS)] \
                                             for row in range(FIELD_ROWS)]
    for pos_ in POS_LIST:
        cell_array[pos_[0]][pos_[1]]['pos'] = pos_
    who_first = input(u'Вы играете крестиками. Компьютер - ноликами.\n' + \
                      u'Кто делает первый ход? 1 - игрок, 2 - компьютер: ')
    game_cycle(cell_array, who_first)

#####=====----- THE END -----=====########################################