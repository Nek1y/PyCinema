from abc import ABC, abstractmethod


class Database(ABC):

    @abstractmethod
    def get_id(self):
        pass

    @abstractmethod
    def set_id(self, id):
        pass

    @abstractmethod
    def hall_add(self, new_hall):
        pass

    @abstractmethod
    def hall_del(self, name):
        pass

    @abstractmethod
    def hall_list(self):
        pass

    @abstractmethod
    def movie_add(self, name):
        pass

    @abstractmethod
    def movie_del(self, name):
        pass

    @abstractmethod
    def movie_list(self, name):
        pass

    @abstractmethod
    def add_session(self, session):
        pass

    @abstractmethod
    def del_session(self, session_num):
        pass

    @abstractmethod
    def get_session(self, session_num):
        pass

    @abstractmethod
    def session_list(self):
        pass

    @abstractmethod
    def hall_get_session_list(self, hall_name):
        pass

    @abstractmethod
    def movie_get_session_list(self, movie_name):
        pass

    @abstractmethod
    def update_session(self, session_num, data):
        pass
