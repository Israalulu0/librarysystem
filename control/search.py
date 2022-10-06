import users
from Lists.constants import Constants
from users.Client import Client
from users.Librarian import Librarian
from users.Order import Order
from users.book import Book
from Lists.Lists import Lists

class Search_controller:
    def check_if_client_exsist(id:str):
        for item in Lists.Client_list:
            if item.get_id()== id:
                return True
        return False
    def check_if_Librarian_exsist(id:str):
       for item in Lists.Librarian_list:
          if item.get_id()==id:
            return True
       return False


    def check_if_book_available(id: str):
        for item in Lists.Book_list:
          if item.get_book_id()==id:
             if item.get_book_status() ==4:
                return True

        return False


    def create_new_borrow_order(client_id: str, book_id: str, date = "20/1/2023", order_status = 5, order_id = "2"):
        counter = 2
        if Search_controller.check_if_book_available(book_id)==True:
            order_id = str(counter + 1)
            new_order=users.Order.Order(order_id,client_id,date,book_id,order_status)
            Lists.Borrow_Orders_list.append(new_order)
        else:
            print("enter valid book id")

    def search_for_client_by_id(self, id: int, Client_list: list[Client]):
        if Client_list == None or len(Client_list) == 0:
            return None
        else:
             for item in Client_list:
                 if item.get_id() == id:
                      return item

    def search_for_book_by_id(self, id: int, Book_list: list[Book]):
        if Book_list == None or len(Book_list) == 0:
            return None
        else:
              for item in Book_list:
                 if item.get_book_id() == id:
                      return item

    def search_for_librarian_by_id(self, id: int, Librarian_list: list[Librarian]):
        if Librarian_list == None or len(Librarian_list) == 0:
            return None
        else:
              for item in Librarian_list:
                 if item.get_id() == id:
                      return item



class Register:
    def register_new_client(client: Client):
        if not Search_controller.check_if_client_exsist(Client.get_id(client)):
            Lists.Client_list.append(client)
        else:
            print("User already exist!")

    def register_new_book(book: Book):
        if not Search_controller.check_if_book_available(Book.get_book_id(book)):
              Lists.Book_list.append(book)
        else:
            print("Book already exist!")

class Return_book:
    def return_book(id:str):
        for item in Lists.Book_list:
            if item.get_book_id() == id:
                item.set_book_status()
                for i in Lists.Borrow_Orders_list:
                    if i.get_book_id()==id:
                       Lists.Borrow_Orders_list.remove(i)





