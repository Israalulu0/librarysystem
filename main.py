
from constants import Constants


from control.search import check_if_Librarian_exsist, check_if_client_exsist

print("Hello user, Welcome to our Library")
id1=input("enter your library id\n")

if check_if_Librarian_exsist(id1) is True:
    type=Constants.Librarian
    print("what is your request:\n 1. ")
elif check_if_client_exsist(id1) is True:
    type=Constants.Client
else:
    print("enter a valid ID")








