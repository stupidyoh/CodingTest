#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2056                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2056                           #+#        #+#      #+#     #
#    Solved: 2025/06/25 20:37:28 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

# 주어진 입력받기
N = int(input())
works = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# dp 정의
dp = [0] * N

for i in range(N):
    # 선행작업이 없으면
    if works[i][1] == 0:
        # 작업종료시간 = 작업시간
        dp[i] = works[i][0]
        continue

    # 선행작업 탐색
    preceding_work = []
    for p in works[i][2:]:
        preceding_work.append(dp[p-1])

    # 선행작업이 있으면 선행작업 중 가장 늦게 끝난 시간 + 작업시간
    dp[i] = max(preceding_work) + works[i][0]

# 모든 작업이 종료된 시간
print(max(dp))