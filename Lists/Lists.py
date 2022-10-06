import constants
from constants import Constants
from users.Client import Client
from users.Librarian import Librarian
from users.book import Book
from users.Order import Order

class Lists:
    Client_list: list[Client] = [
        Client("123", "Ahmed", 35, "123","059949"),
        Client("456", "Omar", 16,"456","059969"),
        Client("789", "Israa", 31,"789","0597")]

    Librarian_list: list[Librarian]= [
        Librarian("236","Mohammed",40,"987",1),
        Librarian("782", "Adam", 29,"256", 2),
        Librarian("463", "Josif", 42,"111", 1)]

    Book_list: list[Book] = [
        Book("1", "The origin of creation","This book give all earth discoveres","Razi",3),
        Book("2", "Physics","This book give information about Einstein theories","Sam",4),
        Book("3", "Chemistry", "This book introduces the chemical reactions","James",3),
        Book("4", "Life & Science", "This Book specializes in development","Ibrahim",4)]

    Borrow_Orders_list: list[Order]= [
        Order("1","456","20/01/2022","1",5),
        Order("2", "456", "5/01/2022", "3", 5),


    ]

    def get_Client_list():
        return Lists.Client_list
    def get_Librarian_list(self):
        return self.Librarian_list
    def get_Book_list():
        return Lists.Book_list
    def get_Borrow_Orders_list(self):
        return self.Borrow_Orders_list


    def display_available_books():
        for item in Lists.Book_list:
            if item.get_book_status()==4:
               print("book id is:",item.get_book_id(),"\nbook title is:",item.get_book_title(),"\n description is:",item.get_book_description(),"\n book author:",item.get_book_author())

    def display_available_borrow_order():
        for item in Lists.Borrow_Orders_list:
               print("borrowing order list are: order id",item.get_order_id(),"\n client id:",
                     item.get_client_id(),"\n date:",item.get_date(),"\n book id:",item.get_book_id(),"\n order status:", item.get_order_status())





