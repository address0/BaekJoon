sen = list(input().strip())
s = len(sen)
n = int(input())
for _ in range(n):
    word = input()
    while True:
        sen_lst = []
        for w in word:
            pass_bool = False
            for i in range(s):
                if w == sen[i]:
                    sen_lst.append(i)
                    pass_bool = True
                    break
            if not pass_bool:
                break
        if pass_bool:
            del sen[sen_lst]
        else:
            break
    print(sen)