from .database import Database


class Ramdb(Database):
    Hall_list = []
    Movie_list = []
    Session_list = []
    Session_id = 0


    def get_id(self):
        return self.Session_id


    def set_id(self, new_id):
        self.Session_id = new_id


    def hall_add(self, new_hall):
        self.Hall_list.append(new_hall)


    def hall_del(self, name):
        for h in self.Hall_list:
            if(h.Name == name):
                self.Hall_list.remove(h)


    def hall_list(self):
        return self.Hall_list


    def movie_add(self, name):
        self.Movie_list.append(name)


    def movie_del(self, name):
        for m in self.Movie_list:
            if(m.Name == name):
                self.Movie_list.remove(m)


    def movie_list(self):
        return self.Movie_list


    def add_session(self, session):
        self.Session_list.append(session)        


    def del_session(self, session_num):
        s = self.Session_list.get(session_num)
        if s is not None:
            self.Session_list.pop(s)


    def get_session(self, session_num):
        for s in self.Session_list:
            if(s.ID == session_num):
                return s.Data
        return ['error']


    def hall_get_session_list(self, hall_name):
        data = []
        for s in self.Session_list:
            if(s.Hall_name == hall_name):
                data.append(s)
        return data


    def session_list(self):
        return self.Session_list

    
    def movie_get_session_list(self, movie_name):
        data = []
        for s in self.Session_list:
            if(s.Movie_name == movie_name):
                data.append(s)
        return data
    

    def update_session(self, session_num, data):
        for s in self.Session_list:
            if(s.ID == session_num):
                new_s = s
                new_s.Data = data
                self.Session_list.remove(s)
                self.Session_list.append(new_s)
