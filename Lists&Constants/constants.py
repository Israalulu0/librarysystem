class Constants:
    FULL_TIME = 1
    PART_TIME = 2
    Active_Book=1
    Inactive_Book=2
    Active_order=1
    Expired_order=2
    Cancelled_order=3

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