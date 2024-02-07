x = 0
while True:
    testcase = list(input())
    if '-' in testcase:
        break
    count = 0
    result = testcase[:1]
    for i in range(1, len(testcase)):
        result.append(testcase[i])
        if len(result) >= 2:
            if result[-1] == '}':
                if result[-2] == '{':
                    result.pop()
                    result.pop()
                else:
                    continue
            else:
                continue
    while len(result) > 0:
        if result[-1] == '{':
            result[-1] = '}'
            count += 1
            if result[-2] == '{':
                result.pop()
                result.pop()
            else:
                result[-2] = '{'
                count += 1
                result.pop()
                result.pop()
        else:
            count += (len(result) // 2)
            result = []
    x += 1
    print(f'{x}. {count}')