# data = input()
#
# products = {}
#
# while not data == "stop":
#     resource_name = data
#     int_data = int(input())
#     resource_quantity = int_data
#     if resource_name not in products:
#         products[resource_name] = int(resource_quantity)
#     else:
#         products[resource_name] += int(resource_quantity)
#     data = input()
#
# for resource, quantity in products.items():
#     print(f"{resource} -> {quantity}")





def miner_task():
    items_dict = {}

    while True:
        resource = input()

        if resource == 'stop':
            break

        quantity = int(input())

        if resource not in items_dict:
            items_dict[resource] = quantity
        else:
            items_dict[resource] += quantity

    for key, value in items_dict.items():
        print(f"{key} -> {value}")

miner_task()