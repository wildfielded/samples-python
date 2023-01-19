#!/usr/bin/python3

from random import choice
from sys import exit


''' =====----- Variables -----===== '''

FIELD_ROWS = 10
FIELD_COLS = 10
POS_LIST = [(row, col) for row in range(FIELD_ROWS)
                       for col in range(FIELD_COLS)]
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

def draw_field(cell_array_):
    ''' Called in game_cycle() and check_line().
    Forms the current multi-line state of the game field fot output
    to the console.
    -----
    Используется в game_cycle() и check_line().
    Формирует многострочник текущего состояния игрового поля для вывода
    на консоль.
    Arguments:
        cell_array_ [list] -- Двумерный массив (список списков) объектов
            клетки игрового поля
    Returns:
        output_str_ [str] -- Игровое поле в текстовом виде
    '''
    output_str_ = '   '
    for col_ in range(FIELD_COLS):
        output_str_ += (str(col_) + ' ')
    output_str_ += ('\n' + '   | | | | | | | | | |' + '\n')
    row_num_ = 0
    for row_ in cell_array_:
        tmp_str_ = str(row_num_) + '--'
        for cell_ in row_:
            tmp_str_ += (cell_['xo'] + ' ')
        tmp_str_ += '\n'
        output_str_ += tmp_str_
        row_num_ += 1
    return output_str_

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

def check_line(cell_array_, row_, col_, xo_):
    ''' Called in dude_answer() and comp_answer().
    Checks the existence of five X or O in a line and stops the game
    if there are.
    -----
    Используется в dude_answer() и comp_answer().
    Проверяет наличие пяти X или O в линию и прекращает игру, если есть.
    Arguments:
        cell_array_ [list] -- Двумерный массив (список списков) объектов
        row_, col_ [int] -- Номера строки и колонки клетки, в которой
            сделан ход
        xo_ [str] -- 'X' или 'O', в зависимости от того, чей был ход
    '''
    horiz_line_ = ''
    verti_line_ = ''
    risin_line_ = ''
    falln_line_ = ''
    looser_line_ = xo_ * 5
    for s_ in range(-4, 5):
        # Check in horisontal line
        if col_ + s_ in range(FIELD_COLS):
                horiz_line_ += cell_array_[row_][col_ + s_]['xo']
        # Check in vertical line
        if row_ + s_ in range(FIELD_ROWS):
                verti_line_ += cell_array_[row_ + s_][col_]['xo']
        # Check in rising (down-left to up-right) diagonal
        if (row_ - s_ in range(FIELD_ROWS)) and \
           (col_ + s_ in range(FIELD_COLS)):
                risin_line_ += cell_array_[row_ - s_][col_ + s_]['xo']
        # Check in falling (up-left to down-right) diagonal
        if (row_ + s_ in range(FIELD_ROWS)) and \
           (col_ + s_ in range(FIELD_COLS)):
                falln_line_ += cell_array_[row_ + s_][col_ + s_]['xo']
    if (horiz_line_.find(looser_line_) > -1) or \
       (verti_line_.find(looser_line_) > -1) or \
       (risin_line_.find(looser_line_) > -1) or \
       (falln_line_.find(looser_line_) > -1):
        if xo_ == 'X':
            print(draw_field(cell_array_))
            print(u'Вы проиграли!')
        if xo_ == 'O':
            print(draw_field(cell_array_))
            print(u'Вы победили!')
        exit()

def check_end(cell_array_):
    ''' Called in put_signs().
    Ends the game if there are no free cells left.
    -----
    Используется в put_signs().
    Заканчивает игру, когда не осталось свободных клеток.
    Arguments:
        cell_array_ [list] -- Двумерный массив (список списков) объектов
    '''
    empty_cells_ = 0
    for row_ in cell_array_:
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

def put_signs(cell_array_, str_):
    ''' Called in game_cycle().
    Accepts the player's choice string and makes the computer's move
    -----
    Используется в game_cycle().
    Принимает строку выбора игрока и делает ход компьютера.
    Arguments:
        cell_array_ [list] -- Двумерный массив (список списков) объектов
        str_ [str] -- Координаты хода игрока в формате
            row_number/column_number (именно через "/", можно с
            пробелами в люьом месте, которые устаняются)
    '''
    list_ = str_.split('/')
    if len(list_) == 2 and list_[0].strip().isdigit() and \
                           list_[1].strip().isdigit():
        row_ = int(list_[0])
        col_ = int(list_[1])
        if row_ < FIELD_ROWS and col_ < FIELD_COLS:
            if cell_array_[row_][col_]['xo'] == '.':
                dude_answer(cell_array_, row_, col_)
                check_end(cell_array_)
                comp_answer(cell_array_)
                check_end(cell_array_)
            else:
                print('\n\n\n\n\n\n\n\n\n\n')
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                print(u'ОШИБКА!!! Клетка занята. Поробуйте другую.')
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
        else:
            m_ = input(u'Превышен диапазон. Нажмите любую клавишу и пробуйте ещё раз: [Enter]')
    else:
        m_ = input(u'Ошибка ввода. Нажмите любую клавишу и пробуйте ещё раз: [Enter]')

def game_cycle(cell_array_, who_first_):
    ''' Основной игровой цикл хода игрока и ответа компьютера
    '''
    coords = ''
    if who_first_ == '2':
        comp_answer(cell_array_)
    while True:
        print(draw_field(cell_array_))
        str1_ = u'Введите [Q|q] для выхода из программы, или\n'
        str2_ = u'Координаты крестика числами в формате "номер_строки/номер_столбца": '
        coords = input(str1_ + str2_)
        if coords in ('Q', 'q'):
            break
        put_signs(cell_array_, coords)


''' =====----- MAIN -----===== '''

if __name__ == '__main__':
    # cell_obj = GameCell()
    # cell_array = [[cell_obj.cell_dict.copy() for col in range(FIELD_COLS)]
                                             # for row in range(FIELD_ROWS)]
    cell_array = [[GameCell().cell_dict.copy() for col in range(FIELD_COLS)]
                                               for row in range(FIELD_ROWS)]
    for pos_ in POS_LIST:
        cell_array[pos_[0]][pos_[1]]['pos'] = pos_
    who_first = input(u'Вы играете крестиками. Компьютер - ноликами.\n' + \
                      u'Кто делает первый ход? 1 - игрок, 2 - компьютер: ')
    game_cycle(cell_array, who_first)

#####=====----- THE END -----=====#########################################