#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2565                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2565                           #+#        #+#      #+#     #
#    Solved: 2025/06/30 18:50:09 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

# 주어진 입력받기
num_line = int(input())
connections = [list(map(int, sys.stdin.readline().split())) for _ in range(num_line)]

# A전봇대 기준으로 오름차순 정렬
connections.sort(key = lambda x: x[0])

# dp 초기화
dp = [1] * num_line

# dp 계산
# B전봇대 기준으로 가장 긴 증가하는 수열 찾기(자르지 않아도 되는 최대 전깃줄 개수 구하기)
for i in range(1, num_line):
    for j in range(i):
        if connections[j][1] < connections[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

# 최소 없앨 전깃줄 갯수 출력
print(num_line - max(dp))