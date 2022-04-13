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
