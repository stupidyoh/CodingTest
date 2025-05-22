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
row, col, num_rotate = map(int, input().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]

# 회전 구현
num_border = min(col, row) // 2

for b in range(num_border):
    start_row, start_col = b, b
    end_row, end_col = row - 1 - b, col - 1, - b

    for _ in range(num_rotate % ((end_row - start_row) * 2 + (end_col - start_col) * 2)):
        temp = matrix[start_row][start_col]

        # 위쪽 테두리 좌로 한 칸 이동




# 결과 출력
for r in range(row):
    print(*matrix[r])
