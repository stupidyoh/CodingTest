#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11403                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11403                          #+#        #+#      #+#     #
#    Solved: 2025/06/21 11:38:10 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque

# 주어진 입력받기
n = int(input())
g = []
for _ in range(n):
    g.append(list(map(int, input().split())))

# 정답 초기화
answer = [[0] * n for _ in range(n)]

# BFS 정의
def bfs(init_start):

    # 매 노드마다 방문 여부 초기화
    visited = [False for _ in range(n)]

    # 첫 노드 초기화
    q = deque([init_start])

    while q:
        # 시작지점
        start = q.popleft()

        # 다음 이동 가능 노드 탐색
        for end in range(n):
            # 노드가 연결되어 있고 방문한 적이 없다면
            if g[start][end] and not visited[end]:
                q.append((end))
                visited[end] = True
                answer[init_start][end] = 1

# 모든 노드에 대해 bfs 실행
for s in range(n):
    bfs(s)

# 정답 출력
for i in range(n):
    print(*answer[i])