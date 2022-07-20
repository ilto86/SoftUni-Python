# def naughty_or_nice_list(kids, *args, **kwargs):
#     santa_dict = {"Nice": [], "Naughty": [], "Not found": []}
#
#     for command in args:
#         numbers = [int(x[0]) for x in kids]
#         num, nice_or_naughty = command.split("-")
#         num = int(num)
#         if numbers.count(num) > 1:
#             continue
#         for kid in kids:
#             if num == kid[0]:
#                 santa_dict[nice_or_naughty].append(kid[1])
#                 kids.remove(kid)
#
#     for name, nice_or_naughty in kwargs.items():
#         names = [el[1] for el in kids]
#         if names.count(name) > 1:
#             continue
#         for kid in kids:
#             if name == kid[1]:
#                 santa_dict[nice_or_naughty].append(kid[1])
#                 kids.remove(kid)
#
#     result = ""
#
#     if len(santa_dict["Nice"]) > 0:
#         result += f"Nice: {', '.join([el for el in santa_dict['Nice']])}" + "\n"
#     if len(santa_dict["Naughty"]) > 0:
#         result += f"Naughty: {', '.join([el for el in santa_dict['Naughty']])}" + "\n"
#     if kids:
#         result += f"Not found: {', '.join([el[1] for el in kids])}"
#
#     return result.strip()
#
#
#
#
#
# print(naughty_or_nice_list([(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy")],
# "3-Nice", "1-Naughty",
# Amy="Nice", Katy="Naughty"))
#
# Output is:   Nice: Amy
#              Naughty: Tom, Katy
#              Not found: George
#
# print(naughty_or_nice_list([(7, "Peter"), (1, "Lilly"), (2, "Peter"), (12, "Peter"), (3, "Simon")],
# "3-Nice", "5-Naughty", "2-Nice", "1-Nice"))
#
# Output is:    Nice: Simon, Peter, Lilly
#               Not found: Peter, Peter
#
# print(naughty_or_nice_list([(6, "John"), (4, "Karen"), (2, "Tim"), (1, "Merry"), (6, "Frank")],
# "6-Nice", "5-Naughty", "4-Nice", "3-Naughty", "2-Nice", "1-Naughty",
# Frank="Nice", Merry="Nice", John="Naughty"))
#
# Output is:   Nice: Karen, Tim, Frank
#              Naughty: Merry, John





def naughty_or_nice_list(santa_kids_list, *args, **kwargs):

    naughty_nice_dict = {"Nice": [], "Naughty": [], "Not found": []}
    santa_naughty_or_nice_list = ""

    for action in args:
        numbers = [x[0] for x in santa_kids_list]
        commands = action.split("-")
        num = int(commands[0])
        command = commands[1]
        if numbers.count(num) > 1:
            continue

        for kid in santa_kids_list:
            if num == kid[0]:
                naughty_nice_dict[command].append(kid[1])
                santa_kids_list.remove(kid)

    for key, value in kwargs.items():
        names = [el[1] for el in santa_kids_list]
        if names.count(key) > 1:
            continue

        for kid in santa_kids_list:
            if key == kid[1]:
                naughty_nice_dict[value].append(kid[1])
                santa_kids_list.remove(kid)

    if santa_kids_list:
        for kid in santa_kids_list:
            naughty_nice_dict["Not found"].append(kid[1])

    for naughty_or_nice, kids_names in naughty_nice_dict.items():
        if kids_names:
            santa_naughty_or_nice_list += f"{naughty_or_nice}: {', '.join(kids_names)}" + "\n"

    return santa_naughty_or_nice_list





print(naughty_or_nice_list(                      # Output is:   Nice: Amy
 [                                               #              Naughty: Tom, Katy
 (3, "Amy"),                                     #              Not found: George
 (1, "Tom"),
 (7, "George"),
 (3, "Katy"),
 ],
 "3-Nice",
 "1-Naughty",
 Amy="Nice",
 Katy="Naughty",
))

print(naughty_or_nice_list(                     # Output is:    Nice: Simon, Peter, Lilly
 [                                              #               Not found: Peter, Peter
 (7, "Peter"),
 (1, "Lilly"),
 (2, "Peter"),
 (12, "Peter"),
 (3, "Simon"),
 ],
 "3-Nice",
 "5-Naughty",
 "2-Nice",
 "1-Nice",
 ))

print(naughty_or_nice_list(                    # Output is:     Nice: Karen, Tim, Frank
 [                                             #                Naughty: Merry, John
 (6, "John"),
 (4, "Karen"),
 (2, "Tim"),
 (1, "Merry"),
 (6, "Frank"),
 ],
 "6-Nice",
 "5-Naughty",
 "4-Nice",
 "3-Naughty",
 "2-Nice",
 "1-Naughty",
 Frank="Nice",
 Merry="Nice",
 John="Naughty",
))