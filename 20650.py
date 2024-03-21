import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
import heapq
T = int(input())
inf = int(1e9)
def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0
    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next_graph in graph[now]:
            next_node = next_graph[0]
            cost = next_graph[1]
            new_cost = dist + cost
            if new_cost >= distance[next_node]:
                continue
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))
for x in range(T):
    n, E = map(int, input().split())
    start = 0
    graph = [[] for i in range(n+1)]
    distance = [inf]*(n+1)
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([e, w])
    dijkstra(start)
    print(f'#{x+1} {distance.pop()}')