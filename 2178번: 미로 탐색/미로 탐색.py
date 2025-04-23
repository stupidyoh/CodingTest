#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2178                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2178                           #+#        #+#      #+#     #
#    Solved: 2025/04/22 09:51:57 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque

# 주어진 입력 받기
h, w = map(int, input().split())
maze_map = [list(map(int, input().strip())) for _ in range(h)]

# 상하좌우 1칸씩 이동
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 정의
def bfs(x, y):
    q = deque([(x, y)])
    
    while q:
        # 현재 위치
        cx, cy = q.popleft()
        
        # 상하좌우 1칸씩 모두 탐색
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            
            # 미로 범위 내에 있으며 다음 이동할 위치가 길일 때(1일 때)
            if (0 <= nx < w and 0 <= ny < h and maze_map[ny][nx] == 1):
                # 현재 위치 값을 이동거리로 계산(다음 위치 = 현재 위치 + 1)
                maze_map[ny][nx] = maze_map[cy][cx] + 1
                q.append((nx, ny))
                
bfs(0, 0)

print(maze_map[h-1][w-1])