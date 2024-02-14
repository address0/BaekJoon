n = int(input())
board = [i for i in range(1, n**2+1)]
queens = []
for queen in board:
    queens = board.pop()
    while board:
        test = board.pop()
        for i in range(n):
            if test:
                pass
'''
1  2  3  4
5  6  7  8 
9  10 11 12
13 14 15 16
'''