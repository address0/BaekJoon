import sys
sys.stdin = open('input.txt', 'r')
T = int(input())

def dfs(i, k, t):
    global max_total
    if i == k:
        if t > max_total:
            max_total = t
            return
    elif t < max_total:
        return
    else:
        for j in range(n):
            if bit[j] == 0 and pds[i][j]:
                bit[j] = 1
                dfs(i+1, k, t*0.01*(pds[i][j]))
                bit[j] = 0

for x in range(T):
    n = int(input())
    pds = [list(map(int, input().split())) for _ in range(n)]
    bit = [0]*n
    max_total = 0
    dfs(0, n, 100)
    print(f'#{x+1} {max_total:.6f}')