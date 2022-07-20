n = int(input())

result = set()

for _ in range(n):
    current_set = set(input().split())
    result = result.union(current_set)

print(*result, sep="\n")
# [print(el) for el in result]
# for el in result:
#     print(el)







# n = int(input())
# unique_elements = set()
#
# for _ in range(n):
#     chemical_elements = input().split()
#     for idx in range(len(chemical_elements)):
#         chemical_compounds = chemical_elements[idx]
#         unique_elements.add(chemical_compounds)
#
# print("\n".join(unique_elements))