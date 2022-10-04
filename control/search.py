from constants import Constants

from users.Client import Client
from users.Librarian import Librarian
from users.book import Book


def register_new_client(self, client: Client):
    if not self.check_if_user_exsist(Client.get_id(client)):
        self.Client_list.append(Client)
    else:
        print("User already exist!")

def register_new_book(self, book: Book):
    if not self.check_if_user_exsist(Book.get_book_id(book)):
        self.Book_list.append(Book)
    else:
        print("Book already exist!")

def check_if_client_exsist(self, id: str):
        for item in self.Client_list:
            if item.get_id() == id:
                return True
        return False


def check_if_book_available(self, name: str):
    for item in self.Book_list:
        if item.get_book_status() == Constants.Active_Book:
            return True
    return False

class Search_controller:
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


