n = int(input())
board = [i for i in range(1, n**2+1)]
queens = board[:]
for first in board:
    queen = first
    while True:
        testcase = queens[:]
        queens = []
        queen_bool = True
        for test in testcase:
            for i in range(-n, n):
                if test == queen + n * i or test == queen + i or test == queen + n * i + i:
                    queen_bool = False
                    break
                else:
                    continue
            if queen_bool:
                queens.append(test)
'''    
    for _ in range(n):
        board = queens[:]
        if board:
            queen = board.pop()
        else:
            break
        queens = []
        while board:
            test = board.pop()
            queen_bool = True
            for i in range(-n, n):
                if test == queen + n*i or test == queen + i or test == queen + n*i+i:
                    queen_bool = False
                    break
                else:
                    continue
            if queen_bool:
                queens.append(test)
    print(queen)
'''


'''
1  2  3  4
5  6  7  8 
9  10 11 12
13 14 15 16
'''