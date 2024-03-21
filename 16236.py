import sys
input = sys.stdin.readline
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
si, sj = 0, 0
find_s = False
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            si, sj = i, j
            find_s = True
            break
    if find_s:
        break
st = [[si, sj]]
visited = []
while st:
    pass