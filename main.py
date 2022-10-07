from model.Book import Book
from model.client import client
from model.librarian import librarian
from model.Borrowing_Order import Borrowing_Order
from Utills.utills import constatns, book_status, order_status
from datetime import date

specialCLient = client(0,"",0,0,0)
List_Client = [
    client(1,"sara",18,123,5996),
    client(2, "omar", 23, 234, 5943),
    client(3, "khaled", 19, 456,5998),
    ]
List_librarian=[
        librarian(1,"saja",14,"369",constatns.Full_time),
        librarian(2, "sami", 30, "753", constatns.Part_time),
        librarian(3, "eyad", 40, "159", constatns.Full_time)
    ]
List_Book = [
    Book(1,"Game Of Thrones","Nine noble families fight ","omar",specialCLient),
    Book(2,"Harry Potter","while an ancient enemy returns after being dormant for millennia.","eric",List_Client[2]),
    Book(3,"Prison Break"," after being dormant for millennia.","israa",List_Client[2]),
    Book(4,"Attak on titan","it's anime for 20 to 30 years old","omar",List_Client[1])
    ]

List_Borrowed_Book = [
    Borrowing_Order(1,date(2022,10,5),1,2,order_status.Active)
    ]

ListOfIdForAvailableBook = []

# def BorrowedBooksNumber():
#     i=0
#     for book in List_Book:
#         if book.status == 4:
#             i=i+1
#     return i
#
# def AvailableBooksNumber():
#     i=0
#     for book in List_Book:
#         if book.status == 3:
#             i=i+1
#     return i
#
# totalOfBorrowedBooks= BorrowedBooksNumber()
# totalAvailableBooks = AvailableBooksNumber()
# totalBorrowedOrders = 2




def login():
    type = int(input("\n***LOGIN***\nif you are Librarian please enter 1\nif you are Client please enter 2\n\nyour choice:  "))
    if type != 1 and type != 2:
        WrongChoice()
        login()
    id = int(input("Enter your Id: "))

    if type == 1:
        i_lib=0
        for item in List_librarian:
            if id == item.id:
                print("you are successfully loged in")
                Librarian_Process(i_lib)
            i_lib=i_lib+1
        print("user not found**********")
        login()
    elif type == 2:
        i_cli = 0
        for item in List_Client:
            if id == item.id:
                print("you are successfully loged in")
                Client_Process(i_cli)
            i_cli= i_cli+1
        print("user not found**********")
        login()




def newClient ():
    print("\n***create new client***")
    id = int(input("Enter the id: "))
    for item in List_Client:
        if id == item.id:
            print("This id is used,Enter again pls")
            newClient()
    name = str(input("Enter name: "))
    age = int(input("Enter your age: "))
    id_Num = input("Enter your identity: ")
    phone = int(input("Enter your number: "))
    print("congratullation new client is created\n")
    List_Client.append(client(id,name,age,id_Num,phone))
    wellcome()

def newBook(idd):
    print("\n***create new book***")
    id = int(input("Enter the id: "))
    for item in List_Book:
        if id == item.id:
            print("This id is used,Enter again pls")
            newBook(id)
    title = str(input("Enter title of the book: "))
    author = str(input("Enter author of the book: "))
    Des = input("Enter description of the book: ")
    print("congratullation new book is created\n")
    List_Book.append(Book(id,title,Des,author,specialCLient))
    # bookInfo()
    # Librarian_Process(id)
    Librarian_Process(idd)


choice=0

def newLibrarian ():
    print("\n***create new librarian***")
    id = int(input("Enter the id: "))
    for item in List_librarian:
        if id == item.id:
            print("This id is used,Enter again pls")
            newLibrarian()
    name = str(input("Enter name: "))
    age = int(input("Enter your age: "))
    id_Num = input("Enter your identity: ")
    print("congratullation new librarian is created\n")
    List_librarian.append(client(id, name, age, id_Num, constatns.Part_time))
    wellcome()

def WrongChoice():
    print("\nWrong Choice!!!!!!\n")
def check_Choice ():
    if choice == 1:
        login()
    elif choice == 2:
        newClient()
    elif choice == 3:
        newLibrarian()
    elif choice == 4:
        exit()
    else:
        WrongChoice()
        wellcome()

def wellcome():
    print("\nWhat do you want to do now ?\n1-login\n2-create new client\n3-create new librarian\n4-Exit")
    global choice
    choice = int(input("your choice: "))
    check_Choice()
def printCliInfo(id):
    print("id: " + str(List_Client[id].id))
    print("name: " + str(List_Client[id].full_name))
    print("age: " + str(List_Client[id].age))
    print("ID number: " + str(List_Client[id].id_no))
    print("phone number: " + str(List_Client[id].phone_number))
def printLibInfo(id):
    print("id: " + str(List_librarian[id].id))
    print("name: " + str(List_librarian[id].full_name))
    print("age: " + str(List_librarian[id].age))
    print("ID number: " + str(List_librarian[id].id_no))
    if List_librarian[id].emplyment_type == 1:
        print("emplyment_type: Full time")
    else:
        print("emplyment_type: Part time")
def bookInfo():
    print("Books")
    for book in List_Book:
        print("ID: "+str(book.id)+"\ttitle: "+book.title+"\tDes: "+book.descrption+"\tauth: "+book.author+"\towner: "+book.owner.full_name)

def Librarian_Process(id):
    print("\n***your profile***\n")
    printLibInfo(id)
    choice = int(input("\n1- Show Books\n2- Create New Book\n3- Exit\nyour Choice: "))
    if choice == 1:
        bookInfo()
    elif choice == 2:
        newBook(id)
    else:
        wellcome()
    Librarian_Process(id)


def Client_Book(id):
    print("\nyour books")
    i=1
    ListOfBook = []
    for book in List_Book:
        if book.owner == List_Client[id]:
            ListOfBook.append(book)
            print(str(i)+ "- " + str(book.title)+ "\tID: "+str(book.id))
            i=i+1
    if i == 1 :
        print("you don't have any book,you should borrow first")
def Client_Borrowing ():
    print("\nList of available book,you can borrow")
    i = 1
    for book in List_Book:
        if book.owner == specialCLient:
            ListOfIdForAvailableBook.append(book.id)
            print(str(i)+ "- title: "+book.title + "\t"+"ID: "+str(book.id))
            i = i + 1
    if i == 1 :
        print("There is no book to borrow, you can visit us later:)")
def CLient_Decision(id):
    print("\nwell, now what do you wanna do?")
    choice = int(input("1- Cancel borrowing any of your book\n2- Borrow new book\n3- Exit\nyour choice: "))
    if choice == 2:
        Client_Borrowing()
        ID = int(input("Enter the ID of the book: "))
        for book in List_Book:
            if book.id == ID:
                book.owner = List_Client[id]
        Client_Book(id)
        Client_Process(id)
    elif choice == 1:
        Client_Book(id)
        ID = int(input("Enter the ID of the book: "))
        for book in List_Book:
            if book.id == ID:
                book.owner = specialCLient
        Client_Book(id)
        Client_Process(id)
    else:
        wellcome()
def Client_Process(id):
    print("\n***your profile***\n")
    printCliInfo(id)
    Client_Book(id)
    Client_Borrowing()
    CLient_Decision(id)



    exit()

print("***WELLCOME***\n")
wellcome()





