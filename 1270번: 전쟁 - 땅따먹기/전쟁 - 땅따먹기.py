#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1270                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1270                           #+#        #+#      #+#     #
#    Solved: 2025/07/01 19:58:17 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# v2: 딕셔너리 순회 탐색
# 더 오래걸림

# import sys

# # 주어진 입력받기
# num_ground = int(input())
# for _ in range(num_ground):
#     ground_info = list(map(int, sys.stdin.readline().split()))

#     soldier_dict = dict()
#     max_num = 0
#     max_soldier = 0
#     for soldier_num in ground_info[1:]:
#         soldier_dict[soldier_num] = soldier_dict.get(soldier_num, 0) + 1
#         if soldier_dict[soldier_num] > max_num:
#             max_num = soldier_dict[soldier_num]
#             max_soldier = soldier_num

#     if max_num > (ground_info[0] / 2):
#         print(max_soldier)
#     else:
#         print("SYJKGW")


#  **************************************************************************  #

# v1: Counter 함수 활용

import sys
from collections import Counter

# 주어진 입력받기
num_ground = int(input())
for _ in range(num_ground):
    ground_info = list(map(int, sys.stdin.readline().split()))
    # 병사 번호별 수 집계
    soldier_info = Counter(ground_info[1:])

    # 가장 많은 번호의 군대가 절반을 초과한다면
    if soldier_info.most_common()[0][1] > (ground_info[0] / 2):
        print(soldier_info.most_common()[0][0]) # 군대 번호 출력
    # 절반 이하라면
    else:
        print("SYJKGW")