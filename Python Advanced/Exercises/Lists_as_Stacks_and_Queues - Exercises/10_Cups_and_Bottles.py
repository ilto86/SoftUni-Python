cups = [int(x) for x in input().split()]
bottles = [int(x) for x in input().split()]
wasted_liters = 0

while True:
    if len(bottles) <= 0 or len(cups) <= 0:
        break

    current_bottle = bottles[-1]
    current_cup = cups[0]

    if current_bottle - current_cup > 0:
        picking_bottle = bottles.pop()
        filling_cup = cups.pop(0)
        wasted_liters += picking_bottle - filling_cup
    elif current_cup - current_bottle > 0:
        picking_bottle = bottles.pop()
        cups[0] -= picking_bottle
    else:
        picking_bottle = bottles.pop()
        filling_cup = cups.pop(0)

if bottles:
    print(f"Bottles:", *bottles)
elif cups:
    print(f"Cups:", *cups)
print(f"Wasted litters of water: {wasted_liters}")