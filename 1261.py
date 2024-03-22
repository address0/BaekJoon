import sys
import heapq
input = sys.stdin.readline
m, n = map(int, input().split())
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
arr = [list(input().strip()) for _ in range(n)]
inf = int(1e9)
si, sj = 0, 0
distance = [[inf]*m for _ in range(n)]

def dijkstra(i, j):
    pq = []
    heapq.heappush(pq, [0, i, j])
    distance[i][j] = 0
    while pq:
        dist, ni, nj = heapq.heappop(pq)
        if distance[ni][nj] < dist:
            continue
        for k in range(4):
            if 0 <= ni+di[k] < n and 0 <= nj+dj[k] < m:
                if arr[ni+di[k]][nj+dj[k]] == '1':
                    cost = 1
                else:
                    cost = 0
                new_cost = dist + cost
                if new_cost >= distance[ni+di[k]][nj+dj[k]]:
                    continue
                distance[ni + di[k]][nj + dj[k]] = new_cost
                heapq.heappush(pq, [new_cost, ni+di[k], nj+dj[k]])

dijkstra(0, 0)
print(distance[-1][-1])