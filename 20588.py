T = int(input())
for x in range(T):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b_lst = list(map(int, input().split()))
    count = 0
    for b in b_lst:
        start, end = 0, n-1
        left, right = False, False
        time = 0
        while start <= end:
            mid = (start + end) // 2
            if a[mid] == b:
                count += 1
                break
            elif a[mid] < b:
                start = mid + 1
                time += 1
                if left:
                    break
                left = True
            else:
                end = mid-1
                time += 1
                if right:
                    break
                right = True
    print(f'#{x+1} {count}')