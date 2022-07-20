def shopping_list(num, **kwargs):
    budget = num
    purchased_items = ""
    amount_of_product = 5

    if budget < 100:
        return "You do not have enough budget."

    else:
        for key, value in kwargs.items():
            product_name = key
            price = value[0]
            quantity = value[1]
            total_price = price * quantity
            if budget - total_price >= 0:
                budget -= total_price
                amount_of_product -= 1
                purchased_items += f"You bought {product_name} for {total_price:.2f} leva." + "\n"
            if budget <= 0 or not amount_of_product:
                break

        return purchased_items



print(shopping_list(100, microwave=(70, 2), skirts=(15, 4), coffee=(1.50, 10),))

print(shopping_list(20, jeans=(19.99, 1),))

print(shopping_list(104, cola=(1.20, 2), candies=(0.25, 15), bread=(1.80, 1), pie=(10.50, 5),
                    tomatoes=(4.20, 1), milk=(2.50, 2), juice=(2, 3), eggs=(3, 1),))






# def shopping_list(money, **kwargs):
#     budget = money
#     if budget < 100:
#         return "You do not have enough budget."
#
#     items_list = {}
#     for key, value in kwargs.items():
#         product = key
#         product_price = value[0]
#         product_quantity = value[1]
#         total_price = product_price * product_quantity
#
#         if total_price < budget:
#             budget -= total_price
#             items_list[product] = total_price
#
#         if len(items_list) == 5:
#             break
#
#     items_result = ""
#     for k, v in items_list.items():
#         items_result += f"You bought {k} for {v:.2f} leva." + "\n"
#
#     return items_result
#
#
# print(shopping_list(100, microwave=(70, 2), skirts=(15, 4), coffee=(1.50, 10),))
#
# print(shopping_list(20, jeans=(19.99, 1),))
#
# print(shopping_list(104, cola=(1.20, 2), candies=(0.25, 15), bread=(1.80, 1), pie=(10.50, 5),
#                     tomatoes=(4.20, 1), milk=(2.50, 2), juice=(2, 3), eggs=(3, 1),))








# budget = int(input())
#
# products = {
#     "cola": (1.20, 2),
#     "candies": (0.25, 15),
#     "bread": (1.80, 1),
#     "pie": (10.50, 5),
#     "tomatoes": (4.20, 1),
#     "milk": (2.50, 2),
#     "juice": (2, 3),
#     "eggs": (3, 1),
#     "microwave": (70, 2),
#     "skirts": (15, 4),
#     "coffee": (1.50, 10),
#     "jeans": (19.99, 1)
# }
# purchased_items = ""
# for key, value in products.items():
#     product_name = key
#     price = value[0]
#     quantity = value[1]
#     total_price = price * quantity
#     if budget - total_price >= 0:
#         budget -= total_price
#         purchased_items += f"You bought {product_name} for {total_price:.2f} leva.\n"
#     if budget <= 0:
#         break
#
# print(purchased_items)