#!/usr/bin/python3

from random import choice
from sys import exit


''' =====----- Variables -----===== '''

FIELD_ROWS = 10
FIELD_COLS = 10
POS_LIST = [(row, col) for row in range(FIELD_ROWS) for col in range(FIELD_COLS)]
DUDE_WEIGHTS = (10, 8, 6, 4, 2)
COMP_WEIGHTS = (5, 4, 3, 2, 1)


''' =====----- Classes -----===== '''

class GameCell():
    def __init__(self):
        ''' The object is one cell on the playing field with the
        attributes of coordinates (pos), content empty/cross/zero (xo),
        and weight for the next step selection algorithm (weight).
        -----
        Объект одной клетки игрового поля с атрибутами координаты (pos),
        контента пусто/крестик/нолик (xo), весом для алгоритма выбора
        следующего хода (weight).
        '''
        self.cell_dict = {
            'pos': (0, 0),
            'xo': '.',
            'weight': 0
        }


''' =====----- Functions -----===== '''

def print_field(cell_array_):
    ''' Called in game_cycle().
    Prints the current state of the game field to the console
    -----
    Используется в game_cycle().
    Печать на консоль текущего состояния игрового поля
    Arguments:
        cell_array_ [list] -- Двумерный массив (список списков) объектов
            клетки игрового поля
    Returns:
        [stdout] -- Игровое поле в текстовом виде
    '''
    str_ = '   '
    for col_ in range(FIELD_COLS):
        str_ += (str(col_) + ' ')
    print(str_)
    print('   | | | | | | | | | |')
    row_num_ = 0
    for row_ in cell_array_:
        tmp_str_ = str(row_num_) + '--'
        for cell_ in row_:
            tmp_str_ += (cell_['xo'] + ' ')
        row_num_ += 1
        print(tmp_str_)

def write_weights(cell_array_, row_, col_, xo_):
    ''' Called in dude_answer() and comp_answer().
    Writes weight coefficients to the ['xo'] attribute of cell objects.
    -----
    Используется в dude_answer() и comp_answer().
    Запись весовых коэффициентов в атрибут ['xo'] объектов клеток поля.
    Arguments:
        cell_array_ [list] -- Двумерный массив (список списков) объектов
        row_, col_ [int] -- Номера строки и колонки клетки, в которой
            сделан ход
        xo_ [str] -- 'X' или 'O', в зависимости от того, чей был ход
    '''
    if xo_ == 'X':
        weights_tuple_ = DUDE_WEIGHTS
    else:
        weights_tuple_ = COMP_WEIGHTS
    cell_array_[row_][col_]['weight'] += weights_tuple_[0]
    for s_ in range(1, 5):
        # Направления -> right, left, down, up
        if col_ + s_ in range(FIELD_COLS):
            cell_array_[row_][col_ + s_]['weight'] += weights_tuple_[s_]
        if col_ - s_ in range(FIELD_COLS):
            cell_array_[row_][col_ - s_]['weight'] += weights_tuple_[s_]
        if row_ + s_ in range(FIELD_ROWS):
            cell_array_[row_ + s_][col_]['weight'] += weights_tuple_[s_]
        if row_ - s_ in range(FIELD_ROWS):
            cell_array_[row_ - s_][col_]['weight'] += weights_tuple_[s_]
        # Направления -> down-right, down-left, up-right, up-left
        if (row_ + s_ in range(FIELD_ROWS)) and (col_ + s_ in range(FIELD_COLS)):
            cell_array_[row_ + s_][col_ + s_]['weight'] += weights_tuple_[s_]
        if (row_ + s_ in range(FIELD_ROWS)) and (col_ - s_ in range(FIELD_COLS)):
            cell_array_[row_ + s_][col_ - s_]['weight'] += weights_tuple_[s_]
        if (row_ - s_ in range(FIELD_ROWS)) and (col_ + s_ in range(FIELD_COLS)):
            cell_array_[row_ - s_][col_ + s_]['weight'] += weights_tuple_[s_]
        if (row_ - s_ in range(FIELD_ROWS)) and (col_ - s_ in range(FIELD_COLS)):
            cell_array_[row_ - s_][col_ - s_]['weight'] += weights_tuple_[s_]

def check_line(array_, row_, col_, xo_):
    ''' Проверяет наличие пяти X или O в линию и прекращает игру, если есть.
    '''
    horiz_line_ = ''
    verti_line_ = ''
    risin_line_ = ''
    falln_line_ = ''
    looser_line_ = xo_ * 5
    for s_ in range(-4, 5):
        if col_ + s_ in range(FIELD_COLS):
            horiz_line_ += array_[row_][col_ + s_]['xo']
        if row_ + s_ in range(FIELD_ROWS):
            verti_line_ += array_[row_ + s_][col_]['xo']
        if (row_ - s_ in range(FIELD_ROWS)) and (col_ + s_ in range(FIELD_COLS)):
            risin_line_ += array_[row_ - s_][col_ + s_]['xo']
        if (row_ + s_ in range(FIELD_ROWS)) and (col_ + s_ in range(FIELD_COLS)):
            falln_line_ += array_[row_ + s_][col_ + s_]['xo']
    if (horiz_line_.find(looser_line_) > -1) or \
       (verti_line_.find(looser_line_) > -1) or \
       (risin_line_.find(looser_line_) > -1) or \
       (falln_line_.find(looser_line_) > -1):
        if xo_ == 'X':
            print_field(array_)
            print(u'Вы проиграли!')
        if xo_ == 'O':
            print_field(array_)
            print(u'Вы победили!')
        exit()

def check_end(array_):
    ''' Заканчивает игру, когда не осталось свободных клеток.
    '''
    empty_cells_ = 0
    for row_ in array_:
        for cell_ in row_:
            if cell_['xo'] == '.':
                empty_cells_ += 1
    if empty_cells_ == 0:
        print(u'Нет свободных клеток. Ничья!')
        exit()

def dude_answer(array_, row_, col_):
    ''' Заносит данные хода игрока в матрицу и проверяет "пять X в линию"
    '''
    array_[row_][col_]['xo'] = 'X'
    write_weights(array_, row_, col_, 'X')
    check_line(array_, row_, col_, 'X')

def comp_answer(array_):
    ''' Ход компьютера. Отбирает свободные клетки с минимальным весом и уже
        из них выбирает одну для хода. Заносит данные в матрицу и проверяет
        "пять O в линию".
    '''
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
    check_line(array_, r_, c_, 'O')

def put_signs(array_, str_):
    ''' Принимает строку выбора игрока и делает ход компьютера
    '''
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

def game_cycle(cell_array_, who_first_):
    ''' Основной игровой цикл хода игрока и ответа компьютера
    '''
    coords = ''
    if who_first_ == '2':
        comp_answer(cell_array_)
    while True:
        print_field(cell_array_)
        str1_ = u'Введите [Q|q] для выхода из программы, или\n'
        str2_ = u'Координаты крестика числами в формате "номер_строки/номер_столбца": '
        coords = input(str1_ + str2_)
        if coords in ('Q', 'q'):
            break
        put_signs(cell_array_, coords)


''' =====----- MAIN -----===== '''

if __name__ == '__main__':
    cell_obj = GameCell()
    cell_array = [[cell_obj.cell_dict.copy() for col in range(FIELD_COLS)] \
                                             for row in range(FIELD_ROWS)]
    for pos_ in POS_LIST:
        cell_array[pos_[0]][pos_[1]]['pos'] = pos_
    who_first = input(u'Вы играете крестиками. Компьютер - ноликами.\n' + \
                      u'Кто делает первый ход? 1 - игрок, 2 - компьютер: ')
    game_cycle(cell_array, who_first)

#####=====----- THE END -----=====#########################################