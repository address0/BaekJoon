import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    while a != b:
        if a > b:
            a //= 2
        elif a < b:
            b //= 2
    print(a*10)