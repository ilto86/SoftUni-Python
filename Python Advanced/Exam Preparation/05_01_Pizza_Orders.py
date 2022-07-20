from collections import deque


DOES_NOT_TAKE = 10
INVALID = 0

pizza_orders = deque(input().split(", "))
employees = input().split(", ")
total_count = 0

while employees and pizza_orders:
    pizza = int(pizza_orders.popleft())
    pizza_making_capacities = int(employees.pop())

    if pizza <= INVALID:
        employees.append(str(pizza_making_capacities))

    elif pizza > DOES_NOT_TAKE:
        employees.append(str(pizza_making_capacities))

    elif pizza <= pizza_making_capacities:
        total_count += pizza

    else:
        left_pizza = pizza - pizza_making_capacities
        total_count += pizza_making_capacities
        pizza_orders.appendleft(str(left_pizza))

if pizza_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(pizza_orders)}")
else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_count} ")
    print(f"Employees: {', '.join(employees)}")