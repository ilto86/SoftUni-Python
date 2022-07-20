from collections import deque

eggs = deque([int(x) for x in input().split(', ')])
piece_of_paper = deque([int(x) for x in input().split(', ')])
boxes = 0

while eggs and piece_of_paper:
    egg = eggs.popleft()
    paper = piece_of_paper.pop()
    sum_egg_paper = egg + paper

    if egg <= 0:
        piece_of_paper.append(paper)
        continue

    if egg == 13:
        piece_of_paper.append(paper)
        piece_of_paper[-1], piece_of_paper[0] = piece_of_paper[0], piece_of_paper[-1]
        continue

    if sum_egg_paper <= 50:
        boxes += 1
    else:
        continue

if boxes:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join([str(x) for x in eggs])}")
if piece_of_paper:
    print(f"Pieces of paper left: {', '.join([str(x) for x in piece_of_paper])}")
