#Please enter these choices for client to test the program:
#client_id=123,, choose 2 or 4 the book id to test borrow option then the same id is used for return
#librarian_id=236
import users
from Lists.constants import Check_empty, Check_number
from Lists import Lists
from constants import Constants

from control import search
from control.search import Search_controller, Return_book

print("Hello user, Welcome to our Library")
id=input("enter your library id\n")

if Check_empty.check_value_is_empty(id)== True or Check_number.check_value_is_number(id)== False :
    print("enter a valid id")
else:
     if Search_controller.check_if_client_exsist(id)==True:
        print("what is your request:\n 1. See available books \n 2. Borrow book \n 3. Return book")
        request=input("enter the number of option you want\n")

        if request=="1":
           available_books=Lists.Lists.display_available_books()

        elif request=="2":
             available_books = Lists.Lists.display_available_books()

             book_id=input("\n **enter the id of the book you want to borrow from the above available list**\n")
             if Check_empty.check_value_is_empty(book_id) == True or Check_number.check_value_is_number(book_id) == False:
                print("not valid book id")
             else:
                  date = input("please enter the date of borrowing\n")
                  Search_controller.create_new_borrow_order(client_id=id,date=date,book_id=book_id,order_id = "2",
                                                   order_status = 5)
                  print("your order is created")
                  Lists.Lists.display_available_borrow_order()# this for clarifying the change in borrow order
        elif request=="3":
             book_id=input("enter the id of book you want to return\n")
             Return_book.return_book(book_id)
             Lists.Lists.display_available_borrow_order() # this for clarifying that the book has been returned and show the list of order after this change
             print("your book has been returned")

        else:
             print("enter valid number for your option")

     elif Search_controller.check_if_Librarian_exsist(id)==True:
          choice=input("what is your request:\n 1.Show book list \n 2. available books \n 3. add new book to list \n"
                       " 4. see borrow order list \n 5. add new client\n enter the number of your choice\n")
          if Check_empty.check_value_is_empty(choice) == True or Check_number.check_value_is_number(choice) == False:
             print("not valid number")
          else:
              if choice=="1":
                 print("The book list are:",Lists.Lists.get_Book_list())

              elif choice=="2":
                 print("available books are:\n",Lists.Lists.display_available_books())

              elif choice=="3":
                   print("So you want to add new book to list!")
                   book_id=input("enter book id")
                   title=input("enter title")
                   description=input("enter description")
                   author=input("enter author name")
                   book=users.book.Book(book_id,title,description,author,book_status=3)
                   search.Register.register_new_book(book)
                   print(Lists.Lists.get_Book_list()) # this for clarifying after adding


              elif choice=="4":
                   print("this is the borrow order list",Lists.Lists.display_available_borrow_order())

              elif choice=="5":
                   print("the list of client is", Lists.Lists.get_Client_list())

                   identity=input("enter the new client identity")
                   name=input("client name")
                   age=input("client age")
                   id=input("client id")
                   phone=input("phone")
                   client=users.Client.Client(identity,name,age,id,phone)
                   search.Register.register_new_client(client)
                   print("New client list",Lists.Lists.get_Client_list()) # this for clarifying after adding
              else:
                  print("enter valid option")





