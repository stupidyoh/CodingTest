#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16926                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16926                          #+#        #+#      #+#     #
#    Solved: 2025/05/15 10:21:28 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

# 주어진 입력받기
col, row, num_rotate = map(int, input().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(col)]

# 회전한 배열
matrix_rotated = [[0] * row for _ in range(col)]

# 회전 구현




# 결과 출력
for c in range(col):
    print(*matrix_rotated[c])
