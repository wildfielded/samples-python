#!/usr/bin/python3

''' =====----- Global variables -----===== '''
post = {'id': 0, 'coords': (0, 2), 'descr': 'Почтовое отделение'}
point1 = {'id': 1, 'coords': (2, 5), 'descr': 'Ул. Грибоедова, 104/25'}
point2 = {'id': 2, 'coords': (5, 2), 'descr': 'Ул. Бейкер стрит, 221б'}
point3 = {'id': 3, 'coords': (6, 6), 'descr': 'Ул. Большая Садовая, 302-бис'}
point4 = {'id': 4, 'coords': (8, 3), 'descr': 'Вечнозелёная Аллея, 742'}

point_list = [post, point1, point2, point3, point4]
point_set = set([point_['id'] for point_ in point_list[1:]])
ALL_ROUTES = []
ALLOWED_DELTA = 0.01


''' =====----- Functions -----===== '''
def create_distance_array(point_list_: list) -> list:
    ''' Creates a diagonally symmetrical array (matrix) of all distances between
    all points. The distance from A to B and the distance from B to A are
    calculated once. That is, for 5 points 4+3+2+1=10 distances are calculated.

    Создаёт диагонально-симметричную матрицу всех расстояний между всеми
    точками. Расстояние от A до B и расстояние от B до A вычисляется один раз.
    То есть, как положено, для 5 точек вычисляется 4+3+2+1=10 расстояний.
    Arguments:
        point_list_ [list] -- Список словарей с атрибутами точек назначения
    Returns:
        distance_array_ [list] -- Массив (список списков) расстояний между
            точками назначения
    '''
    calc_dist = lambda a, b : (   (a['coords'][0] - b['coords'][0]) ** 2
                                + (a['coords'][1] - b['coords'][1]) ** 2
                              ) ** 0.5
    len_ = len(point_list_)
    distance_array_ = [[0 for col_ in range(len_)] for raw_ in range(len_)]
    for start_point_ in point_list_:
        s_ = start_point_['id']
        for finish_point_ in point_list_[s_+1:]:
            f_ = finish_point_['id']
            distance_array_[s_][f_] \
                = distance_array_[f_][s_] \
                = calc_dist(point_list_[s_], point_list_[f_])
    return distance_array_


def multiply_list(set_: set, list_: list=[]) -> list:
    ''' Called in find_routes().
    Multiplies the list into elements in which one member from the set is added
    sequentially to the initial list (using a generator).

    Используется в find_routes().
    Размножает список на элементы, в которых последовательно (с применением
    генератора) к исходному списку добавляется один член из множества.
    Arguments:
        set_ [set] -- Множество, содержащее идентификаторы (id) точек назначения
        list_ [list] [optional] -- Список списков id точек назначения, созданный
            внутри рекурсии find_routes() (необязательный аргумент)
    Returns:
        output_list_ [list] -- Список полученных списков
    '''
    output_list_ = []
    for item_ in (s_ for s_ in set_):
        output_list_.append(list_ + [item_])
    return output_list_


def find_routes(set_: set, list_: list=[]):
    ''' Recursion is used.
    Changes the global variable ALL_ROUTES, where it writes the created list of
    all possible sequences (routes) of destination points by their numbers (id).
    Each route is also a list without the start and end point (post office with
    id=0).

    Используется рекурсия.
    Изменяет глобальную переменную ALL_ROUTES, в которую заносит созданный
    список всех возможных последовательностей (маршрутов) посещения точек по их
    номерам (id). Каждый маршрут тоже в виде списка без начальной и
    конечной точки с id=0 (почты).
    Arguments:
        set_ [set] -- Множество, содержащее идентификаторы (id) точек назначения
        list_ [list] [optional] -- Список списков id точек назначения
            (необязательный аргумент)
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
            global ALL_ROUTES
            ALL_ROUTES = list_
    else:
        result_list_ += multiply_list(set_)
        find_routes(set_, result_list_)


def calc_distance(route_list_: list, distance_array_: list) -> float:
    ''' Called in get_shorty().
    For the given route sheet,
    Sums distances from the distance array for the given route list. Firstly,
    adding distances from post office to the first waypoint and the last one.

    Испольщуется в get_shorty().
    Для данного маршрутного листа суммирует расстояния из матрицы расстояний,
    добавляя расстояния от почты до первой и последней точки маршрута.
    Arguments:
        route_list_ [list] -- Последовательность id точек назначения
        distance_array_ [list] -- Массив (список списков) расстояний между
            точками назначения
    Returns:
        distance_ [float] -- Итоговая длина маршрута
    '''
    distance_ = (     distance_array_[0][route_list_[0]]
                    + distance_array_[0][route_list_[-1]]
                )
    for d_ in range(len(route_list_) - 1):
        distance_ += distance_array_[route_list_[d_]][route_list_[d_+1]]
    return distance_


def get_shorty(point_list_: list, distance_array_: list) -> list:
    ''' Finds the shortest route from global variable ALL_ROUTES. Additionally,
    it finds routes that are close to the shortest one in distance (the square
    of the difference is less than global variable ALLOWED_DELTA).

    Из всех маршрутов в ALL_ROUTES находит кратчайший маршрут. Дополнительно
    находит маршруты, близкие к нему по расстоянию (квадрат разницы меньше
    ALLOWED_DELTA).
    Arguments:
        point_list_ [list] -- Список словарей с атрибутами точек назначения
        distance_array_ [list] -- Массив (список списков) расстояний между
            точками назначения
    Returns:
        min_route_ [list] -- Список списков с последовательностями id точек
            назначения (без начальной и конечной точек - почты) первого
            кратчайшего пути и близких к нему по сумме расстояний.
    '''
    min_route_ = []
    min_dist_ = 0.0
    for route_ in ALL_ROUTES:
        length_ = calc_distance(route_, distance_array_)
        if min_dist_:
            if length_ < min_dist_:
                min_dist_ = length_
                min_route_ = [route_]
        else:
            min_dist_ = length_
    for route_ in ALL_ROUTES:
        if route_ != min_route_[0]:
            length_ = calc_distance(route_, distance_array_)
            if (length_ - min_dist_) ** 2 < ALLOWED_DELTA:
                min_route_.append(route_)
    return min_route_


def write_string(list_: list, point_list_: list, distance_array_:list) -> str:
    ''' Called in output_result().
    Forms a string in the required format from the route list. If the postman
    needs to present the route in a more readable form (by addresses), then one
    can replace the 'coords' dictionary key with 'descr' key in the code, or
    paint the output to any beauty format.

    Используется в output_result().
    Из маршрутного листа формирует строку в требуемом формате. Если для
    почтальона надо представлять маршрут в более читабельном виде (по адресам),
    то можно в коде заменить ключ словаря 'coords' на 'descr', или расширить
    формат выдачи до любой красоты.
    Arguments:
        list_ [list] -- Список с последовательностями id точек назначения из
            списка списков, полученного в get_shorty()
        point_list_ [list] -- Список словарей с атрибутами точек назначения
        distance_array_ [list] -- Массив (список списков) расстояний между
            точками назначения
    Returns:
        output_str_ [str] -- Маршрутная строка в требуемом формате
    '''
    dist_sum_ = 0.0
    list_ = [0] + list_ + [0]
    output_str_ = str(point_list_[0]['coords'])
    for r_ in range(len(list_) - 2):
        dist_sum_ += distance_array_[list_[r_]][list_[r_+1]]
        p_ = str(point_list_[list_[r_+1]]['coords'])
        d_ = str(dist_sum_)
        output_str_ += f' -> {p_}[{d_}]'
    dist_sum_ += distance_array_[list_[-2]][0]
    p_ = str(point_list_[0]['coords'])
    d_ = str(dist_sum_)
    output_str_ += f' -> {p_}[{d_}] = {d_}'
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


''' =====----- MAIN -----===== '''
if __name__ == '__main__':
    distance_array = create_distance_array(point_list)
    find_routes(point_set)
    short_list = get_shorty(point_list, distance_array)
    print(output_result(short_list, point_list, distance_array))

#####=====----- THE END -----=====#########################################