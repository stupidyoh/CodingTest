#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16928                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16928                          #+#        #+#      #+#     #
#    Solved: 2025/07/10 18:43:45 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

# 주어진 입력받기
num_ladder, num_snake = map(int, sys.stdin.readline().split())

# 게임판 연결관계 그래프화
board = {}
for i in range(1, 100):
    board[i] = []
for i in range(1, 100):
    for j in range(1, 7):
        if i + j > 100:
            break
        board[i].append(i+j)

# 사다리/뱀칸 연결관계 리스트
ladder_snake = {}
for _ in range(num_ladder+num_snake):
    start, end = map(int, sys.stdin.readline().split())
    ladder_snake[start] = end

# 방문 처리
visited = [False] * 101

# bfs로 최단경로 찾기
def bfs(start):
    q = deque([(start, 0)]) # 시작칸, 주사위 굴린 횟수
    visited[1] = True

    while q:
        s, d = q.popleft()

        # 100번 칸에 도달했다면
        if s == 100:
            return d

        # 주사위 1~6으로 방문한 가능한 칸 bfs 탐색
        for next in board[s]:
            # 방문한 적 없는 칸이라면
            if not visited[next]:
                # 사다리나 뱀을 마주쳤다면
                if next in ladder_snake:
                    next = ladder_snake[next] # 도착칸을 사다리/뱀 끝칸으로 교체
                # 일반칸 - 방문한 적 없다면 / 사다리,뱀칸 - 시작, 끝점 모두 방문한 적 없다면
                if not visited[next]:
                    visited[next] = True # 방문처리
                    q.append((next, d+1)) # 주사위 횟수 추가

# 주사위 굴린 최소 횟수
print(bfs(1))