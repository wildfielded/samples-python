#!/usr/bin/python3

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

#####=====----- THE END -----=====#########################################