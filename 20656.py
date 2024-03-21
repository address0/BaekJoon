import sys
sys.stdin = open('input.txt', 'r')

def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

T = int(input())
for x in range(T):
    v, E = map(int, input().split())
    edges = []
    for _ in range(E):
        s, e, w = map(int, input().split())
        edges.append([s, e, w])
    edges.sort(key=lambda x: x[2])
    sum_weight = 0
    cnt = 0
    parents = [i for i in range(v+1)]
    for s, e, w in edges:
        if find_set(s) != find_set(e):
            cnt += 1
            union(s, e)
            sum_weight += w
            if cnt == v:
                break
    print(f'#{x+1} {sum_weight}')