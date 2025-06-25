#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11053                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11053                          #+#        #+#      #+#     #
#    Solved: 2025/06/25 20:37:13 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

# 주어진 입력받기
N = int(input())
arr = list(map(int, sys.stdin.readline().split()))

# dp 정의
dp = [1] * N

# dp 업데이트
for i in range(1, N):
    for j in range(i):  # 0부터 i-1까지 모든 이전 원소 확인
        if arr[j] < arr[i]:  # j번째 원소가 i번째보다 작으면
            dp[i] = max(dp[i], dp[j] + 1)

# 최대값 출력
print(max(dp))