import sys
input = sys.stdin.readline
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
r, c = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]
i, j = 0, 0
al = arr[0][0]
st = [[i, j]]
als = [al]
# visited = [[0]*c for _ in range(r)]
time = 1
result = 0
while st:
    move = False
    for k in range(4):
        if 0 <= i+di[k] < r and 0 <= j+dj[k] < c:
            if arr[i+di[k]][j+dj[k]] not in als:
                time += 1
                i += di[k]
                j += dj[k]
                st.append([i, j])
                als.append(arr[i][j])
                move = True
                break
    if not move:
        if time > result:
            result = time
        i, j = st.pop()
        als.pop()
        time -= 1
def dfs(i, j, st, time):
    global result
    if time > result:
        result = time
    for k in range(4):
        if 0 <= i+di[k] < r and 0 <= j+dj[k] < c:
            if arr[i+di[k]][j+dj[k]] not in visited:
                st.append([i+di[k], j+dj[k]])
                visited.append(arr[i+di[k]][j+dj[k]])
                dfs(i+di[k], j+dj[k], st, time+1)
                st.pop()

print(result)