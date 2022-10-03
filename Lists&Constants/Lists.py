from constants import Constants
from users.Client import Client
from users.Librarian import Librarian
from users.book import Book
from users.Order import Order

class Lists:
    Client_list: list[Client] = [
        Client("123", "Ahmed", 35, 1,"059949"),
        Client("456", "Omar", 16,2,"059969"),
        Client("789", "Israa", 31,3,"0597")]

    Librarian_list: list[Librarian]= [
        Librarian("236","Mohammed",40,1,Constants.FULL_TIME),
        Librarian("782", "Adam", 29,2, Constants.PART_TIME),
        Librarian("463", "Josif", 42,3, Constants.FULL_TIME)]

    Book_list: list[Book] = [
        Book(1, "The origin of creation","This book give all earth discoveres","Razi",Constants.Active_Book),
        Book(2, "Physics","This book give information about Einstein theories","Sam",Constants.Inactive_Book),
        Book(3, "Chemistry", "This book introduces the chemical reactions","James",Constants.Active_Book),
        Book(4, "Life & Science", "This Book specializes in development","Ibrahim",Constants.Inactive_Book)]

    Borrow_Orders_list: list[Order]= [
        Order(1,1,"20/01/2022",1,Constants.Active_order),
        Order(2, 3, "5/01/2022", 2, Constants.Active_order),
        Order(3, 2, "8/01/2022", 4, Constants.Active_order)

    ]

    def get_Client_list(self):
        return self.Client_list
    def get_Librarian_list(self):
        return self.Librarian_list
    def get_Book_list(self):
        return self.Book_list




