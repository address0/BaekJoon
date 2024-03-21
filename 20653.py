import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())
for x in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    i, j = 0, 0
    visited = []
    while i < n-1 or j < n-1:
        pass