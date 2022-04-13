# type_of_client_and_pc_price = input()
# tax = 0.20
# total_price = 0
#
# while type_of_client_and_pc_price != "special" and type_of_client_and_pc_price != "regular":
#     prices = float(type_of_client_and_pc_price)
#     if prices < 0:
#         print("Invalid price!")
#         type_of_client_and_pc_price = input()
#         continue
#     total_price += prices
#
#     type_of_client_and_pc_price = input()
#
# tax_price = total_price * tax
# total_price_with_tax = total_price + tax_price
# if type_of_client_and_pc_price == "special":
#     total_price_with_tax -= total_price_with_tax * 0.10
# if total_price <= 0:
#     print("Invalid order!")
# else:
#     print("Congratulations you've just bought a new computer!")
#     print(f"Price without taxes: {total_price:.2f}$")
#     print(f"Taxes: {tax_price:.2f}$")
#     print("-----------")
#     print(f"Total price: {total_price_with_tax:.2f}$")




# type_of_client_and_pc_price = input()
# tax = 0.20
# total_price = 0
#
# while type_of_client_and_pc_price != "special" and type_of_client_and_pc_price != "regular":
#     prices = float(type_of_client_and_pc_price)
#     if prices < 0:
#         print("Invalid price!")
#         type_of_client_and_pc_price = input()
#         continue
#     total_price += prices
#
#     type_of_client_and_pc_price = input()
#
# tax_price = total_price * tax
# total_price_with_tax = total_price + tax_price
# if type_of_client_and_pc_price == "special":
#     total_price_with_tax -= total_price_with_tax * 0.10
# if total_price <= 0:
#     print("Invalid order!")
# else:
#     print("Congratulations you've just bought a new computer!")
#     print(f"Price without taxes: {total_price:.2f}$")
#     print(f"Taxes: {tax_price:.2f}$")
#     print("-----------")
#     print(f"Total price: {total_price_with_tax:.2f}$")


prices_without_tax = 0

while True:
    data = input()

    if data == "special" or data == "regular":
        break
    else:
        price = float(data)

    if price > 0:
        prices_without_tax += price
    else:
        print("Invalid price!")

tax = prices_without_tax * 0.2
total_price = tax + prices_without_tax

if prices_without_tax <= 0:
    print("Invalid order!")

else:
    if data == "special":
        special_price = total_price * 0.1
        total_price -= special_price
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {prices_without_tax:.2f}$")
    print(f"Taxes: {tax:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")



prices_without_tax = 0

while True:
    data = input()

    if data == "special" or data == "regular":
        break
    elif float(data) < 0:
        print("Invalid price!")
    else:
        prices_without_tax += float(data)

tax = prices_without_tax * 0.2
total_price = tax + prices_without_tax
if prices_without_tax <= 0:
    print("Invalid order!")
elif data == "special":
    special_price = total_price * 0.1
    total_price = total_price - special_price
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {prices_without_tax:.2f}$\nTaxes: {tax:.2f}$\n-----------\nTotal price: {total_price:.2f}$")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {prices_without_tax:.2f}$")
    print(f"Taxes: {tax:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")