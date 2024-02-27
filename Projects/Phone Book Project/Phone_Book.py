import Contact


class PhoneBook:
    def __init__(self):
        self.contact_list = []
        self.show_contact_list = []

    def add_contact(self, name, phone):
        contact = Contact.Contact(name, phone)
        self.contact_list.append(contact)
        self.show_contact_list.append(contact)

    def search_contact(self, name):
        self.show_contact_list.clear()

        for i in self.contact_list:
            if name.upper() in i.full_name.upper():
                self.show_contact_list.append(i)

    def delete_contact(self, name, phone):
        for i in self.contact_list:
            if i.full_name == name and i.phone_number == phone:
                self.contact_list.remove(i)

        self.show_contact_list = self.contact_list.copy()
