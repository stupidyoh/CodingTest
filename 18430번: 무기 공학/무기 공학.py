#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 18430                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/18430                          #+#        #+#      #+#     #
#    Solved: 2025/07/05 13:01:46 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 주어진 입력받기
height, width = map(int, input().split())
woods = [list(map(int, input().split())) for _ in range(height)]

# 부메랑 모양 정의(문제 그림 순: ㄱ, 역ㄴ, ㄴ, 역ㄱ)
dx = [(-1, 0), (-1, 0), (0, 1), (0, 1)]
dy = [(0, 1), (0, -1), (-1, 0), (1, 0)]

# 방문 여부
visited = [[False] * width for _ in range(height)]

# 최대 강도 합
max_strength = 0

def dfs_with_backtracking(x, y, strength):
    global max_strength
    max_strength = max(strength, max_strength)

    if y == height:
        return

    # 부메랑이 채워지지 않았다면
    if not visited[y][x]:
        for i in range(4):
            nx1, ny1 = x + dx[i][0], y + dy[i][0]
            nx2, ny2 = x + dx[i][1], y + dy[i][1]

            if (0<=nx1<width) and (0<=nx2<width) and (0<=ny1<height) and (0<=ny2<height):
                if (not visited[ny1][nx1]) and (not visited[ny2][nx2]):
                    visited[y][x] = True
                    visited[ny1][nx1] = True
                    visited[ny2][nx2] = True

                    # 재귀 계산
                    # 마지막 열 도달시 다음 행으로 이동
                    if x == width - 1:
                        dfs_with_backtracking(0, y + 1, strength + 2 * woods[y][x] + woods[ny1][nx1] + woods[ny2][nx2])
                    # 다음 열로 이동
                    else:
                        dfs_with_backtracking(x + 1, y, strength + 2 * woods[y][x] + woods[ny1][nx1] + woods[ny2][nx2])
    
                    # 백트래킹
                    visited[y][x] = False
                    visited[ny1][nx1] = False
                    visited[ny2][nx2] = False

    # 중심점이 방문했던 곳이거나 방문하지 않았어도 재귀를 끝내고 다음 탐색
    # 마지막 열 도달시 다음 행으로 이동
    if x == width - 1:
        dfs_with_backtracking(0, y + 1, strength)
    # 다음 열로 이동
    else:
        dfs_with_backtracking(x + 1, y, strength)


dfs_with_backtracking(0, 0, 0)

print(max_strength)
