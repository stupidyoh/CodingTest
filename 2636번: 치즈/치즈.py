#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2636                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2636                           #+#        #+#      #+#     #
#    Solved: 2025/07/17 18:52:39 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

# 주어진 입력받기
H, W = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

# 상하좌우 탐색
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 구멍 찾는 함수 - (0,0)에서 bfs해서 연결된 부분은 전부 바깥 공기
# 그 외는 치즈 구멍
def find_hole():
    # 바깥 공기 탐색
    air = set()
    q = deque([(0, 0)])
    air.add((0, 0))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 판 내부에 있고, 방문한 적 없고, 공기일 때
            if (0<=nx<W) and (0<=ny<H) and board[ny][nx] == 0:
                if (nx, ny) not in air:
                    q.append((nx, ny))
                    air.add((nx, ny))

    # 치즈 구멍 탐색
    holes = set()
    for y in range(1,H-1):
        for x in range(1, W-1):
            if board[y][x] == 0 and (x, y) not in air:
                holes.add((x, y))

    return holes

# 가장자리 찾는 함수 - 상하좌우에 0이 있는지(구멍은 제외)
def find_border():
    for y in range(H):
        for x in range(W):
            if board[y][x] == 1:
                
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]

                    # 상하좌우 중 공기가 있을 경우, 가장자리임
                    if board[ny][nx] == 0 and (nx, ny) not in holes:
                        borders.add((x, y))
                        break

# 가장자리 녹이는 함수
def delete_border():
    for border in borders:
        x, y = border
        board[y][x] = 0

# 치즈 갯수 찾는 함수(1 갯수 세기)
def count_cheese():
    num_cheese = 0
    for y in range(H):
        for x in range(W):
            if board[y][x] == 1:
                num_cheese += 1
    return num_cheese

# from pprint import pprint

# 녹는 시간
time = 0

# 처음 치즈 개수
num_cheese = count_cheese()

while True:
    # 구멍 위치 탐색
    holes = find_hole()
    # print(holes)

    # 가장자리 위치 튜플
    borders = set()
    # 가장자리 탐색
    find_border()
    # print(borders)

    # 치즈 갯수가 가장자리 갯수와 같으면 다음 차례에 다 녹음
    if num_cheese == len(borders):
        print(time+1) # 다 녹는 데 걸린 시간
        print(num_cheese) # 다 녹기 1시간 전 치즈 갯수
        break

    # 가장자리 제거
    delete_border()
    # pprint(board)
    
    # 가장자리 제거 후 치즈 갯수
    num_cheese -= len(borders)

    # 한 시간 추가
    time+=1