#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15486                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15486                          #+#        #+#      #+#     #
#    Solved: 2025/04/30 19:29:59 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

# 주어진 입력받기
n = int(input())
schedules = []
for _ in range(n):
    schedules.append(list(map(int, sys.stdin.readline().split())))

# dp 초기화(dp[i+1]에 대한 경계처리를 위해 길이를 1 늘림)
dp = [0 for _ in range(n+1)]
# print(dp)

# n-1 ~ 0까지 역순 진행
for i in range(n-1, -1, -1):
    # 소요시간, 금액
    t, p = schedules[i]

    # 퇴사 전까지 상담 가능할 경우
    if t + i  <= n:
        # 오늘 상담비 + 소요시간 후 최대이익 vs. 내일 최대이익
        dp[i] = max(p + dp[t+i], dp[i+1])
        # print(dp)
    else:
        dp[i] = dp[i+1]

print(dp[0])

