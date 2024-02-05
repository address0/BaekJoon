T = int(input())
group_words = 0
for _ in range(T):
    testcase = input()
    count = []
    count.append(testcase[0])
    result = True
    for i in range(1, len(testcase)):
        if testcase[i] in count:
            if testcase[i - 1] == testcase[i]:
                continue
            else:
                result = False
                break
        count.append(testcase[i])
    if result is True:
        group_words += 1
print(group_words)