from model.person import person


class client(person):

    def __init__(self, id, full_name, age, id_no, phone_number):
        self.phone_number = phone_number
        super(client, self).__init__(id=id,full_name=full_name,age=age,id_no=id_no)



    def get_phone_number(self):
        return self.phone_number
