from constants import Constants
from users.Client import Client
from users.Librarian import Librarian
from users.book import Book
from users.Order import Order

class Lists:
    Client_list: list[Client] = [
        Client(1, "Ahmed", 35, "059949"),
        Client(2, "Omar", 16, "059969"),
        Client(3, "Israa", 31, "0597")]

    Librarian_list: list[Librarian]= [
        Librarian(1,"Mohammed",40,Constants.FULL_TIME),
        Librarian(2, "Adam", 29, Constants.PART_TIME),
        Librarian(3, "Josif", 42, Constants.FULL_TIME)]

    Book_list: list[Book] = [
        Book(1, "The origin of creation","This book give all earth discoveres","Razi",Constants.Active_Book),
        Book(2, "Physics","This book give information about Einstein theories","Sam",Constants.Inactive_Book),
        Book(3, "Chemistry", "This book introduces the chemical reactions","James",Constants.Active_Book),
        Book(4, "Life & Science", "This Book specializes in development","Ibrahim",Constants.Inactive_Book)]

    Borrow_Orders_list: list[Order]= [
        Order(1)
    ]

    def get_Client_list(self):
        return self.Client_list
    def get_Librarian_list(self):
        return self.Librarian_list
    def get_Book_list(self):
        return self.Book_list




