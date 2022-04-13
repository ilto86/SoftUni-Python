items = input().split("|")
budget = float(input())

new_prices = []
total_profit = 0

for item in items:
    item_info = item.split("->")
    item_type = item_info[0]
    item_price = float(item_info[1])

    is_bought = False

    if budget <= 0:
        break

    if item_type == "Clothes" and item_price <= 50.00:
        is_bought = True
    elif item_type == "Shoes" and item_price <= 35.00:
        is_bought = True
    elif item_type == "Accessories" and item_price <= 20.50:
        is_bought = True


    if is_bought:
        if budget >= item_price:
            budget -= item_price
            new_price = item_price + (item_price * 0.4)
            new_prices.append(f"{new_price:.2f}")
            total_profit += item_price * 0.40

print(" ".join(new_prices))
print(f"Profit: {total_profit:.2f}")

for price in new_prices:
    budget += float(price)

if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")



# items = input().split("|")
# budget = int(input())
#
# data_prices = []
# new_item_prices = []
# profit = 0
# condition = False
#
# for item in items:
#     current_item_info = item.split("->")
#     type_of_product = current_item_info[0]
#     price = float(current_item_info[1])
#     condition = False
#
#     if type_of_product == "Clothes" and price <= 50.00:
#             condition = True
#     elif type_of_product == "Shoes" and price <= 35.00:
#         condition = True
#     elif type_of_product == "Accessories" and price <= 20.50:
#         condition = True
#
#     if condition:
#         if budget >= price:
#             budget -= price
#             profit += price * 0.40
#             new_price = price + (price * 0.40)
#             new_item_prices.append(new_price)
#             data_prices.append(f"{new_price:.2f}")
#
#
# print(" ".join(data_prices))
# print(f"Profit: {profit:.2f}")
#
# total_sum = budget + sum(new_item_prices)
#
# if total_sum >= 150:
#     print("Hello, France!")
# else:
#     print("Not enough money.")