from collections import deque

price_of_each_bullet = int(input())
size_of_the_gun_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = [int(x) for x in input().split()]
locks_queue = deque(locks)
value_of_the_intelligence = int(input())
total_bullets_prices = 0
safe_is_open = False
safe_is_not_open = False


while locks:
    for _ in range(size_of_the_gun_barrel):
        if not locks_queue:
            safe_is_open = True
            break
        if not bullets:
            safe_is_not_open = True
            break

        if bullets[-1] <= locks_queue[0] and locks_queue and bullets:
            bullets.pop()
            locks_queue.popleft()
            print("Bang!")
            total_bullets_prices += price_of_each_bullet
        elif bullets[-1] > locks_queue[0] and locks_queue and bullets:
            bullets.pop()
            print("Ping!")
            total_bullets_prices += price_of_each_bullet
    if safe_is_open or safe_is_not_open:
        break
    if bullets:
        print("Reloading!")

if locks_queue:
    print(f"Couldn't get through. Locks left: {len(locks_queue)} ")
else:
    money_earned = value_of_the_intelligence - total_bullets_prices
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")