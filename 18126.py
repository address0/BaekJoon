import sys
input = sys.stdin.readline
n = int(input())
roads = [[] for _ in range(5000)]
def dfs(v, len):
    if not roads[v]:
        global max_len
        if len > max_len:
            max_len = len
    else:
        for road in roads[v]:
            print(road, len)
            if not visited[road[0]-1]:
                visited[road[0]-1] += 1
                dfs(road[0]-1, len+road[1])
for _ in range(n-1):
    a, b, c = map(int, input().split())
    roads[a-1].append([b, c])
max_len = 0
visited = [0]*5000
dfs(0, 0)
print(max_len)