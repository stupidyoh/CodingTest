#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1743                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1743                           #+#        #+#      #+#     #
#    Solved: 2025/04/23 09:46:10 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque

# 주어진 입력받기
h, w, num_trash = map(int, input().split())
trash_map = [[0] * w for _ in range(h)]
visited = [[False] * w for _ in range(h)]

for _ in range(num_trash):
    y, x = map(int, input().split())
    trash_map[y-1][x-1] = 1

# 상하좌우 이동
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 정의
def bfs(x, y):
    q = deque([(x, y)])
    visited[y][x] = True
    count = 1

    while q:
        cx, cy = q.popleft()

        # 상하좌우 한칸씩 탐색
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            # 다음 지점이 맵 범위 내에 있으며, 방문한 적 없고, 쓰레기가 있는 지점이면
            if (0 <= nx < w and 0 <= ny < h 
                and not visited[ny][nx] and trash_map[ny][nx] == 1):

                count += 1
                visited[ny][nx] = True
                q.append((nx, ny))

    return count

biggest_trash = 0

# 맵 모든 범위 탐색
for j in range(h):
    for i in range(w):
        # 방문한 적 없고 쓰레기가 있는 곳만 탐색
        if not visited[j][i] and trash_map[j][i] == 1:
            cur_trash = bfs(i, j)

            # 제일 큰 음식물이면 업데이트
            if cur_trash > biggest_trash:
                biggest_trash = cur_trash

print(biggest_trash)