#!/usr/bin/python3

from random import choice


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

def dude_answer(array_, row_, col_):
    array_[row_][col_]['xo'] = 'X'
    array_[row_][col_]['weight'] += DUDE_WEIGHTS[0]
    for s_ in range(1, 5):
        if col_ + s_ in range(FIELD_COLS):
            array_[row_][col_ + s_]['weight'] += DUDE_WEIGHTS[s_]
        if col_ - s_ in range(FIELD_COLS):
            array_[row_][col_ - s_]['weight'] += DUDE_WEIGHTS[s_]
        if row_ + s_ in range(FIELD_ROWS):
            array_[row_ + s_][col_]['weight'] += DUDE_WEIGHTS[s_]
        if row_ - s_ in range(FIELD_ROWS):
            array_[row_ - s_][col_]['weight'] += DUDE_WEIGHTS[s_]
        if (row_ + s_ in range(FIELD_ROWS)) and (col_ + s_ in range(FIELD_COLS)):
            array_[row_ + s_][col_ + s_]['weight'] += DUDE_WEIGHTS[s_]
        if (row_ + s_ in range(FIELD_ROWS)) and (col_ - s_ in range(FIELD_COLS)):
            array_[row_ + s_][col_ - s_]['weight'] += DUDE_WEIGHTS[s_]
        if (row_ - s_ in range(FIELD_ROWS)) and (col_ + s_ in range(FIELD_COLS)):
            array_[row_ - s_][col_ + s_]['weight'] += DUDE_WEIGHTS[s_]
        if (row_ - s_ in range(FIELD_ROWS)) and (col_ - s_ in range(FIELD_COLS)):
            array_[row_ - s_][col_ - s_]['weight'] += DUDE_WEIGHTS[s_]

def comp_answer(array_):
    candidates_ = []

def put_cross(array_, str_):
    list_ = str_.strip().split('/')
    row_ = int(list_[0])
    col_ = int(list_[1])
    if array_[row_][col_]['xo'] == '.':
        dude_answer(array_, row_, col_)
        comp_answer(array_)
    else:
        print('\n\n\n\n\n\n\n\n\n\n')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print(u'ОШИБКА!!! Клетка занята. Поробуйте другую.')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')

def game_cycle(array_):
    coords = ''
    while True:
        print_weight(array_)
        print_field(array_)
        str1_ = u'Введите [N|n] для выхода из программы, или\n'
        str2_ = u'Координаты крестика числами в формате "строка/столбец": '
        coords = input(str1_ + str2_)
        if coords in ('n', 'N'):
            break
        try:
            put_cross(array_, coords)
        except:
            m_ = input(u'Ошибка ввода. Нажмите любую клавишу и пробуйте ещё раз:')


#####=====----- MAIN -----=====#####

if __name__ == '__main__':
    cell_obj = GameCell()
    cell_array = [[cell_obj.cell_dict.copy() for col in range(FIELD_COLS)] \
                                             for row in range(FIELD_ROWS)]
    for pos_ in POS_LIST:
        cell_array[pos_[0]][pos_[1]]['pos'] = pos_
    game_cycle(cell_array)

#####=====----- THE END -----=====########################################