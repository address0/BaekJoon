import sys
input = sys.stdin.readline
n = int(input())
sols = list(map(int, input().split()))
i = 0
j = -1
result = 2000000000
x1, x2 = 0, 0
while i-j < n:
    mix = sols[i] + sols[j]
    if mix == 0:
        print(sols[i], sols[j])
        sys.exit()
    elif mix < 0:
        if abs(mix) < result:
            result = abs(mix)
            x1, x2 = sols[i], sols[j]
        i += 1
    else:
        if abs(mix) < result:
            result = abs(mix)
            x1, x2 = sols[i], sols[j]
        j -= 1
print(x1, x2)