
class Borrowing_Order:
    def __init__(self, id, date, client_id, book_id, status):
        self.id = id
        self.date = date
        self.client_id = client_id
        self.book_id = book_id
        self.status = status

    def get_id(self):
        return self.id