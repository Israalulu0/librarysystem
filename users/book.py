class Book:
    def __init__(self,book_id,title,description,author,book_status=3):
        self.__book_id=book_id
        self.__title=title
        self.__description=description
        self.__author=author
        self.__book_status=book_status
    def get_book_id(self):
        return self.__book_id
    def get_book_title(self):
        return self.__title
    def get_book_description(self):
        return self.__description
    def get_book_author(self):
        return self.__author
    def get_book_status(self):
        return self.__book_status
    def set_book_status(book_id):
         Book.book_status=3