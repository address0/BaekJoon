import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n = int(input())
roads = [[] for _ in range(n+1)]
def dfs(v, leng):
    global max_len
    if leng > max_len:
        max_len = leng
    visited[v] = 1
    for road in roads[v]:
        if visited[road[0]]:
            continue
        dfs(road[0], leng+road[1])
for _ in range(n-1):
    a, b, c = map(int, input().split())
    roads[a].append([b, c])
    roads[b].append([a, c])
max_len = 0
visited = [0]*(n+1)
visited[1] = 1
dfs(1, 0)
print(max_len)