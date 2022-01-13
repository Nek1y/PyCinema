from app import HALL_REPO, MOVIE_REPO, SESSION_REPO


def use_case_index_movie():
    movie_names = []
    movies = MOVIE_REPO.movie_list()
    for m in movies:
        movie_names.append(m.Name)
    return movie_names


def use_case_index_hall():
    hall_names = []
    halls = HALL_REPO.hall_list()
    for h in halls:
        hall_names.append(h.Name)

    return hall_names


def use_case_add_hall(name, row, column):
    HALL_REPO.hall_add(name, row, column)


def use_case_del_hall(hall):
    HALL_REPO.hall_del(hall)


def use_case_hall_session_list(hall_name):
    dict_list = []
    session_list = SESSION_REPO.hall_get_session_list(hall_name)
    for s in session_list:
        dict_list.append(s.__dict__)
    return dict_list


def use_case_add_movie(name):
    MOVIE_REPO.movie_add(name)


def use_case_del_movie(name):
    MOVIE_REPO.movie_del(name)


def use_case_movie_session_list(movie_name):
    dict_list = []
    session_list = SESSION_REPO.movie_get_session_list(movie_name)
    for s in session_list:
        dict_list.append(s.__dict__)
    return dict_list


def use_case_get_session(id):
    return SESSION_REPO.get_session(id)


def use_case_update_session(id, row, column):
    data = SESSION_REPO.get_session(id)
    data[row][column] = 1
    SESSION_REPO.update_session(id, data)


def use_case_gen_session():
    movie_list = MOVIE_REPO.movie_list()
    hall_list = HALL_REPO.hall_list()
    
    for h in hall_list:
        for m in movie_list:
            hall_name = h.Name
            movie_name = m.Name
            time = "12:00"
            data = [0] * h.Row
            for i in range(h.Row):
                data[i] = [0] * h.Column
            SESSION_REPO.add_session(hall_name, movie_name, time, data)
