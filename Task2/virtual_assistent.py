from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        self.name = name

class Phone(Field):
    def __init__(self, number):
        if self.validate_number(number):
            self.number = number
        else:
            raise ValueError("Invalid phone number format")
    def validate_number(self, number):
        if len(number) == 10 and number.isdigit():
            return True
        else:
            return False

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        return "Phone added"
    def remove_phone(self, phone_remove):
        for phone in self.phones:
            if phone.value == phone_remove:
                self.phones.remove(phone)
                return "Phone deleted"
        return "Phone not found"
    def edit_phone(self, new_phone):
        self.phones = [Phone(new_phone)]
        return "Phone edited"
    def find_phone(self):
        if self.phones:
            return "; ".join(str(phone) for phone in self.phones)
        else:
            return "Phone not found"
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {self.find_phone()}"

class AddressBook(UserDict):
    def add_record(self, name, record):
        self.data[name] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return "Record not found"

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return "Record deleted"
        else:
            return "Record not found"