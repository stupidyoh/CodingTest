#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14502                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14502                          #+#        #+#      #+#     #
#    Solved: 2025/05/22 10:29:50 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from itertools import combinations
from collections import deque
# from pprint import pprint

# 주어진 입력받기
h, w = map(int, input().split())
map_lab = [list(map(int, input().split())) for _ in range(h)]

empties = set()
virus = set()
for j in range(h):
    for i in range(w):
        if map_lab[j][i] == 0:
            empties.add((i, j))
        elif map_lab[j][i] == 2:
            virus.add((i, j))

# 상하좌우 이동
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# temp = 0
max_safe_area = 0

for comb in combinations(empties, 3):
    # print(comb)
    map_wall = [row[:] for row in map_lab]
    for c in comb:
        map_wall[c[1]][c[0]] = 1
    
    # if temp == 0:
    #     print(comb)
    #     pprint(map_wall)
    # temp+=1

    def virus_simulation(virus_loc):
        q = deque()

        for v in virus_loc:
            q.append(v)

        while q:
            x, y = q.pop()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if (0<= nx < w) and (0<= ny < h) and map_wall[ny][nx] == 0:
                    map_wall[ny][nx] = 2
                    q.append((nx, ny))

    virus_simulation(virus)

    num_safe_area = 0
    for row in map_wall:
        num_safe_area += row.count(0)

    max_safe_area = max(max_safe_area, num_safe_area)

print(max_safe_area)