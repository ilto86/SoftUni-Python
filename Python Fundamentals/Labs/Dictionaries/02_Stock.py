# data = input().split()
# searched_products = input().split()
#
# products = {}
#
# for index in range(0, len(data), 2):
#     key = data[index]
#     value = int(data[index + 1])
#     products[key] = value
#
# for matched_product in searched_products:
#     if matched_product in products:
#         print(f"We have {products[matched_product]} of {matched_product} left")
#     else:
#         print(f"Sorry, we don't have {matched_product}")


# data = input().split(" ")
# search_data = input().split(" ")
# bakery = dict()
#
# for i in range(0, len(data), 2):
#     food = data[i]
#     quantity = int(data[i + 1])
#     bakery[food] = quantity
#
# for search_term in search_data:
#     if search_term in bakery.keys():
#         print(f"We have {bakery[search_term]} of {search_term} left")
#     else:
#         print(f"Sorry, we don't have {search_term}")



bakery_dict = {}
stock = input().split()
searched_products = input().split()

for i in range(0, len(stock), 2):
    key = stock[i]
    value = stock[i + 1]
    bakery_dict[key] = int(value)

for searched in searched_products:
    if searched in bakery_dict:
        print(f"We have {bakery_dict[searched]} of {searched} left")
    else:
        print(f"Sorry, we don't have {searched}")










