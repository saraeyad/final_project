from model.person import person


class librarian(person):

    def __init__(self, id, full_name, age, id_no, emplyment_type):
        self.emplyment_type = emplyment_type
        super(librarian, self).__init__(id=id,full_name=full_name,age=age,id_no=id_no)

    def get_emplyment_type(self):
        return self.emplyment_type