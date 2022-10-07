from Utills.utills import constatns
from model.librarian import librarian
from model.client import client


class auth:

    client_list : list[client]=[
        client(1,"sara",18,"123",5996),
        client(2, "omar", 23, "234", 5943),
        client(3, "khaled", 19, "456",5998)
    ]
    librarian_list:list[librarian]=[
        librarian(4,"saja",14,"369",constatns.Full_time),
        librarian(5, "sami", 30, "753", constatns.Part_time),
        librarian(4, "eyad", 40, "159", constatns.Full_time)



    ]

    def login(self,username:str,password:str)->bool:
        for item in self.client_list:
            if username==item.get_user_name()and password==item.get_password():
                return True

        return False

    def login1(self,username:str,password:str)->bool:
        for item in self.librarian_list:
            if username==item.get_user_name()and password==item.get_password():
                return True


        return False

    def new_users(self,user:client):

        if not self.check_if_client_exist(user.get_user_name()):
            self.client_list.append(user)
        else: print("user already used")

    def check_if_client_exist(self,username:str):
        for item in self.client_list:
            if item.get_user_name()== username:
                return True
            return False

    def new_librarian(self,user:librarian):
        if not self.check_if_librarian_exist(user.get_user_name()):
            self.librarian_list.append(user)
        else: print("user already used")

    def check_if_librarian_exist(self, username: str):
        for item in self.librarian_list:
            if item.get_user_name() == username:
                return True
            return False
