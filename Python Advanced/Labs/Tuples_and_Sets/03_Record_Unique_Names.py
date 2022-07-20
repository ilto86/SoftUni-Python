n = int(input())
names = set()

for _ in range(n):
    name = input()
    names.add(name)

print("\n".join(names))

# [print(name) for name in {input() for _ in range(int(input()))}]


# n = int(input())
# names_set = {input() for _ in range(n)}
# [print(name) for name in names_set]



# n = int(input())
#
# names_set = set()
#
# for _ in range(n):
#     names_set.add(input())
#
# # [print(name) for name in names_set]
# for name in names_set:
#     print(name)



# count = int(input())
#
# names_list = []
#
# for _ in range(count):
#     data = input()
#     names_list.append(data)
#
# unique_names_list = {name for name in names_list}
#
# for name in unique_names_list:
#     print(name)