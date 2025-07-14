#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16973                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16973                          #+#        #+#      #+#     #
#    Solved: 2025/07/14 17:56:16 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

input = sys.stdin.readline

# 주어진 입력받기
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
H, W, Sr, Sc, Fr, Fc = map(int, input().split())

# 상하좌우 이동
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 방문여부
visited = [[False] * M for _ in range(N)]

# 벽 주변 이동 가능 가능 영역 전처리
for j in range(N):
    for i in range(M):
        if board[j][i] == 1:
            for y in range(j-H+1, j+1):
                for x in range(i-W+1, i+1):
                    if 0<=x<M and 0<=y<N:
                        board[y][x] = 1

# 가장자리 이동 가능 영역 전처리
for j in range(N):
    for i in range(M-W+1, M):
        board[j][i] = 1
for i in range(M):
    for j in range(N-H+1, N):
        board[j][i] = 1       

# bfs 정의(최단경로 찾기)
def bfs(sc, sr):
    q = deque([(sc, sr)])
    visited[sr][sc] = True

    while q:
        x, y = q.popleft()

        # 목표 도착시
        if x == Fc-1 and y == Fr-1:
            print(board[Fr-1][Fc-1])
            return

        # 상하좌우 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 직사각형이 격자판 내에 있고 좌상단 칸이 방문한 적 없는 칸이면
            if 0<=nx<M and 0<=ny<N and not visited[ny][nx] and board[ny][nx] == 0:
                q.append((nx, ny))
                visited[ny][nx] = True
                board[ny][nx] = board[y][x] + 1
    
    # 길이 없으면 -1 출력
    print(-1)

# 시작점에서 bfs 실행
bfs(Sc-1, Sr-1)