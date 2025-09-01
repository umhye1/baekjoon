import sys
from collections import deque

num = int(sys.stdin.readline())
cards = deque([ i+1 for i in range(num)])

while len(cards) != 1:
    cards.popleft()
    n = cards.popleft()
    cards.append(n)

print(*cards)

