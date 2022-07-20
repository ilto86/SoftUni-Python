# data = input()
# phonebook = {}
#
# while len(data) > 1:
#     people_phone_numbers = data.split("-")
#     people_name, phone_number = people_phone_numbers[0], people_phone_numbers[1]
#     if people_name not in phonebook:
#         phonebook[people_name] = phone_number
#
#     phonebook[people_name] = phone_number
#
#     data = input()
#
# n = int(data)
# for i in range(n):
#     name = input()
#     if name not in phonebook:
#         print(f"Contact {name} does not exist.")
#     else:
#         print(f"{name} -> {phonebook.get(name)}")





def phone_book_information(number_of_lines, phone_book):
    for x in range(number_of_lines):
        name = input()
        if name not in phone_book:
            print((f"Contact {name} does not exist."))
        else:
            print(f"{name} -> {phone_book[name]}")
    return True


def phone_book_info():
    phone_book = {}
    condition = False

    while True:
        contact_information = input().split('-')

        if contact_information[0].isdigit():
            condition = phone_book_information(int(contact_information[0]), phone_book)
        else:
            phone_book[contact_information[0]] = contact_information[1]

        if condition:
            break

phone_book_info()