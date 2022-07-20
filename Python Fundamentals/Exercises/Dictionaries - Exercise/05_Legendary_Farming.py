def print_func(legendary_items_dict, junk_items_dict, special_item):
    print(f"{special_item} obtained!")
    print(f"shards: {legendary_items_dict['shards']}")
    print(f"fragments: {legendary_items_dict['fragments']}")
    print(f"motes: {legendary_items_dict['motes']}")

    for key, value in junk_items_dict.items():
        print(f"{key}: {value}")

def legendary_farming():
    legendary_items_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
    junk_items_dict = {}
    while_condition = False

    while True:
        items = input().lower()
        items = items.split()

        for value, materials in zip(items[0::2], items[1::2]):
            material = materials
            value = int(value)

            if material in ['shards', 'fragments', 'motes']:
                if material not in legendary_items_dict:
                    legendary_items_dict[material] = value
                else:
                    legendary_items_dict[material] += value

                if legendary_items_dict[material] >= 250:
                    legendary_items_dict[material] -= 250
                    special_item = ''
                    if material == 'shards':
                        special_item = 'Shadowmourne'
                    elif material == 'fragments':
                        special_item = 'Valanyr'
                    elif material == 'motes':
                        special_item = 'Dragonwrath'

                    print_func(legendary_items_dict, junk_items_dict, special_item)
                    while_condition = True

            else:
                if material not in junk_items_dict:
                    junk_items_dict[material] = value
                else:
                    junk_items_dict[material] += value

            if while_condition:
                break
        if while_condition:
            break

legendary_farming()




# def collect_material(key_materials_dict: dict, junk_materials: dict, material: str, quantity: int):
#     if material == 'shards' or material == 'fragments' or material == 'motes':
#         # Key material is found
#         key_materials_dict[material] += quantity
#     else:
#         if material not in junk_materials.keys():
#             # Material still does not exist in the junk
#             junk_materials[material] = quantity
#         else:
#             # Material already exists in the junk and we need to add the quantity
#             junk_materials[material] += quantity
#
#
# key_materials = {"shards": 0, "fragments": 0, "motes": 0}
# junk = {}
# item_obtained = ''
#
# # While item is still not obtained (empty string)
# while item_obtained == '':
#     current_line = input().split()
#
#     for i in range(0, len(current_line), 2):
#         material_quantity = int(current_line[i])
#         material_name = current_line[i + 1].lower()
#
#         collect_material(key_materials, junk, material_name, material_quantity)
#
#         if key_materials['shards'] >= 250:
#             item_obtained = 'Shadowmourne'
#             key_materials['shards'] -= 250
#             break
#         elif key_materials['fragments'] >= 250:
#             item_obtained = 'Valanyr'
#             key_materials['fragments'] -= 250
#             break
#         elif key_materials['motes'] >= 250:
#             item_obtained = 'Dragonwrath'
#             key_materials['motes'] -= 250
#             break
#
# print(f"{item_obtained} obtained!")
# # sorted_dict = sorted(key_materials.items(), key=lambda kvp: (-kvp[1], kvp[0]))
# for (key_material_name, key_material_quantity) in key_materials.items():
#     print(f"{key_material_name}: {key_material_quantity}")
#
# # sorted_junks = sorted(junk.items(), key=lambda kvp: kvp[0])
# for (junk_material_name, junk_material_quantity) in junk.items():
#     print(f"{junk_material_name}: {junk_material_quantity}")