#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2468                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2468                           #+#        #+#      #+#     #
#    Solved: 2025/07/08 19:59:45 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

# 주어진 입력받기
N = int(input())
min_height = 101
max_height = 0
maps = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    min_row = min(row)
    max_row = max(row)
    if min_row < min_height:
        min_height = min_row
    if max_row > max_height:
        max_height = max_row
    maps.append(row)

# 최대 안전 영역 갯수 초기화
max_num_safe_area = 1

# 상하좌우 이동
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# bfs 정의
def bfs(x, y, h):
    global num_safe_area

    q = deque([(x, y)])
    visited[y][x] = True

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if (0<=nx<N) and (0<=ny<N) and not visited[ny][nx] and maps[ny][nx] > h:
                q.append((nx, ny))
                visited[ny][nx] = True

    num_safe_area += 1

# 물에 잠기는 높이별 탐색
for h in range(min_height, max_height):
    num_safe_area = 0
    # 방문 여부 확인
    visited = [[False] * N for _ in range(N)]
    for j in range(N):
        for i in range(N):
            if not visited[j][i] and maps[j][i] > h:
                bfs(i, j, h)

    if num_safe_area > max_num_safe_area:
        max_num_safe_area = num_safe_area

# 최대 안전 영역의 갯수 출력
print(max_num_safe_area)
