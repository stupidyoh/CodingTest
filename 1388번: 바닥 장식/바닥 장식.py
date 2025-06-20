#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1388                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1388                           #+#        #+#      #+#     #
#    Solved: 2025/06/20 18:46:05 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque

# 주어진 입력받기
n, m = map(int, input().split())
ground = []
for _ in range(n):
    ground.append(input())

# 방문 여부 초기화
visited = [[False] * m for _ in range(n)]

# 정답 초기화
num_plate = 0

def bfs(h, w):

    q = deque([(w, h)])

    visited[h][w] = True

    while q:
        x, y = q.popleft()

        if ground[y][x] == "|" and y < n - 1:
            nx, ny = x, y + 1
            if ground[ny][nx] == "|":
                q.append((nx, ny))
                visited[ny][nx] = True
        elif ground[y][x] == "-" and x < m - 1:
            nx, ny = x + 1, y
            if ground[ny][nx] == "-":
                q.append((nx, ny))
                visited[ny][nx] = True

for h in range(n):
    for w in range(m):
        if not visited[h][w]:
            bfs(h, w)
            num_plate += 1

print(num_plate)