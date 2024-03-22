t = int(input())
for x in range(t):
    n, num = list(input().split())
    int_num = int(num, 16)
    bin_num = str(bin(int_num))
    print(f'#{x+1} {str(bin_num[2:].zfill(int(n) * 4))}')