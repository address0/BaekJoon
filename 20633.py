T = int(input())
def find_set(x):
    if people[x] == x:
        return x
    return find_set(people[x])

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        people[y] = x
    else:
        people[x] = y

for x in range(T):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    nodes = [0]*n
    people = list(range(n+1))
    for i in range(m):
        x1, x2 = nums[2*i], nums[2*i+1]
        union(x1, x2)
    result = 0
    group = set(people)
    print(f'#{x+1} {len(group)-1}')