from collections import deque
T = int(input())
for x in range(T):
    bats = deque(map(int, input().split()))
    n = bats.popleft()
    result = 0
    bat = bats.popleft()
    bats.append(0)
    for i in range(n-1):
        bat -= 1
        if stop > bat:
            bat = stop
            result += 1
    print(f'#{x+1} {result}')