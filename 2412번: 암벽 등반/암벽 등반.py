#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2412                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2412                           #+#        #+#      #+#     #
#    Solved: 2025/07/16 17:13:28 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

# 주어진 입력받기
n, T = map(int, sys.stdin.readline().split())
holes = {tuple(map(int, sys.stdin.readline().split())) for _ in range(n)}

# 방문 여부
visited = set()

# bfs 정의
def bfs():
    q = deque([(0, 0, 0)]) # x좌표, y좌표, 이동횟수 초기값
    visited.add((0, 0))

    while q:
        x, y, d = q.popleft()

        # 정상 도달시
        if y == T:
            print(d)
            return

        # 범위 내에 갈 수 있는 곳이 탐색
        for dy in range(-2, 3):
            for dx in range(-2, 3):
                nx, ny = x + dx, y + dy

                # 범위 내 갈 수 있는 홈이 있고 방문한 적 없으면
                if (nx, ny) in holes and (nx, ny) not in visited:
                    q.append((nx, ny, d+1))
                    visited.add((nx, ny))

    # 정상 미도달시
    print(-1)
    return

# bfs 실행
bfs()