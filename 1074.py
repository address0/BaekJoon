import sys
input = sys.stdin.readline
n, r, c = map(int, input().split())
start = [0, 0]
result = 0
for i in range(n):
    center = [start[0] + 2**(n-i-1), start[1] + 2**(n-i-1)]
    if r < center[0] and c < center[1]:
        continue
    elif r < center[0] and c >= center[1]:
        start[1] = center[1]
        result += 4**(n-i-1)
    elif r >= center[0] and c < center[1]:
        start[0] = center[0]
        result += 4**(n-i-1)*2
    else:
        start[0] = center[0]
        start[1] = center[1]
        result += 4 ** (n-i-1) * 3
print(result)