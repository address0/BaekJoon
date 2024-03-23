# 시간초과

import sys
input = sys.stdin.readline
m, n = map(int, input().split())
toms = [list(map(int, input().split())) for _ in range(n)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
day = 0
while True:
    st = []
    ripe = True
    for i in range(n):
        for j in range(m):
            if toms[i][j] == 1:
                for k in range(4):
                    if 0 <= i+di[k] < n and 0 <= j+dj[k] < m:
                        if not toms[i+di[k]][j+dj[k]]:
                            st.append([i + di[k], j + dj[k]])
            elif not toms[i][j]:
                ripe = False
    day += 1
    if st:
        for tom in st:
            toms[tom[0]][tom[1]] = 1
    if not st or ripe:
        break
if not ripe:
    print(-1)
else:
    print(day-1)
