#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1932                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1932                           #+#        #+#      #+#     #
#    Solved: 2025/06/30 18:50:04 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

# 주어진 입력받기
n =  int(input())
triangles = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 누적합 계산
for h in range(1, n):
    for i in range(h+1):
        if i == 0:
            triangles[h][i] += triangles[h-1][i]
        elif i == h:
            triangles[h][i] += triangles[h-1][i-1]
        else:
            triangles[h][i] += max(triangles[h-1][i-1], triangles[h-1][i])

print(max(triangles[n-1]))