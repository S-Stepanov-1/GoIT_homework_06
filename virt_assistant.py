from collections import UserDict


class AddressBook(UserDict):
    def add_to_book(self, record):
        self.data[record.name.value] = record

    def change_number(self, name, record):
        self.data[name] = record

    def delete_number(self, name):
        del self.data[name]

    def find_info_by_name(self, name):
        return [record for record in self.data.values() if record.name.value == name]

    def find_info_by_phone(self, phone):
        return [record for record in self.data.values() for p in record.phones if p.value == phone]


class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value=None):
        super().__init__(value)

    def __str__(self):
        return f"Name: {self.value}"


class Phone(Field):
    def __init__(self, value=None):
        super().__init__(value)

    def __str__(self):
        return f"Phone: {self.value}"


class Email(Field):
    def __init__(self, value=None):
        super().__init__(value)

    def __str__(self):
        return f"E-Mail: {self.value}"


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def change_phone(self, index, phone):
        self.phones[index] = Phone(phone)

    def delete_phone(self, index):
        del self.phones[index]

    def __str__(self):
        result = str(self.name)
        for p in self.phones:
            result += f"\n{str(p)}"
        return result


if __name__ == '__main__':
    book = AddressBook()

    record = Record("John")
    record.add_phone("112")
    record.add_phone("911")
    record.add_phone("007")

    record.delete_phone(0)
    record.change_phone(1, "001")

    book.add_to_book(record)

    answer = book.find_info_by_name("John")

    for i in answer:
        print(i)
