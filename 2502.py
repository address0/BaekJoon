import sys
input = sys.stdin.readline
def sub(i):
    if i == 2:
        rice = [arr[bit[0]], arr[bit[1]]]
        for _ in range(d - 2):
            rice.append(rice[-1] + rice[-2])
            if rice[-1] > total:
                break
        if rice[-1] == total:
            print(rice[0])
            print(rice[1])
            sys.exit()
    else:
        for j in range(k):
            if i > 0:
                if j >= bit[i-1]:
                    bit[i] = j
            else:
                bit[i] = j
            sub(i+1)
d, k = map(int, input().split())
total = k
for _ in range(d-2):
    k = int(k*2/3+0.9)
arr = list(range(1, k+1))
bit = [0, 0]
sub(0)