import sys
from collections import Counter

cardlen = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
findlen = int(sys.stdin.readline())
find = list(map(int, sys.stdin.readline().split()))

card_counts = Counter(card)
result = [str(card_counts[i]) for i in find]
print(' '.join(result))