#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5557                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5557                           #+#        #+#      #+#     #
#    Solved: 2025/05/01 09:40:14 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
# from pprint import pprint

# 주어진 입력받기
n = int(input())
numbers = list(map(int, sys.stdin.readline().split()))

# i(0~n-2)번째 단계에 0이상 20이하의 수가 될 수 있는 경우의 수 표현
dp = [[0 for _ in range(21)] for _ in range(n-1)]

for i in range(n-1):
    # 첫 번째 값은 바로 입력
    if i == 0:
        dp[i][numbers[i]] = 1
        continue

    # 0~20까지 확인
    for j in range(21): 
        # 이전 단계 경우가 있을시
        if dp[i-1][j] > 0:
            # 더하거나 뺐을 때 범위 안에 있을시
            if 0 <= (j + numbers[i]) <= 20:
                dp[i][j+numbers[i]] += dp[i-1][j]
            if 0 <= (j - numbers[i]) <= 20:
                dp[i][j-numbers[i]] += dp[i-1][j]

# pprint(dp)
print(dp[n-2][numbers[n-1]])