from collections import deque

bowls_of_ramen = [int(x) for x in input().split(", ")]
customers = deque([int(x) for x in input().split(", ")])

while customers and bowls_of_ramen:
    bowl_ramen = bowls_of_ramen.pop()
    customer = customers.popleft()

    if bowl_ramen > customer:
        bowls_of_ramen.append(bowl_ramen - customer)
    elif customer > bowl_ramen:
        customers.appendleft(customer - bowl_ramen)


if customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")
else:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join([str(x) for x in bowls_of_ramen])}")