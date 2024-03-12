import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_d = 0
for n in range(1, 100):
    for i in range(n):
        for j in range(n):
            if arr[i][j] <= n:
                arr[i][j] = 0
    pass