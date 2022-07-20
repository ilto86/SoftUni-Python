# import string

# def valid_username(data):
#     flag = 0
#     expected_elements = string.digits + string.ascii_letters + '_' + '-'
#     for name in data:
#         flag = 0
#         if 3 > len(name) or len(name) > 16:
#             flag = 1
#         elif len([x for x in name if x in expected_elements]) != len(name):
#             flag = 1
#         elif flag == 0:
#             print(name)
#
# d = input().split(', ')
# valid_username(d)

# usernames = input().split(", ")
#
# for username in usernames:
#     condition = username.isalnum() or "_" in username or "-" in username
#     if 3 <= len(username) <= 16 and condition:
#         print(username)

usernames = input()

for username in usernames.split(", "):
    condition = username.isalnum() or "_" in username or "-" in username
    if 3 <= len(username) <= 16 and condition:
        print(username)