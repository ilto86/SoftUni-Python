# items = {}
#
# while True:
#     command = input()
#     if command == 'buy':
#         break
#
#     tokens = command.split()
#
#     product = tokens[0]
#     price = float(tokens[1])
#     quantity = int(tokens[2])
#
#     if product not in items:
#         items[product] = []
#         items[product].append(price)
#         items[product].append(quantity)
#     else:
#         items[product][1] += quantity
#         if price != items[product][0]:
#             items[product].pop(0)
#             items[product].insert(0, price)
#
# [print(f'{i} -> {(j[0] * j[1]):.2f}') for i, j in items.items()]
# # for i, j in items.items():
# #     total_price = j[0] * j[1]
# #     print(f'{i} -> {total_price:.2f}')





def orders_func(orders_dict, command):
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if product in orders_dict:
        orders_dict[product] = [price, (quantity + orders_dict[product][1])]
    else: orders_dict[product] = [price, quantity]

    return orders_dict

def orders():
    orders_dict = {}

    while True:
        command = input()

        if command == 'buy':
            break

        command = command.split()
        orders_dict = orders_func(orders_dict, command)

    for k in orders_dict:
        total_sum = orders_dict[k][0] * orders_dict[k][1]
        print(f"{k} -> {total_sum:.2f}")

orders()