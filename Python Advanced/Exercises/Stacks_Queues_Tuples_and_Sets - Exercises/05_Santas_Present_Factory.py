# from collections import deque
#
# materials = [int(x) for x in input().split()]
# magic_values = deque([int(x) for x in input().split()])
#
# crafting_table = {
#     150: "Doll",
#     250: "Wooden train",
#     300: "Teddy bear",
#     400: "Bicycle"
# }
# crafted_toys = {}
#
# while materials and magic_values:
#     material = materials.pop()
#     value = magic_values.popleft()
#
#     if material == 0 and value == 0:
#         continue
#
#     if material == 0:
#         magic_values.appendleft(value)
#         continue
#
#     if value == 0:
#         materials.append(material)
#         continue
#
#     result = material * value
#     if result in crafting_table:
#         toy_name = crafting_table[result]
#         if toy_name in crafted_toys:
#             crafted_toys[toy_name] += 1
#         else:
#             crafted_toys[toy_name] = 1
#         continue
#
#     if result < 0:
#         materials.append(material + value)
#     else:
#         materials.append(material + 15)
#
# if ("Doll" in crafted_toys and "Wooden train" in crafted_toys) or ("Teddy bear" in crafted_toys and "Bicycle" in crafted_toys):
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")
#
# if materials:
#     print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")
# if magic_values:
#     print(f"Magic left: {', '.join([str(x) for x in magic_values])}")
#
# for toy, count in sorted(crafted_toys.items()):
#     print(f"{toy}: {count}")








from collections import deque

materials_boxes = [int(x) for x in input().split()]
magic_values = deque([int(x) for x in input().split()])

toys = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
 }

crafted_toys = {}

while materials_boxes and magic_values:
    material = materials_boxes.pop()
    magic_value = magic_values.popleft()
    operation = material * magic_value

    if material == 0 and magic_value == 0:
        continue

    if material == 0:
        magic_values.appendleft(magic_value)
        continue

    if magic_value == 0:
        materials_boxes.append(material)
        continue

    if operation in toys:
        toy_name = toys[operation]
        if toy_name in crafted_toys:
            crafted_toys[toy_name] += 1
        else:
            crafted_toys[toy_name] = 1
        continue

    if operation < 0:
        materials_boxes.append(material + magic_value)
    else:
        materials_boxes.append(material + 15)

if ("Doll" in crafted_toys and "Wooden train" in crafted_toys) or ("Teddy bear" in crafted_toys and "Bicycle" in crafted_toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials_boxes:
    print(f"Materials left: {', '.join([str(x) for x in materials_boxes[::-1]])}")
if magic_values:
    print(f"Magic left: {', '.join([str(x) for x in magic_values])}")

for toy, count in sorted(crafted_toys.items()):
    print(f"{toy}: {count}")