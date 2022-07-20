'''
                    Error Handling Exercise
'''#
'''
                    01. Numbers Dictionary
'''

# numbers_dictionary = {}
# line = input('Please enter your string number: ')
#
# while line != "Search":
#     try:
#         number_as_string = line
#         number = int(input('Please enter your int number: '))
#         numbers_dictionary[number_as_string] = number
#     except ValueError:
#         print('The variable number must be an integer')
#     line = input('Please enter your string number: ')
#
#
# line = input('Please enter your Search string number: ')
# while line != "Remove":
#     try:
#         searched = line
#         print(numbers_dictionary[searched])
#     except KeyError:
#         print('Number does not exist in dictionary')
#     line = input('Please enter your Search string number: ')
#
#
# line = input('Please enter your Delete string number: ')
# while line != "End":
#     try:
#         searched = line
#         del numbers_dictionary[searched]
#     except KeyError:
#         print('Number does not exist in dictionary')
#     line = input('Please enter your Delete string number: ')
#
# print(numbers_dictionary)











'''
                    Error Handling Exercise
'''

'''
                    02. Email Validator
'''



# class MustContainAtSymbolError(Exception):
#     pass
#
#
# class NameTooShortError(Exception):
#     pass
#
#
# class InvalidDomainError(Exception):
#     pass
#
#
# valid_domains = {".com", ".bg", ".org", ".net"}
#
# while True:
#     text = input()
#     if text == "End":
#         break
#     email = text
#
#     email_parts = email.split("@")
#
#     if len(email_parts) < 2:
#         raise MustContainAtSymbolError("Email must contain @")
#
#     name, domain_elements = email_parts
#
#     if len(name) < 5:
#         raise NameTooShortError("Name must be more than 4 characters")
#
#     domain_name = f".{domain_elements.split('.')[-1]}"
#
#     if domain_name not in valid_domains:
#         raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
#
#     print("Email is valid")