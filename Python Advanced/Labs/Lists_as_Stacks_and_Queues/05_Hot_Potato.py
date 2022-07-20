# from collections import deque
# import time
#
# start_time = time.time()
#
# kids = deque(input().split())
# n = int(input())
#
# while len(kids) > 1:
#     kids.rotate(-n)
#     print(f"Removed {kids.pop()}")
#
# print(f"Last is {kids.pop()}")
#
# print("--- %s seconds ---" % (time.time() - start_time))




# from collections import deque
#
# kids = deque(input().split())
# tosses = int(input())
#
# while len(kids) > 1:
#     for num in range(1, tosses + 1):
#         if num % tosses == 0:
#             print(f"Removed {kids.popleft()}")
#             break
#         kids.append(kids.popleft())
#
# print(f"Last is {''.join(kids)}")







from collections import deque

queue = deque(input().split())
count = int(input())

while len(queue) > 1:
    queue.rotate(-count)
    print(f"Removed {queue.pop()}")

print(f"Last is {queue.pop()}")