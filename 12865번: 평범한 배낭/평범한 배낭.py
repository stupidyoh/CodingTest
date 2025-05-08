#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 12865                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/12865                          #+#        #+#      #+#     #
#    Solved: 2025/05/08 19:36:13 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
# from pprint import pprint

# 주어진 입력받기
num_object, weight_limit = map(int, input().split())
objects = [list(map(int, sys.stdin.readline().split())) for _ in range(num_object)]

# dp[고려한 물건 수][무게제한] = 얻을 수 있는 최대 가치
dp = [[0 for _ in range(weight_limit+1)] for _ in range(num_object+1)]

# 물건을 차례대로 꺼냄
for i in range(1, num_object+1):
    # 꺼낸 물건의 무게와 가치
    weight, value = objects[i-1]

    # 가능한 가방 무게제한
    for j in range(weight_limit+1):
        # 가방 무게제한 < 물건 무게(못 넣음)
        if j < weight:
            dp[i][j] = dp[i-1][j]
        # 가방 무게제한 > 물건 무게(넣을 수도 있음)
        else:
            # 넣지 않는 경우와 넣는 경우 둘 중 더 큰 가치 선택
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
        # pprint(dp)

print(dp[num_object][weight_limit])