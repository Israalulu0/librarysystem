from users.Person import Person

class Client(Person):

    def __init__(self, identity, name, age, id, phone):

        super(Client, self).__init__(identity=identity,name=name, age=age,id=id, phone=phone)

    def get_id(self):
        return self.__id


