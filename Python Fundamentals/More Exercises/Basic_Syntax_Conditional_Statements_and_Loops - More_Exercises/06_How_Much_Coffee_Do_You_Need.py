# def in_list(word):
#     test_list = ["coding", "dog", "cat", "movie"]
#     if word.lower() in test_list:
#         return True
#     return False
#
# coffee_counter = 0
#
# while True:
#     command = input()
#     if command == "END":
#         break
#
#     if in_list(command) and command.islower():
#         coffee_counter += 1
#     elif in_list(command) and command.isupper():
#         coffee_counter += 2
#
# if coffee_counter > 5:
#     print('You need extra sleep')
# else:
#     print(coffee_counter)

# coffees_count = 0
# command = input()
#
# while not command == 'END':
#     if command.lower() in ['coding', 'cat', 'dog', 'movie']:
#         if command == command.lower():
#             coffees_count += 1
#         elif command == command.upper():
#             coffees_count += 2
#     command = input()
#
# if coffees_count > 5:
#     print('You need extra sleep')
# else:
#     print(coffees_count)

activity = input()

coffees = 0
while activity != 'END':

    if activity == 'CODING' or activity == 'DOG' or activity == 'CAT' or activity == 'MOVIE':
        coffees += 2

    elif activity == 'coding' or activity == 'dog' or activity == 'cat' or activity == 'movie':
        coffees += 1
    else:
        activity = input()
        continue
    activity = input()

if coffees > 5:
    print(f'You need extra sleep')
else:
    print(f'{coffees}')