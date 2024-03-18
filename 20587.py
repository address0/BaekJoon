T = int(input())
for x in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    while True:
        q = a[0]
        i, j = 1, n-1
        swap = False
        while i <= j:
            while i <= j and a[i] <= q:
                i += 1
            while i <= j and a[j] >= q:
                j -= 1
            if i < j:
                a[i], a[j] = a[j], a[i]
                swap = True
        a[0], a[j] = a[j], a[0]
        if not swap:
            break
    print(a)