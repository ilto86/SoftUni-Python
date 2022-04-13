# input_list = input().split(" ")
# abs_list = list()
#
# for n in input_list:
#  current_abs = abs(float(n))
#  abs_list.append(current_abs)
#
# print(abs_list)



input_list = input().split(" ")
abs_list = [abs(float(i)) for i in input_list]
print(abs_list)