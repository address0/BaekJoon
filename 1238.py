import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
for x in range(10):
    contacts = [[] for _ in range(101)]
    l, s = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(l//2):
        x1, x2 = arr[2*i], arr[2*i+1]
        if x2 not in contacts[x1]:
            contacts[x1].append(x2)
    visited = [0]*101
    visited[s] = 1
    max_call, max_num = 1, s
    q = deque()
    q.append(s)
    while q:
        call = q.popleft()
        if contacts[call]:
            for c in contacts[call]:
                if not visited[c]:
                    visited[c] = visited[call]+1
                    q.append(c)
                    if max_call < visited[c] or (max_call == visited[c] and max_num < c):
                        max_call = visited[call]
                        max_num = c
    print(f'#{x+1} {max_num}')