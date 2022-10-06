from Lists.constants import Check_empty, Check_number
from Lists import Lists
from constants import Constants
from control.search import Search_controller

print("Hello user, Welcome to our Library")
id=input("enter your library id\n")

if Check_empty.check_value_is_empty(id)== True or Check_number.check_value_is_number(id)== False :
    print("enter a valid id")

if Search_controller.check_if_client_exsist(id)==True:
    print("what is your request:\n 1. See available books \n 2. Borrow book \n 3. Return book \n 4. Cancel Order ")
request=input("enter the number of option you want\n")

if request=="1":
    available_books=Lists.Lists.display_available_books()
    print("available books in the library are:")
elif request=="2":
    print("2")
elif request=="3":
    pass
elif request=="4":
    pass
else:
    print("enter valid number for your option")


