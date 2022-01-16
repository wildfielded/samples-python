post = {'id': 0, 'coords': (0, 2), 'descr': 'Почтовое отделение'}
point1 = {'id': 1, 'coords': (2, 5), 'descr': 'Ул. Грибоедова, 104/25'}
point2 = {'id': 2, 'coords': (5, 2), 'descr': 'Ул. Бейкер стрит, 221б'}
point3 = {'id': 3, 'coords': (6, 6), 'descr': 'Ул. Большая Садовая, 302-бис'}
point4 = {'id': 4, 'coords': (8, 3), 'descr': 'Вечнозелёная Аллея, 742'}

point_list = [post, point1, point2, point3, point4]
point_set = set([point_['id'] for point_ in point_list[1:]])

draft_routes = [
    [1,2,3,4],
    [1,2,4,3],
    [1,3,2,4],
    [1,3,4,2],
    [1,4,2,3],
    [1,4,3,2],
    [2,1,3,4],
    [2,1,4,3],
    [2,3,1,4],
    [2,3,4,1],
    [2,4,1,3],
    [2,4,3,1],
    [3,1,2,4],
    [3,1,4,2],
    [3,2,1,4],
    [3,2,4,1],
    [3,4,1,2],
    [3,4,2,1],
    [4,1,2,3],
    [4,1,3,2],
    [4,2,1,3],
    [4,2,3,1],
    [4,3,1,2],
    [4,3,2,1]
]

def create_distance_array(point_list_):
    calc_distance = lambda a, b : ((a['coords'][0] - b['coords'][0]) ** 2 + (a['coords'][1] - b['coords'][1]) ** 2) ** 0.5
    len_ = len(point_list_)
    distance_array = [[0 for col_ in range(len_)] for raw_ in range(len_)]
    for start_point in point_list_:
        i_ = start_point['id']
        for finish_point in point_list_[i_+1:]:
            j_ = finish_point['id']
            distance_array[i_][j_] = distance_array[j_][i_] = calc_distance(point_list_[i_], point_list_[j_])
    return distance_array

distances = create_distance_array(point_list)
for k_ in distances:
    print(k_)
