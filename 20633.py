T = int(input())
def find_set(x):
    if nodes[x] == x:
        return x
    return find_set(nodes[x])

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        nodes[y] = x
    else:
        nodes[x] = y

for x in range(T):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    nodes = [0]*n
    for i in range(m):
        x1, x2 = nums[2*i], nums[2*i+1]
        nodes[x1-1] = x2
    visited = [0]*n
    result = 0
    for j in range(n):
        union(j, nodes[j])
    print(nodes)
    print(f'#{x+1} {result}')


def group(i, b):
    global result
    if visited[i]:
        return
    elif nodes[i]:
        group_b = False
        visited[i] = 1
        for k in range(len(nodes[i])):
            if not visited[nodes[i][k] - 1]:
                group(nodes[i][k] - 1, True)
            else:
                group_b = True
        if not group_b and not b:
            result += 1
    else:
        if not b:
            result += 1
        visited[i] = 1
        return
