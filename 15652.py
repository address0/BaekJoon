import sys
imput = sys.stdin.readline
n, m = map(int, input().split())
result = [0]*m
arr = [i for i in range(1, n + 1)]
def f(i, k):
    if i == k:
        print(' '.join(list(map(str, result))))
    else:
        for j in range(n):
            if i == 0:
                result[i] = arr[j]
                f(i + 1, k)
            else:
                if result[i-1] <= arr[j]:
                    result[i] = arr[j]
                    f(i + 1, k)
f(0, m)