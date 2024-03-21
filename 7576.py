import sys
input = sys.stdin.readline
m, n = map(int, input().split())
toms = [list(map(int, input().split())) for _ in range(n)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
day = 0
while True:
    change = False
    ripe = True
    for i in range(n):
        for j in range(m):
            if toms[i][j] == 1:
                for k in range(4):
                    if 0 <= i+di[k] < n and 0 <= j+dj[k] < m:
                        if not toms[i+di[k]][j+dj[k]]:
                            toms[i + di[k]][j + dj[k]] = 1
                            change = True
            elif not toms[i][j]:
                ripe = False
    day += 1
    if not change or ripe:
        break
if not ripe:
    print(-1)
else:
    print(day-1)