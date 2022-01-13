from app.database import Database


class Hall_repo():
    DB:Database = None

    def __init__(self, database):
        self.DB = database


    def hall_add(self, name:str, row:int, column:int):
        new_hall = Hall(name, row, column)
        self.DB.hall_add(new_hall)


    def hall_del(self, name:str):
        self.DB.hall_del(name)


    def hall_list(self):
        return self.DB.hall_list()
        

class Movie_repo():
    DB:Database = None

    def __init__(self, database):
        self.DB = database


    def movie_add(self, name:str):
        new_hall = Movie(name)
        self.DB.movie_add(new_hall)


    def movie_del(self, name:str):
        self.DB.movie_del(name)


    def movie_list(self):
        return self.DB.movie_list()


class Session_repo():
    DB:Database = None

    def __init__(self, database):
        self.DB = database

    
    def add_session(self, hall, movie, time, data):
        id = self.DB.get_id() + 1
        self.DB.set_id(id)
        new_session = Session(hall, movie, time, id, data)
        self.DB.add_session(new_session)


    def del_session(self, session_num):
        self.DB.del_session(session_num)


    def session_list(self):
        return self.DB.session_list()


    def get_session(self, session_num):
        return self.DB.get_session(session_num)


    def hall_get_session_list(self, hall_name):
        return self.DB.hall_get_session_list(hall_name)

    
    def movie_get_session_list(self, movie_name):
        return self.DB.movie_get_session_list(movie_name)


    def update_session(self, session_num, data):
        self.DB.update_session(session_num, data)


class Hall():
    Row = 0
    Column = 0
    Name = ''

    def __init__(self, name, row, column):
        self.Name = name
        self.Row = row
        self.Column = column


class Movie():
    Name = ''

    def __init__(self, name):
        self.Name = name


class Session():
    Hall_name = ''
    Movie_name = ''
    Time = ''
    ID = 0
    Data = []

    def __init__(self, hall, movie, time, id, data):
        self.Hall_name = hall
        self.Movie_name = movie
        self.Time = time
        self.ID = id
        self.Data = data
