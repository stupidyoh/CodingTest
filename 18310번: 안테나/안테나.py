#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 18310                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/18310                          #+#        #+#      #+#     #
#    Solved: 2025/06/24 20:00:05 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 주어진 입력받기
N = int(input())
houses = list(map(int, input().split()))

# 오름차순 정렬
houses.sort()

# 양끝을 기준으로 그 사이 어느 집을 고르던 거리의 합은 동일
# 집의 수가 홀수이면 가운데집으로부터의 거리가 최소
if len(houses) % 2 == 1:
    print(houses[len(houses) // 2])
# 집의 수가 짝수이면 중앙에 가까운 두 집 중 어느 곳을 기준으로 거리를 계산해도 동일    
else:
    print(houses[len(houses) // 2 - 1])

#  **************************************************************************  #

# 기준 1
# 4+6+8 = 18

# 기준 5
# 4+2+4 = 10

# 기준 6
# 5+1+1+3 = 10

# 기준 7
# 6+2+2 = 10

# 기준 9
# 8+4+2 = 14

#  **************************************************************************  #

# from collections import Counter
# import sys

# # 주어진 입력받기
# N = int(input())
# houses = list(map(int, input().split()))

# count_dict = Counter(houses)

# max_distance = sys.maxsize
# answer = 0

# for standard in count_dict.keys():
#     distance = 0
#     for k, v in count_dict.items():
#         distance += abs(standard - k) * v
    
#     if distance < max_distance:
#         max_distance = distance
#         answer = standard

# print(answer)