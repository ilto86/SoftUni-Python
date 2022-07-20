# from collections import deque
#
#
# def get_result_operation(current_material, current_magic, last_result):
#     if 100 <= last_result <= 499:
#         return last_result
#
#     elif last_result < 100 and last_result % 2 == 0:
#         even_result = current_material * 2 + current_magic * 3
#         if 100 <= even_result <= 499:
#             return even_result
#         else:
#             return None
#
#     elif last_result < 100 and last_result % 2 != 0:
#         odd_result = last_result * 2
#         if 100 <= odd_result <= 499:
#             return odd_result
#         else:
#             return None
#
#     elif last_result > 499:
#         divide_result = last_result // 2
#         if 100 <= divide_result <= 499:
#             return divide_result
#         else:
#             return None
#
#
# def wedding_presents(gift_1, gift_2, gift_3, gift_4):
#     if (gift_1 > 0 and gift_2 > 0) or (gift_3 > 0 and gift_4 > 0):
#         return print("The wedding presents are made!")
#     else:
#         return print("Aladdin does not have enough wedding presents.")
#
#
# def material_check(material_element):
#     if material_element:
#         return print(f"Materials left: {', '.join([str(x) for x in material_element])}")
#
#
# def magic_chek(magic_level):
#     if magic_level:
#         return print(f"Magic left: {', '.join([str(x) for x in magic_level])}")
#
#
# def gemstone_check(stone):
#         if gemstone > 0:
#             return print(f"Gemstone: {gemstone}")
#
#
# def sculpture_check(sculpture):
#     if porcelain_sculpture > 0:
#         return print(f"Porcelain Sculpture: {sculpture}")
#
#
# def gold_check(gold):
#     if gold > 0:
#         return print(f"Gold: {gold}")
#
#
# def diamond_check(diamond):
#     if diamond_jewellery > 0:
#         print(f"Diamond Jewellery: {diamond}")
#
#
# gemstone = 0
# porcelain_sculpture = 0
# gold = 0
# diamond_jewellery = 0
#
# materials = [int(x) for x in input().split()]
# magic_levels = deque([int(x) for x in input().split()])
#
# while materials and magic_levels:
#     material = materials.pop()
#     magic = magic_levels.popleft()
#     sum_of_material_and_magic = material + magic
#     result = get_result_operation(material, magic, sum_of_material_and_magic)
#
#     if result == None:
#         continue
#
#     if 100 <= result <= 199:
#         gemstone += 1
#
#     elif 200 <= result <= 299:
#         porcelain_sculpture += 1
#
#     elif 300 <= result <= 399:
#         gold += 1
#
#     elif 400 <= result <= 499:
#         diamond_jewellery += 1
#
# wedding_presents(gemstone, porcelain_sculpture, gold, diamond_jewellery)
# material_check(materials)
# magic_chek(magic_levels)
# diamond_check(diamond_jewellery)
# gemstone_check(gemstone)
# gold_check(gold)
# sculpture_check(porcelain_sculpture)



from collections import deque


materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

gemstone = 0
porcelain_sculpture = 0
gold = 0
diamond_jewellery = 0
gifts_1 = False
gifts_2 = False
while materials and magic_levels:
    material = materials[-1]
    magic = magic_levels[0]
    mix_together = material + magic

    if mix_together < 100:
        if mix_together % 2 == 0:
            material *= 2
            magic *= 3
            mix_together = material + magic
        else:
            mix_together *= 2

    if mix_together > 499:
        mix_together = mix_together / 2

    if 100 <= mix_together <= 199:
        gemstone += 1
        if porcelain_sculpture:
            gifts_1 = True
    if 200 <= mix_together <= 299:
        porcelain_sculpture += 1
        if gemstone:
            gifts_1 = True
    if 300 <= mix_together <= 399:
        gold += 1
        if diamond_jewellery:
            gifts_2 = True
    if 400 <= mix_together <= 499:
        diamond_jewellery += 1
        if gold:
            gifts_2 = True

    materials.pop()
    magic_levels.popleft()

if gifts_1 or gifts_2:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")


if diamond_jewellery:
    print(f"Diamond Jewellery: {diamond_jewellery}")
if gemstone:
    print(f"Gemstone: {gemstone}")
if gold:
    print(f"Gold: {gold}")
if porcelain_sculpture:
    print(f"Porcelain Sculpture: {porcelain_sculpture}")