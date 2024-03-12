import sys
input = sys.stdin.readline
def rotate(i, j, t):
    pass
n, m, k = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for _ in range(k):
    r, c, s = map(int, input())