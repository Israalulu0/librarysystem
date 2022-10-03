class Book:
    def __init__(self,book_id,title,description,author,book_status):
        self.__book_id=book_id
        self.__title=title
        self.__description=description
        self.__author=author
        self.__book_status=book_status


    def get_book_id(self):
        return self.__book_id

    def get_book_status(self):
        return self.__book_status

