#!/usr/bin/python3

#####=====----- Variables -----=====#####

post = {'id': 0, 'coords': (0, 2), 'descr': 'Почтовое отделение'}
point1 = {'id': 1, 'coords': (2, 5), 'descr': 'Ул. Грибоедова, 104/25'}
point2 = {'id': 2, 'coords': (5, 2), 'descr': 'Ул. Бейкер стрит, 221б'}
point3 = {'id': 3, 'coords': (6, 6), 'descr': 'Ул. Большая Садовая, 302-бис'}
point4 = {'id': 4, 'coords': (8, 3), 'descr': 'Вечнозелёная Аллея, 742'}

point_list = [post, point1, point2, point3, point4]
point_set = set([point_['id'] for point_ in point_list[1:]])
all_routes = []
ALLOWED_DELTA = 0.01


#####=====----- Functions -----=====#####

def create_distance_array(point_list_):
    ''' Создаёт диагонально-симметричную матрицу всех расстояний между всеми
        точками. Расстояние от A до B и расстояние от B до A вычисляется один раз.
        То есть, как положено, для 5 точек вычисляется 4+3+2+1=10 расстояний.
    '''
    calc_dist = lambda a, b : ((a['coords'][0] - b['coords'][0]) ** 2 + (a['coords'][1] - b['coords'][1]) ** 2) ** 0.5
    len_ = len(point_list_)
    dist_array_ = [[0 for col_ in range(len_)] for raw_ in range(len_)]
    for start_point_ in point_list_:
        s_ = start_point_['id']
        for finish_point_ in point_list_[s_+1:]:
            f_ = finish_point_['id']
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

def calc_distance(route_list_, distance_array_):
    ''' Для данного маршрутного листа суммирует расстояния из матрицы расстояний,
        добавляя расстояния от почты до первой и последней точки маршрута.
    '''
    distance_ = (distance_array_[0][route_list_[0]] + distance_array_[0][route_list_[-1]])
    for d_ in range(len(route_list_) - 1):
        distance_ += distance_array_[route_list_[d_]][route_list_[d_+1]]
    return distance_

def get_shorty(route_list_, point_list_, distance_array_, allowed_delta_):
    ''' Находит кратчайший маршрут. Дополнительно находит маршруты, близкие к
        к нему по расстоянию (квадрат разницы меньше заданной дельты).
    '''
    min_route_ = []
    min_dist_ = 0.0
    for route_ in route_list_:
        length_ = calc_distance(route_, distance_array_)
        if min_dist_:
            if length_ < min_dist_:
                min_dist_ = length_
                min_route_ = [route_]
        else:
            min_dist_ = length_
    for route_ in route_list_:
        if route_ != min_route_[0]:
            length_ = calc_distance(route_, distance_array_)
            if (length_ - min_dist_) ** 2 < allowed_delta_:
                min_route_.append(route_)
    return min_route_

def write_string(list_, point_list_, distance_array_):
    ''' Из маршрутного листа формирует строку в требуемом формате.
        Если для почтальона надо представлять маршрут в более читабельном виде
        (по адресам) то можно в коде заменить ключ словаря 'coords' на 'descr'.
        Или расширить формат выдачи до любой красоты.
    '''
    dist_sum_ = 0.0
    list_ = [0] + list_ + [0]
    output_str_ = str(point_list_[0]['coords'])
    for r_ in range(len(list_) - 2):
        dist_sum_ += distance_array_[list_[r_]][list_[r_+1]]
        p_ = str(point_list_[list_[r_+1]]['coords'])
        d_ = str(dist_sum_)
        output_str_ += ' -> {}[{}]'.format(p_, d_)
    dist_sum_ += distance_array_[list_[-2]][0]
    p_ = str(point_list_[0]['coords'])
    d_ = str(dist_sum_)
    output_str_ += ' -> {}[{}] = {}'.format(p_, d_, d_)
    return output_str_

def output_result(short_list_, point_list_, distance_array_):
    ''' Вывод результата работы программы с некоторым расширением к заданию.
        А именно: дополнительно выводит альтернативные маршруты (если есть),
        близкие по расстоянию к кратчайшему.
    '''
    output_str_ = u'\nКратчайший маршрут:\n'
    output_str_ += write_string(short_list_[0], point_list_, distance_array_)
    if len(short_list_) > 1:
        output_str_ += u'\n\nАльтернативные кратчайшие маршруты:\n'
        for another_list_ in short_list_[1:]:
            output_str_ += write_string(another_list_, point_list_, distance_array_)
    return output_str_


#####=====----- MAIN -----=====#####

if __name__ == '__main__':
    distance_array = create_distance_array(point_list)
    find_routes(point_set)
    short_list = get_shorty(all_routes, point_list, distance_array, ALLOWED_DELTA)
    print(output_result(short_list, point_list, distance_array))

#####=====----- THE END -----=====########################################