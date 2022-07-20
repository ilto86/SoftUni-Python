# number_of_pieces = int(input())
#
# pieces_dict = {}
#
# for n in range(number_of_pieces):
#     piece_info = input().split('|')
#     piece_name = piece_info[0]
#     composer = piece_info[1]
#     piece_key = piece_info[2]
#
#     if piece_name not in pieces_dict:
#         pieces_dict[piece_name] = {'composer': composer, 'piece_key': piece_key}
#
# while True:
#     command = input().split('|')
#     if command[0] == 'Stop':
#         break
#     action = command[0]
#     if action == 'Add':
#         piece_name = command[1]
#         composer = command[2]
#         piece_key = command[3]
#         if piece_name not in pieces_dict:
#             pieces_dict[piece_name] = {'composer': composer, 'piece_key': piece_key}
#             print(f"{piece_name} by {composer} in {piece_key} added to the collection!")
#         else:
#             print(f"{piece_name} is already in the collection!")
#
#     elif action == 'Remove':
#         piece_name = command[1]
#         if piece_name in pieces_dict:
#             del pieces_dict[piece_name]
#             print(f"Successfully removed {piece_name}!") # check if the deleted piece cannot be displayed
#         else:
#             print(f"Invalid operation! {piece_name} does not exist in the collection.")
#
#     elif action == 'ChangeKey':
#         piece_name = command[1]
#         new_key = command[2]
#         if piece_name in pieces_dict:
#             pieces_dict[piece_name]['piece_key'] = new_key
#             print(f'Changed the key of {piece_name} to {new_key}!')
#         else:
#             print(f'Invalid operation! {piece_name} does not exist in the collection.')
#
# sorted_pieces_dict = dict(sorted(pieces_dict.items(), key=lambda x: (x, x[0])))
#
# for piece, details in sorted_pieces_dict.items():
#     print(f"{piece} -> Composer: {details['composer']}, Key: {details['piece_key']}")




# n = int(input())
#
# data = {}
#
# for _ in range(n):
#     piece_name, composer, key = input().split("|")
#     data[piece_name] = [composer, key]
#
# command = input()
#
# while not command == "Stop":
#     command_type = command.split("|")[0]
#
#     if command_type == "Add":
#         piece, composer, key = command.split("|")[1:]
#         if piece not in data:
#             data[piece] = [composer, key]
#             print(f"{piece} by {composer} in {key} added to the collection!")
#         else:
#             print(f"{piece} is already in the collection!")
#
#     elif command_type == "Remove":
#         piece = command.split("|")[1]
#         if piece not in data:
#             print(f"Invalid operation! {piece} does not exist in the collection.")
#         else:
#             del data[piece]
#             print(f"Successfully removed {piece}!")
#
#     elif command_type == "ChangeKey":
#         piece, new_key = command.split("|")[1:]
#         if piece not in data:
#             print(f"Invalid operation! {piece} does not exist in the collection.")
#         else:
#             data[piece][-1] = new_key
#             print(f"Changed the key of {piece} to {new_key}!")
#
#     command = input()
#
# sorted_data = dict(sorted(data.items()))
#
# for key, value in sorted_data.items():
#     print (f"{key} -> Composer: {value[0]}, Key: {value[1]}")




# def add_piece(pieces, piece, composer, key):
# 	if piece in pieces:
# 		print(f"{piece} is already in the collection!")
# 	else:
# 		pieces[piece] = {"composer": composer, "key": key}
# 		print(f"{piece} by {composer} in {key} added to the collection!")
# 	return pieces
#
#
# def remove_piece(pieces, piece):
# 	if piece not in pieces:
# 		print(f"Invalid operation! {piece} does not exist in the collection.")
# 	else:
# 		del pieces[piece]
# 		print(f"Successfully removed {piece}!")
# 	return pieces
#
#
# def change_key(pieces, piece, key):
# 	if piece not in pieces:
# 		print(f"Invalid operation! {piece} does not exist in the collection.")
# 	else:
# 		pieces[piece]["key"] = key
# 		print(f"Changed the key of {piece} to {key}!")
# 	return pieces
#
#
# def get_pieces():
# 	pieces = {}
# 	n = int(input())
# 	for _ in range(n):
# 		piece, composer, key = input().split("|")
# 		pieces[piece] = {"composer": composer, "key": key}
# 	return pieces
#
#
# def print_pieces(pieces):
# 	pieces = dict(sorted(pieces.items(), key=lambda x: (x[0], x[1]["composer"])))
# 	for name, values in pieces.items():
# 		print(f"{name} -> Composer: {values['composer']}, Key: {values['key']}")
#
#
# def main():
# 	pieces = get_pieces()
# 	while True:
# 		command = input()
# 		if command == "Stop":
# 			break
# 		action, *token = command.split("|")
# 		if action == "Add":
# 			piece, composer, key = token
# 			pieces = add_piece(pieces, piece, composer, key)
# 		elif action == "Remove":
# 			piece = token[0]
# 			pieces = remove_piece(pieces, piece)
# 		elif action == "ChangeKey":
# 			piece, key = token
# 			pieces = change_key(pieces, piece, key)
# 	print_pieces(pieces)
#
#
# main()




number_of_pieces = int(input())
collection = {}

for piece in range(number_of_pieces):
    data = input().split("|")
    collection[data[0]] = [data[1], data[2]]

while True:
    data = input()

    if data == "Stop":
        break
    commands = data.split("|")
    command, piece = commands[0], commands[1]

    if command == "Add":
        composer, key = commands[2], commands[3]
        if piece in collection:
            print(f"{piece} is already in the collection!")
        else:
            collection[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif command == "Remove":
        if piece in collection:
            del collection[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command == "ChangeKey":
        new_key = commands[2]
        if piece in collection:
            collection[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for key, value in collection.items():
    piece, composer, key = key, value[0], value[1]
    print(f"{piece} -> Composer: {composer}, Key: {key}")