#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1303                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1303                           #+#        #+#      #+#     #
#    Solved: 2025/04/21 09:44:12 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque

# 주어진 입력받기
w, h = map(int, input().split())
battlefield = [list(input()) for _ in range(h)]

# 방문여부
visited = [[False] * w for _ in range(h)]

# 상하좌우 1칸씩 이동(동서남북)
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 정의
def bfs(x, y, color):
    # queue 초기화
    queue = deque([(x, y)])
    # 방문 체크
    visited[y][x] = True
    # 뭉친 인원 수 초기화
    count = 1

    while queue:
        # 현재 위치
        cx, cy = queue.popleft()

        # 상하좌우 한칸 움직인 위치
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            # 행렬 범위 내에 있으며 방문하지 않았고 같은 색상일 때
            if (0 <= nx < w and 0 <= ny < h and 
                battlefield[ny][nx] == color and not visited[ny][nx]):

                # 큐 추가(bfs 이어감), 새로운 위치 방문 체크, 뭉친 인원 수 +1
                queue.append((nx, ny))
                visited[ny][nx] = True
                count += 1

    return count # 뭉친 인원 수 반환

# 각 팀별 위력 초기화
power_w, power_b = 0, 0

# 행렬 크기만큼 확인
for j in range(h):
    for i in range(w):
        # 방문한 적 없을 경우만
        if not visited[j][i]:
            if battlefield[j][i] == "W":
                power_w += bfs(i, j, "W")**2
            else:
                power_b += bfs(i, j, "B")**2

print(power_w, power_b)