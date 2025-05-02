#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11559                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11559                          #+#        #+#      #+#     #
#    Solved: 2025/05/02 09:46:20 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
from pprint import pprint

# 주어진 입력받기
map = [list(map(str, input().strip())) for _ in range(12)]
visited = [[False] * 6 for _ in range(12)]

# 연쇄 갯수
chains = 0
is_bomb = True

# 상하좌우 탐색
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# bfs로 연쇄 구현
def bfs(x, y):
    q = deque([(x, y)])
    color = map[y][x]
    visited[y][x] = True
    connected = 1
    temp_chain = [(x, y)]

    while q:
        cx, cy = q.pop()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if (0<= nx < 6 and 0 <= ny < 12 and not visited[ny][nx] and map[ny][nx] == color):
                q.append((nx, ny))
                visited[ny][nx] = True
                connected += 1
                temp_chain.append((nx, ny))

    if connected >= 4:
        # print("connect: ", connected)
        # print("temp_chain: ", temp_chain)
        for c in temp_chain:
            map[c[1]][c[0]] = "."
        global is_bomb
        # chains += 1
        is_bomb = True

# 중력 방향으로 떨어지는 기능
def gravity():
    # 각 열에 대해서 시행
    for i in range(6):
        gravity_stack = []
        for j in range(11, -1, -1):
            if map[j][i] != '.':
                gravity_stack.append(map[j][i])
        
        limit = len(gravity_stack)
        for k in range(12):
            if k < limit:
                map[11-k][i] = gravity_stack[k]
            else:
                map[11-k][i] = '.'

while is_bomb:
    is_bomb = False
    visited = [[False] * 6 for _ in range(12)]

    for h in range(12):
        for w in range(6):
            if map[h][w] != '.' and not visited[h][w]:
                bfs(w, h)
                # pprint(map)

    if is_bomb:
        chains += 1
        gravity()
    # pprint(map)

print(chains)