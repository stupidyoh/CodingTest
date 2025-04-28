#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16197                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16197                          #+#        #+#      #+#     #
#    Solved: 2025/04/28 09:54:21 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

# 주어진 입력받기
h, w = map(int, input().split())
board = list(sys.stdin.readline().strip() for _ in range(h))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 초기 동전 위치 탐색
position_coins = []
for j in range(h):
    for i in range(w):
        if board[j][i] == 'o':
            position_coins.append((i, j))


def bfs(x1, y1, x2, y2):
    q = deque([(x1, y1, x2, y2, 0)])

    while q:
        cx1, cy1, cx2, cy2, count = q.popleft()

        if count >= 10:
            return -1

        for i in range(4):
            nx1, ny1 = cx1 + dx[i], cy1 + dy[i]
            nx2, ny2 = cx2 + dx[i], cy2 + dy[i]

            # 둘 다 보드 안에 있는 경우
            if (0 <= nx1 < w and 0 <= ny1 < h and 0 <= nx2 < w and 0 <= ny2 < h):
                # 벽을 마주할 경우
                if board[ny1][nx1] == "#":
                    nx1, ny1 = cx1, cy1
                if board[ny2][nx2] == "#":
                    nx2, ny2 = cx2, cy2
                q.append((nx1, ny1, nx2, ny2, count + 1))
            
            # 둘 중 하나만 보드 안에 있는 경우
            elif (0 <= nx1 < w and 0 <= ny1 < h) or (0 <= nx2 < w and 0 <= ny2 < h):
                return count + 1

    return -1

count = bfs(position_coins[0][0], position_coins[0][1], position_coins[1][0], position_coins[1][1])

print(count)