from model.client import client

class Book:
    def __init__(self,id,title,descrption,author,owner):
        self.id = id
        self.title = title
        self.descrption = descrption
        self.author = author
        self.owner = owner


    def get_id(self):
        return self.id