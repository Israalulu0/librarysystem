class Constants:
    FULL_TIME = 1
    PART_TIME = 2
    Active_Book=3
    Inactive_Book=4
    Active_order=5
    Expired_order=6
    Cancelled_order=7
    Librarian=8
    Client=9



class Check_empty:

    def check_value_is_empty(*value: str):
        for item in value:
            if item.isspace() or item == "":
                return True
            else:
                return False

class Check_number:
    def check_value_is_number(value):
        if value.isdigit():
            return True
        else:
            return False