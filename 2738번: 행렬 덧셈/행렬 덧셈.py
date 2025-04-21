#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2738                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2738                           #+#        #+#      #+#     #
#    Solved: 2025/04/21 09:31:40 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# v2
# 행렬 A만 저장하고 B는 입력받는 즉시 A에 더해서 결과 출력

n, m = map(int, input().split())

matrix_a = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    print(*[a+b for a, b in zip(matrix_a[i], map(int, input().split()))])

# ---------------------------------------------------------------------------- #

# v1
# 행렬 A와 B를 각각 저장해서 출력하는 방식

# n, m = map(int, input().split())
# matrix_a = []
# matrix_b = []

# for _ in range(n):
#     matrix_a.append(list(map(int, input().split())))

# for _ in range(n):
#     matrix_b.append(list(map(int, input().split())))

# for row in range(n):
#     for col in range(m):
#         print(matrix_a[row][col] + matrix_b[row][col], end=' ')
#     print()