from users.Person import Person


class Librarian(Person):

    def __init__(self, identity, name, age, id,employment_type):

        self.__employment_type = employment_type
        super(Librarian, self).__init__(identity=identity, name=name,age=age,id=id)



