class Contact:
    def __init__(self, fullname, phonenumber):
        if fullname == "":
            raise Exception("Enter the name")
        self.full_name = fullname
        self.phone_number = phonenumber
