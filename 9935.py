testcase = list('mirkovC4nizCC44')
bomb = list('C4')
# testcase = list(input())
# bomb = list(input())
frula = testcase[:len(bomb)]
i = len(bomb)
while i < len(testcase):
    if frula[-len(bomb):] == bomb:
        for _ in range(len(bomb)):
            frula.pop()
    else:
        frula.append(testcase[i])
        i += 1
if frula[-len(bomb):] == bomb:
    frula = frula[:-len(bomb)]
if len(frula) > 0:
    print(''.join(frula))
else:
    print("FRULA")