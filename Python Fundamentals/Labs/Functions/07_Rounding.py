# def convert_list_to_round(base_list):
#     final_list = list()
#     for n in base_list:
#         final_n = round(float(n))
#         final_list.append(final_n)
#
#     return final_list
#
# input_list = input().split(" ")
#
# print(convert_list_to_round(input_list))



# def convert_list_to_round(base_list, num_digits = 0):
#     final_list = list()
#     for n in base_list:
#         final_n = round(float(n), num_digits)
#         final_list.append(final_n)
#
#     return final_list
#
# input_list = input().split(" ")
# current_round = int(input())
# print(convert_list_to_round(input_list, current_round))


def convert_list_to_round(base_list):
    final_list = [round(float(x)) for x in input_list]

    return final_list

input_list = input().split(" ")

print(convert_list_to_round(input_list))