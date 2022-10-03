class Person:
    def __init__(self, identity, name, age, id, phone="05997256"):
        self.__identity = identity
        self.__name = name
        self.__age = age
        self.__phone = phone
        self.__id= id


    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
