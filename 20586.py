T = int(input())
def merge(left, right):
    result = []
    i, j = 0, 0
    if left[-1] > right[-1]:
        global count
        count += 1
    while i < len(left) or j < len(right):
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif i < len(left):
            result.append(left[i])
            i += 1
        elif j < len(right):
            result.append(right[j])
            j += 1
    return result
def merge_sort(lst, k):
    if k == 1:
        return lst
    mid = k // 2
    left_lst = []
    right_lst = []
    for l in range(k):
        if l < mid:
            left_lst.append(lst[l])
        else:
            right_lst.append(lst[l])
    left = merge_sort(left_lst, mid)
    right = merge_sort(right_lst, k-mid)
    return merge(left, right)
for x in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    total = merge_sort(arr, n)
    print(f'#{x+1} {total[n//2]} {count}')
