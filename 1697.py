import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
result = 0
temp = 0
q = deque()
q.append(n)
while True:
    num = q.popleft()
    if num == k:
        break
    else:
        q.append(num-1)
        q.append(num+1)
        q.append(2*num)
        temp += 1
    if temp == 3**result:
        result += 1
        temp = 0
print(result)