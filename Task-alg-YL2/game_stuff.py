#!/usr/bin/python3

''' =====----- Variables -----===== '''

FIELD_ROWS = 10
FIELD_COLS = 10


''' =====----- Classes -----===== '''

class GameCell:
    ''' The object is one cell on the playing field with the attributes
    of coordinates (pos), content empty/cross/zero (xo), and weight for
    the next step selection algorithm (weight).
    -----
    Объект одной клетки игрового поля с атрибутами координаты (pos),
    контента пусто/крестик/нолик (xo), весом для алгоритма выбора
    следующего хода (weight).
    '''
    def __init__(self):
        self.cell_obj = {
            'pos': (0, 0),
            'xo': '.',
            'weight': 0
        }

class GameField:
    ''' The array of game field cells. Consists of instances of the
    GameCell class
    -----
    Весь массив клеток игрового поля, состоящий из экземпляров класса GameCell
    '''
    def __init__(self):
        self.cell_arr = [[GameCell().cell_obj.copy()
                          for col in range(FIELD_COLS)]
                          for row in range(FIELD_ROWS)]

#####=====----- THE END -----=====#########################################