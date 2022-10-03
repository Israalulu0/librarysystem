
class Order:
    def __init__(self,order_id,client_id,date,book_id,order_status):
        self.__order_id=order_id
        self.__client_id=client_id
        self.__date=date
        self.__book_id=book_id
        self.__order_status=order_status

    def get_order_status(self):
        return self.__order_status

    def get_order_id(self):
        return self.__order_id


