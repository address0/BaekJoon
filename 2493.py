n = 5
result = [0]*n
testcase = list(map(int, '6 9 5 7 4'.split()))[::-1]
i = 1
top = testcase[-1]
testcase.pop()
while len(testcase) > 0:
    if testcase[-1] <= top:
        result[i] += k
    else:
        top = testcase[-1]
        k = testcase.index(top) + 1
    testcase.pop()
    i += 1
print(result)