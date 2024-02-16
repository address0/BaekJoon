import sys
input = sys.stdin.readline
n, m = map(int, input().split())
result = [0]*m
arr = [x for x in range(1, n+1)]

def f(i, k):
    if i == k:
        print(' '.join(list(map(str, result))))
    else:
        for j in range(n):
            result[i] = arr[j]
            if i > 0 and result[i-1] >= result[i]:
                pass
            else:
                f(i + 1, k)

f(0, m)