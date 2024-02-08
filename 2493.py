# import sys
# input = sys.stdin.readline
# n = int(input())
n = 5
result = [0]*n
testcase = list(map(int, '5 4 3 2 1'.split()))
test_index = []
for x in range(n):
    test_index.append(x)
stack = []
i = 1
stack.append(testcase.pop())
for i in range(n):
    if testcase[-1] >= stack[-1]:
        result[-i] += n - i
        break
    else:
        test_index.pop()
    stack.append(testcase.pop())
print(result)