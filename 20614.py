import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
def dfs(i, k, t):
    global min_total
    if i == k:
        if t < min_total:
            min_total = t
            return
    elif t >= min_total:
        return
    else:
        for j in range(1, n+1):
            if j not in bit:
                bit[i] = j
                dfs(i+1, k, t+pds[i][bit[i]-1])
                bit[i] = 0

for x in range(T):
    n = int(input())
    pds = [list(map(int, input().split())) for _ in range(n)]
    bit = [0]*n
    min_total = 50000
    dfs(0, n, 0)
    print(f'#{x+1} {min_total}')