#!/usr/bin/python3

#####=====----- Variables -----=====#####

post = {'id': 0, 'coords': (0.0, 2.0), 'descr': 'Почтовое отделение'}
point1 = {'id': 1, 'coords': (2.0, 5.0), 'descr': 'Ул. Грибоедова, 104/25'}
point2 = {'id': 2, 'coords': (5.0, 2.0), 'descr': 'Ул. Бейкер стрит, 221б'}
point3 = {'id': 3, 'coords': (6.0, 6.0), 'descr': 'Ул. Большая Садовая, 302-бис'}
point4 = {'id': 4, 'coords': (8.0, 3.0), 'descr': 'Вечнозелёная Аллея, 742'}

point_list = [post, point1, point2, point3, point4]
point_set = set([point_['id'] for point_ in point_list[1:]])
all_routes = []


#####=====----- Functions -----=====#####

def create_distance_array(point_list_):
    ''' Создаёт диагонально-симметричную матрицу всех расстояний между всеми
        точками. Расстояние от A до B и расстояние от B до A вычисляется один раз.
        То есть, как положено, для 5 точек вычисляется 4+3+2+1=10 расстояний.
    '''
    calc_dist = lambda a, b : ((a['coords'][0] - b['coords'][0]) ** 2 + (a['coords'][1] - b['coords'][1]) ** 2) ** 0.5
    len_ = len(point_list_)
    dist_array_ = [[0 for col_ in range(len_)] for raw_ in range(len_)]
    for start_point in point_list_:
        s_ = start_point['id']
        for finish_point in point_list_[s_+1:]:
            f_ = finish_point['id']
            dist_array_[s_][f_] = dist_array_[f_][s_] = calc_dist(point_list_[s_], point_list_[f_])
    return dist_array_

def multiply_list(set_: set={}, list_: list=[]):
    ''' Размножает список на элементы, в которых последовательно (с применением
        генератора) к исходному списку добавляется один член из множества.
        Выводит список полученных списков.
    '''
    output_list_ = []
    for item_ in (s_ for s_ in set_):
        output_list_.append(list_ + [item_])
    return output_list_

def find_routes(set_: set={}, list_: list=[]):
    ''' Создаёт список всех возможных последовательностей (маршрутов) посещения
        точек по их номерам (id). Каждый маршрут тоже в виде списка без начальной
        и конечной точки id=0 (почты). Используется рекурсия, результат заносится
        в глобальную переменную all_routes.
    '''
    result_list_ = []
    if len(list_) > 0:
        if len(list_[0]) < len(set_):
            tmp_list_ = []
            for id_list_ in list_:
                tmp_set_ = set_.copy()
                for id_ in id_list_:
                    tmp_set_.remove(id_)
                tmp_list_ += multiply_list(tmp_set_, id_list_)
            result_list_ = tmp_list_
            find_routes(set_, result_list_)
        else:
            global all_routes
            all_routes = list_
    else:
        result_list_ += multiply_list(set_)
        find_routes(set_, result_list_)


#####=====----- MAIN -----=====#####

if __name__ == '__main__':
    distance_array = create_distance_array(point_list)
    for k_ in distance_array:
        print(k_)
    find_routes(point_set)
    print(all_routes)
    #####print(len(all_routes))

#####=====----- THE END -----=====########################################