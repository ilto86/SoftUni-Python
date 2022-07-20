# data = input()
# products = {}
#
# while not data == "statistics":
#     product_name, product_quantity = data.split(": ")
#     if product_name not in products:
#         products[product_name] = int(product_quantity)
#     else:
#         products[product_name] += int(product_quantity)
#     data = input()
#
# print("Products in stock:")
#
# for key, value in products.items():
#     print(f"- {key}: {value}")
#
# print(f"Total Products: {len(products.keys())}")
# print(f"Total Quantity: {sum(products.values())}")




text = input()

store = dict()

while text != "statistics":

    text = text.split(": ")
    product = text[0]
    quantity = int(text[1])

    if product in store.keys():
        store[product] += quantity
    else:
        store[product] = quantity

    text = input()

count = len(store.keys())
total = sum(store.values())

print("Products in stock:")
for product in store:
    print(f"- {product}: {store[product]}")
print(f"Total Products: {count}")
print(f"Total Quantity: {total}")