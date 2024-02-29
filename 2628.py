import sys
input = sys.stdin.readline
wid, hgt = map(int, input().split())
arr = [[0]*wid for _ in range(hgt)]
n = int(input())
for _ in range(n):
    test, cut = map(int, input().split())
    if test == 0:
        for i in range(cut, hgt):
            for j in range(wid):
                arr[i][j] += 1
    else:
        for i in range(hgt):
            for j in range(cut, wid):
                arr[i][j] += 1000
count = {}
for test in arr:
    for t in test:
        count.setdefault(t, 0)
        count[t] += 1
print(max(count.values()))