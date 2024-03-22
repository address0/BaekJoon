import sys
sys.stdin = open('input.txt', 'r')
t = int(input())
def dfs(i, height):
    if height >= b:
        global result
        result = min(result, height)
        return
    if i == n:
        return
    dfs(i+1, height+h[i])
    dfs(i+1, height)
for x in range(t):
    n, b = map(int, input().split())
    h = list(map(int, input().split()))
    result = int(1e9)
    dfs(0, 0)
    print(f'#{x+1} {result-b}')
